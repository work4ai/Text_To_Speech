# Importing required modules
import PyPDF2
import pyttsx3

# Path of the PDF file
with open('transformer.pdf', 'rb') as path:
    # Creating a PdfReader object
    pdf_reader = PyPDF2.PdfReader(path)

    # Selecting the 10th page (index 9)
    from_page = pdf_reader.pages[9]

    # Extracting text using the latest function
    text = from_page.extract_text()

# Initializing text-to-speech engine
speak = pyttsx3.init()

# Reading the extracted text
speak.say(text)
speak.runAndWait()
