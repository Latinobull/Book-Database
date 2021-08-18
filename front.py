from tkinter import *
import back


def viewCommand():
    LB.delete(0, END)
    for row in back.view():
        LB.insert(END, row)


def searchCommand():
    LB.delete(0, END)
    try:

        for row in back.search(
            Title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get()
        ):
            LB.insert(END, row)
    except UnboundLocalError:
        nocontent = "You didn`t add any content in the search engine"
        LB.insert(END, nocontent)


def addCommand():
    back.insert(Title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    LB.delete(0, END)
    LB.insert(
        END, (Title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    )
    Title_Entry.delete(0, END)
    Author_Entry.delete(0, END)
    Year_Entry.delete(0, END)
    ISBN_Entry.delete(0, END)


def deleteCommand():
    back.delete(selectedTuple[0])
    LB.delete(0, END)
    for row in back.view():
        LB.insert(END, row)

    Title_Entry.delete(0, END)
    Author_Entry.delete(0, END)
    Year_Entry.delete(0, END)
    ISBN_Entry.delete(0, END)


def updateCommand():
    back.update(
        selectedTuple[0],
        Title_text.get(),
        Author_text.get(),
        Year_text.get(),
        ISBN_text.get(),
    )
    LB.delete(0, END)
    for row in back.view():
        LB.insert(END, row)

    Title_Entry.delete(0, END)
    Author_Entry.delete(0, END)
    Year_Entry.delete(0, END)
    ISBN_Entry.delete(0, END)


def closeCommand():
    window.destroy()


def getSelectedRow(event):
    global selectedTuple
    index = LB.curselection()[0]
    selectedTuple = LB.get(index)
    Title_Entry.delete(0, END)
    Title_Entry.insert(END, selectedTuple[1])
    Author_Entry.delete(0, END)
    Author_Entry.insert(END, selectedTuple[2])
    Year_Entry.delete(0, END)
    Year_Entry.insert(END, selectedTuple[3])
    ISBN_Entry.delete(0, END)
    ISBN_Entry.insert(END, selectedTuple[4])


window = Tk()

window.wm_title("Bookstore")

TitleL = Label(window, text="Title")
TitleL.grid(row=0, column=0)

AuthorL = Label(window, text="Author")
AuthorL.grid(row=0, column=2)

YearL = Label(window, text="Year")
YearL.grid(row=1, column=0)

ISBNL = Label(window, text="ISBN")
ISBNL.grid(row=1, column=2)

Title_text = StringVar()
Title_Entry = Entry(window, textvariable=Title_text)
Title_Entry.grid(row=0, column=1)

Author_text = StringVar()
Author_Entry = Entry(window, textvariable=Author_text)
Author_Entry.grid(row=0, column=3)

Year_text = StringVar()
Year_Entry = Entry(window, textvariable=Year_text)
Year_Entry.grid(row=1, column=1)

ISBN_text = StringVar()
ISBN_Entry = Entry(window, textvariable=ISBN_text)
ISBN_Entry.grid(row=1, column=3)

LB = Listbox(window, height=6, width=35)
LB.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
LB.configure(yscrollcommand=sb1.set)
sb1.configure(command=LB.yview)

sb2 = Scrollbar(window, orient="horizontal")
sb2.grid(row=7, column=0, columnspan=2)
LB.configure(xscrollcommand=sb2.set)
sb2.configure(command=LB.xview)

LB.bind("<<ListboxSelect>>", getSelectedRow)

b1 = Button(window, text="View All", width=12, command=viewCommand)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=searchCommand)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=addCommand)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=updateCommand)
b4.grid(row=5, column=3)


b5 = Button(window, text="Delete", width=12, command=deleteCommand)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=closeCommand)
b6.grid(row=7, column=3)

window.mainloop()
