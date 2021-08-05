from tkinter import *
import back

window = Tk()

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

b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
