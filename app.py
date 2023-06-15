import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTextEdit, QPushButton, QFileDialog, QLineEdit
import PyPDF2
import openai
import requests
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import Qt

openai.api_key = ''  # write your API key here

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Question Answer')
        self.setGeometry(100, 100, 500, 600)

        # Create a widget to hold the button and labels
        widget = QWidget()
        self.setCentralWidget(widget)
        
        # create upload button
        self.upload_button = QPushButton('Upload PDF', self)
        self.upload_button.setGeometry(50, 50, 100, 30)
        self.upload_button.clicked.connect(self.upload_file)

        # Create a label to display the selected file path
        self.path_label = QLabel("", self)
        self.path_label.setGeometry(170, 50, 300, 30)
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.path_label.setFont(font)
        
        # create question label
        self.question_label = QLabel('Ask a question:', self)
        self.question_label.setGeometry(50, 100, 100, 30)


        # create question text box
        self.question_text_box = QLineEdit(self)
        self.question_text_box.setGeometry(50, 150, 400, 30)
        
        # create answer label
        self.answer_label = QLabel('Answer:', self)
        self.answer_label.setGeometry(50, 200, 100, 30)
        
        # create answer text box
        self.answer_text_box = QTextEdit(self)
        self.answer_text_box.setGeometry(50, 250, 400, 100)
        self.answer_text_box.setReadOnly(True)

        # create pdf display label
        self.question_label = QLabel('pdf text', self)
        self.question_label.setGeometry(50, 375, 100, 30)

        # create pdf display text box
        self.pdf_text = QTextEdit(self)
        self.pdf_text.setGeometry(50, 425, 400, 120)
        self.pdf_text.setReadOnly(True)
        print("In constructor")
    
    def upload_file(self):

        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PDF files (*.pdf)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        pdf_text_display="Nothing Selected"
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.path_label.setText(selected_file)

            pdfFileObj = open(selected_file, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            page_number = len(pdfReader.pages)
            text = ' '
            for page_num in range(page_number):
                pageObj = pdfReader.pages[page_num]
                text += pageObj.extract_text()

            if len(text) <= 150:
                pdf_text_display = text
            else:
                pdf_text_display = text[0:150]

            self.pdf_text.setText(pdf_text_display)
            
            question = self.question_text_box.text()
            if question:
                # use GPT-3 to generate answer
                prompt = f"Question: {question}\nContext: {text}\nAnswer:"
                response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n"]
                )
                answer = response.choices[0].text.strip()
                if len(answer) <= 200:
                    answer_display = answer
                else:
                    answer_display = answer[0:200]

                print(answer_display)
                self.answer_text_box.setText(answer_display)
                #return answer

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    
