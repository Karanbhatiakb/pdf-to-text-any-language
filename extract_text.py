import PyPDF2
from googletrans import Translator

doc = PyPDF2.PdfFileReader('Document.pdf')

data = doc.getPage(0).extractText()
print(data)

translator = Translator()
print("Please select language to translate")
print("1. English")
print("2. Hindi")
print("3. Spanish")
print("4. French")
print("5. Arabic")

num = int(input("Enter number here: "))
if num == 1:
    lan = "en"
elif num == 2:
    lan = "hi"
elif num == 3:
    lan = "es"
elif num == 4:
    lan = "fr"
elif num == 5:
    lan = "ar"
else:
    print("Enter Valid Number")

translated = translator.translate(data,dest=lan)
print(translated.text)
new_text = translated.text

with open("Document.txt",'w') as f:
    f.write(new_text)
