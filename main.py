import tkinter
from tkinter import END

root = tkinter.Tk()
root.title('Simple Checklist')
root.iconbitmap('check.ico')
root.geometry('400x400')
root.resizable(0, 0)

# define fonts and colors
my_font = ('Arial', 11)
root_color = '#6c1cbc'
button_color = '#e2cff4'
root.config(bg=root_color)

# define functions
def add_item():
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)

# define layout
# create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

# input frame layout ============================
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font)
list_add_button = tkinter.Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color, command=add_item)

list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

# output frame layout ===========================
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=17, width=45, borderwidth=3, font=my_font)

my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

# button frame layout ===========================
list_remove_button = tkinter.Button(button_frame, text="Remove Item", borderwidth=2, font=my_font, bg=button_color)
list_clear_button = tkinter.Button(button_frame, text="Clear List", borderwidth=2, font=my_font, bg=button_color)
save_button = tkinter.Button(button_frame, text="Save List", borderwidth=2, font=my_font, bg=button_color)
quit_button = tkinter.Button(button_frame, text="Quit", borderwidth=2, font=my_font, bg=button_color, command=root.destroy)

list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)







root.mainloop()