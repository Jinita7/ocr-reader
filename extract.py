from PIL import Image
import pytesseract

def read_image (path):
   imag=Image.open(path)
   text =pytesseract.image_to_string(imag)
   return text