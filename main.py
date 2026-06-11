from extract import read_image
from clean_text import cleaned
from excel import excel

text=read_image("image.png")

text1=cleaned(text)

finaltext=excel(text1)

print ("output successfully created")
