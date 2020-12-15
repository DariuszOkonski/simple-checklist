import tkinter

root = tkinter.Tk()
root.title('Simple Checklist')
root.iconbitmap('check.ico')
root.geometry('400x400')
root.resizable(0, 0)

# define fonts and colors
my_font = ('Arial', 12)
root_color = '#6c1cbc'
button_color = '#e2cff4'
root.config(bg=root_color)

# define functions

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
list_add_button = tkinter.Button(input_frame, text='Add Item', borderwidth=2, font=my_font, bg=button_color)

list_entry.grid(row=0, column=0)
list_add_button.grid(row=0, column=1)










root.mainloop()