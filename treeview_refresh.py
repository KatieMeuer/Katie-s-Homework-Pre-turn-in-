from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('Status Board')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

# scrollbars
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

# Create table frame
my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('Student_ID', 'Firstname', 'Lastname', 'GPA')

# Format columns
my_game.column("#0", width=0, stretch=NO)
my_game.column("Student_ID", anchor=CENTER, width=80)
my_game.column("Firstname", anchor=CENTER, width=80)
my_game.column("Lastname", anchor=CENTER, width=80)
my_game.column('GPA', anchor=CENTER, width=80)


# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("Student_ID", text="ID", anchor=CENTER)
my_game.heading("Firstname", text="Firstname", anchor=CENTER)
my_game.heading("Lastname", text="Lastname", anchor=CENTER)
my_game.heading('GPA', text='GPA', anchor=CENTER)

# Insert teams
my_game.insert(parent='', index='end', iid=0, text='',
               values=('1', 'Katie', 'Meuer', '3.89'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('2', 'Maggie', 'Landis', '4.00'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('3', 'Anna', 'Trksak', '4.00',))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('4', 'Sam', 'Spanier', '3.89'))
my_game.insert(parent='', index='end', iid=4, text='',
               values=('5', 'Peter', 'Andrew', '5.00'))
my_game.insert(parent='', index='end', iid=5, text='',
               values=('6', 'Elleanor', 'Koop', '4.00'))
my_game.insert(parent='', index='end', iid=6, text='',
               values=('7', 'Sarah', 'Koezly', '4.00'))
my_game.insert(parent='', index='end', iid=7, text='',
               values=('8', 'David', 'Kostik', '4.00'))
my_game.insert(parent='', index='end', iid=8, text='',
               values=('9', 'Grace', 'Brandt', '4.00'))
my_game.insert(parent='', index='end', iid=9, text='',
               values=('10', 'Tim', 'Klimish', '4.00'))
my_game.insert(parent='', index='end', iid=10, text='',
               values=('11', 'Jayda', 'Francis', '4.00'))
my_game.pack()

frame = Frame(ws)
frame.pack(pady=20)

# Labels
Student_ID = Label(frame, text="ID")
Student_ID.grid(row=0, column=0)

Firstname = Label(frame, text="Firstname")
Firstname.grid(row=0, column=1)

Lastname = Label(frame, text="Lastname")
Lastname.grid(row=0, column=2)

GPA = Label(frame, text='GPA')
GPA.grid(row=0, column=3)

# Entry boxes: ID, Name, Rank
Student_ID_entry = Entry(frame)
Student_ID_entry.grid(row=1, column=0)

Firstname_entry = Entry(frame)
Firstname_entry.grid(row=1, column=1)

Lastname_entry = Entry(frame)
Lastname_entry.grid(row=1, column=2)

GPA_entry = Entry(frame)
GPA_entry.grid(row=1, column=3)

# Select Record
def select_record():
    # clear entry boxes
    Student_ID_entry.delete(0, END)
    Firstname_entry.delete(0, END)
    Lastname_entry.delete(0, END)
    GPA_entry.delete(0, END)

    # Get row that has focus
    selected = my_game.focus()
    # grab record values
    values = my_game.item(selected, 'values')
    # temp_label.config(text=selected)

    # Insert focus row in entry boxes
    Student_ID_entry.insert(0, values[0])
    Firstname_entry.insert(0, values[1])
    Lastname_entry.insert(0, values[2])
    GPA_entry.insert(0, values[3])

# Update Record
def update_record():
    selected = my_game.focus()
    # save new data
    my_game.item(selected, text="", values=(Student_ID_entry.get(), Firstname_entry.get(), Lastname_entry.get(), GPA_entry.get()))

    # clear entry boxes
    Student_ID_entry.delete(0, END)
    Firstname_entry.delete(0, END)
    Lastname_entry.delete(0, END)
    GPA_entry.delete(0, END)

# Buttons
select_button = Button(ws, text="Select Record", command=select_record)
select_button.pack(pady=10)

refresh_button = Button(ws, text="Refresh Record", command=update_record)
refresh_button.pack(pady=10)

temp_label = Label(ws, text="")
temp_label.pack()

ws.mainloop()