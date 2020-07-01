from tkinter import *
import sys
import re
win = Tk()
win.title('Sentiment Analysis Vietnamese')
#win.configure(background ="Black" )


#function
def inputFile():
    input_text = textentry.get()  

    text1.delete(0.0, END)



      


#create Labels
Label(win, text = "Put some words here:").grid(row = 1, column = 0, sticky = W)#
Label(win, text = "Cau noi co cam xuc").grid(row = 4, column = 0, sticky = W) 


#create Buttons
Button(win, text = 'Submit', command = inputFile, width = 6).grid(row = 3, column = 0, sticky = W)
Button(win, text = "Quit", command = win.quit).grid(row = 12, column = 0,padx = 5, pady = 5, sticky = W)

#create entry boxes
textentry = Entry(win, width = 80, bg = 'white')
textentry.grid(row = 2, column = 0, sticky = W)


#create text boxes
text1 = Text(win, width = 60, height = 2, wrap = WORD, background = "white")
text1.grid(row = 5, column = 0, columnspan = 2, sticky = W) #tich cuc tieu cuc



win.mainloop()