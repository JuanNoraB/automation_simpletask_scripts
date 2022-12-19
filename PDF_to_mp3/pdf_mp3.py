
import pyttsx3,PyPDF2

engine = pyttsx3.init()

pdfreader= PyPDF2.PdfFileReader(open('Stephen_Hawking_Historia_del_Tiempo.pdf','rb'))
speaker=pyttsx3.init() #inicalization fo speaker


page_num = 9

page = pdfreader.getPage(page_num)
text = page.extractText()
total_text = text
total_pages = pdfreader.numPages
while page_num < total_pages:
    page_num = page_num + 1
    page = pdfreader.getPage(page_num)
    text = page.extractText()
    text = text.replace('’','')
    text = text.replace('“','')
    text = text.replace('”','')
    text = text.replace('‘','')
    text = text.replace('\n',' ')
    total_text += text

speaker.save_to_file(total_text ,'AudioBook.mp3')
speaker.runAndWait()
speaker.stop()


