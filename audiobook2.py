import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf


bg = '#ffdab9'
app = Tk()
app.geometry("800x800")
app.title("Audiobook")
app.configure(bg=bg)

row0 = Frame(app, bg=bg)
row0.pack(side='top', fill='y', anchor='n')

row1 = Frame(app, bg=bg)
row1.pack(side='top', fill='y', anchor='n')

row2 = Frame(app, bg=bg)
row2.pack(side='top', fill='y', anchor='n')

row3 = Frame(app, bg=bg)
row3.pack(side='top', fill='y', anchor='n')

row4 = Frame(app, bg=bg)
row4.pack(side='top', fill='y', anchor='n')

row5 = Frame(app, bg=bg)
row5.pack(side='top', fill='y', anchor='n')

row6 = Frame(app, bg=bg)
row6.pack(side='top', fill='y', anchor='n')

row7 = Frame(app, bg=bg)
row7.pack(side='top', fill='y', anchor='n')

row8 = Frame(app, bg=bg)
row8.pack(side='top', fill='y', anchor='n')

row9 = Frame(app, bg=bg)
row9.pack(side='top', fill='y', anchor='n')


Label(row0, text="Audiobook", font='none 50', fg='brown', bg=bg).pack(pady=10)

image = Image.open('Audiobook.png')
imageResized = image.resize((200, 200), Image.ANTIALIAS)
imageg1 = ImageTk.PhotoImage(imageResized)

logo = Label(row1, image=imageg1,)
logo.pack()


title = Label(row2, text='Where books meet people',
              fg='brown', bg=bg, font='none 40')
title.pack()


path = None


def click():
    global path
    path = filedialog.askopenfilename()
    print(path)


def talk():
    page_n = page_number_box.get()
    if page_n:
        pass
    else:
        page_n = 0
    if path:
        speaker = pyttsx3.init('sapi5')
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)

        # open the pdf
        book = open(path, 'rb')

        # read the pdf
        read_file = PyPDF2.PdfReader(book)

        # chososing the page that we want to read
        page = read_file._get_page(int(page_n))

        # extract text from the page
        story_text = page.extract_text()

        speaker.say(story_text)
        speaker.runAndWait()

    else:
        Label(row9, text="Please Select Book",
              font='none, 20', bg='#f4a967').pack(pady=20)


def readPdf():
    page_n = page_number_box.get()
    if page_n:
        pass
    else:
        page_n = 0

    if path:
        location = path
        top = Toplevel()
        top.title("PDF")
        top.geometry("500x1000")
        top.configure(bg=bg)
        v1 = pdf.ShowPdf()

        # Adding pdf location and width and height.
        v2 = v1.pdf_view(top, pdf_location=open(location, 'r'))

        # Placing Pdf in my gui.
        v2.pack()
        top.mainloop()
    else:
        Label(row8, text="Please Select Book",
              font='none, 20', bg='#f4a967').pack(pady=20)


# open pdf button
open_PDF = Button(row3, text='Open', font='none 10', width=20, command=click)
open_PDF.pack(pady=(50, 0))

# pdf reading button
say_PDF = Button(row4, text="Listen", font='none 10', width=20, command=talk)
say_PDF.pack(pady=(20, 0))

# want to read also ??
read = Button(row5, text="Read",
              font='none 10', width=20, command=readPdf)
read.pack(pady=(20, 0))

page_number = Label(row6, text="Enter Page Number :",
                    bg=bg, font='none 15')
page_number.pack(side='left', pady=20, padx=0)

page_number_box = Entry(row6, bg='white', width=20)
page_number_box.pack(side='right', pady=20, padx=10)

# exit button
exit = Button(row7, text="Exit", font='none 10', width=20, command=app.destroy)
exit.pack(pady=(10, 0))


app.mainloop()
