from tkinter import *

# import the msgbox
from tkinter import messagebox

# Import the DB class
from db import Database
db = Database("store.db")

# create window object
app = Tk()

# functions section
selected_item = None

def populate_list():
    part_list.delete(0, END)
    for row in db.fetch():
        part_list.insert(END, row)


def add_item():
    # validate that the fields aren't empty
    if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror("Required Fields", "Please include all fields")
        return
    # call the insert method on the db class
    db.insert(part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    # clear the list box
    part_list.delete(0, END)
    # add items to the list box
    part_list.insert(END, (part_text.get(), customer_text.get(),
                           retailer_text.get(), price_text.get()))
    clear_text()
    # populate the list
    populate_list()

def select_item(event):
    # create a global variable to be used by other functions
    global selected_item
    # get the index
    index = part_list.curselection()[0]
    selected_item = part_list.get(index)
    # clear the text boxes
    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retailer_entry.delete(0, END)
    retailer_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])




def remove_item():
    db.delete(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0],part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)
    


# Title
app.title("Part Manager")

# Size
app.geometry("700x350")

# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
# Place the label on the 'grid'
part_label.grid(row=0, column=0, sticky=W)
# Part entry
part_entry = Entry(app, textvariable=part_text)
# part_entry.insert(0,"placeholder")
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
# Place the label on the 'grid'
customer_label.grid(row=0, column=2, sticky=W)
# Customer entry
customer_entry = Entry(app, textvariable=customer_text)
# customer_entry.insert(0,"placeholder")
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
# Place the label on the 'grid'
retailer_label.grid(row=1, column=0, sticky=W)
# Retailer entry
retailer_entry = Entry(app, textvariable=retailer_text)
# retailer_entry.insert(0,"placeholder")
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
# Place the label on the 'grid'
price_label.grid(row=1, column=2, sticky=W)
# Price entry
price_entry = Entry(app, textvariable=price_text)
# price_entry.insert(0,"placeholder")
price_entry.grid(row=1, column=3)


# Parts list(listbox widget)
part_list = Listbox(app, height=8, width=50)  # , border =0)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# create the scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# stick/attach to the scrollbar
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)
# bind select
part_list.bind("<<ListboxSelect>>", select_item)


# Buttons Section
# Add button
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)
# Remove button
remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)
# Update button
update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2)
# Clear button
clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Populate the parts list when we open the app
populate_list()

# Start the program
app.mainloop()
