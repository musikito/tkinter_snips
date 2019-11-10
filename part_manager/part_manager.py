from tkinter import *

# create window object
app = Tk()

# change the title
app.title("Part Manager")

# Size
app.geometry("700x350")

part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold',14), pady=20)
# Place the label on the 'grid'
part_label.grid(row=0, column=0, sticky =W)
# Part entry
part_entry = Entry(app, textvariable=part_text)
# part_entry.insert(0,"placeholder")
part_entry.grid(row=0,column=1)

# Start the program
app.mainloop()