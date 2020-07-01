from tkinter import *
from tkinter import font
from joblib import load
win = Tk()
win.title('Sentiment Analysis Vietnamese')

clf = load('LR_model.joblib')
vectorizer = load('TFIDFVEC.joblib')
#function
def convert():
    text = [textentry.get()]
    vecd = vectorizer.transform(text)
    text1.delete('0.0',END)
    if clf.predict(vecd)[0] == 0:
        text1.insert(END,'Negative.\n')
    else:
        text1.insert(END,'Positive.\n')
    text1.insert(END,'Probability: '+str(clf.predict_proba(vecd)[0][clf.predict(vecd)[0]]))

customFont = font.Font(family='Helvetica', size=13)
#create Labels
Label(win, text = "Put some words here:", font=customFont).grid(row = 1, column = 0, sticky = W)#
Label(win, text = "Cau noi co cam xuc", font=customFont).grid(row = 4, column = 0, sticky = W) 


#create Buttons
Button(win, text = 'Submit', command = convert, width = 6, font=customFont).grid(row = 3, column = 0, sticky = W)
Button(win, text = "Quit", command = win.quit, font=customFont).grid(row = 12, column = 0,padx = 5, pady = 5, sticky = W)

#create entry boxes
textentry = Entry(win, width = 80, bg = 'white', font=customFont)
textentry.grid(row = 2, column = 0, sticky = W)


#create text boxes
text1 = Text(win, width = 60, height = 2, wrap = WORD, background = "white", font=customFont)
text1.grid(row = 5, column = 0, columnspan = 2, sticky = W) #tich cuc tieu cuc

win.mainloop()
