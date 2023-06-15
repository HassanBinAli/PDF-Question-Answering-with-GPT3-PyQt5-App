
# PDF-Question-Answering-with-GPT3-PyQt5-App
This is a pyqt5 app. It asks user to upload a pdf file. It is powered by GPT3. User can ask question about the pdf text. App will show the answer to that question using GPT3.




## Install Dependencies
```
pip install PyQt5
pip install pyqt5-tools
pip install openai
pip install PyPDF2
```
## Clone this repo
```
git clone https://github.com/HassanBinAli/PDF-Question-Answering-with-GPT3-PyQt5-App
cd PDF-Question-Answering-with-GPT3-PyQt5-App
```
## Write your API-key provided by OpenAI
In 9th line of the code, put your API key

![image](https://github.com/HassanBinAli/PDF-Question-Answering-with-GPT3-PyQt5-App/assets/87352841/89f5d15c-efd3-4eb4-ae40-cf87886fd74e)

## Run and test
Run the file app.py using following command in terminal
```
python3 app.py
```

Following GUI will appear

![Capture0](https://github.com/HassanBinAli/PDF-Question-Answering-with-GPT3-PyQt5-App/assets/87352841/1858d31a-19ea-4e69-aeb7-c94db858564f)

## Improvements
  1) First you have to write your question, then upload the pdf. Another problem followns when you try to ask another question and hit enter. It doesn't work. You have to do it from start.
  2) It doesn't take images in a pdf into account. This functionality can be added using OCR to extract text from images.
