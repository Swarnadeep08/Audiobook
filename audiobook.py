import pyttsx3
import PyPDF2

book = open('Harry-Potter-and-the-Prisoner-of-Azkaban.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
total_pages = pdfReader.numPages
print(total_pages)

reader = pyttsx3.init()

for page_no in range(6, total_pages):
    page = pdfReader.getPage(page_no)
    text = page.extractText()
    reader.say(text)
    reader.runAndWait()

book.close()