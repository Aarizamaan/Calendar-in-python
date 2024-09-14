import tkinter as tk
import calendar
from PIL import Image, ImageTk

win = tk.Tk()
win.title("GUI Calendar")

# Create a frame to hold all widgets
frame = tk.Frame(win)
frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')



# Load the background image
background_image = Image.open("bg.jpg")  # Replace with your background image
background_image = ImageTk.PhotoImage(background_image)

# Create a frame to hold all widgets
frame = tk.Frame(win)
frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Create a label to display the background image
background_label = tk.Label(frame, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def display_calendar():
    year_str = year.get()
    month_str = month.get()
    year_int = int(year_str)
    month_int = int(month_str)
    cal = calendar.month(year_int, month_int)
    textfield.delete(1.0, tk.END)
    textfield.insert(tk.INSERT, cal)




##icon loading
goicon_image = Image.open("goIcon.png")  # Assuming you have the goIcon.png image in the same folder
Go_icon = ImageTk.PhotoImage(goicon_image)
yearicon_image = Image.open("calendar.png")
year_icon= ImageTk.PhotoImage(yearicon_image)
monthicon_image = Image.open("month (1).png")
month_icon= ImageTk.PhotoImage(monthicon_image)


label1 = tk.Label(frame, image=year_icon)
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = tk.Label(frame,image=month_icon)
label2.grid(row=0, column=1, padx=10, pady=10)

year = tk.Spinbox(frame, from_=1947, to=2150, width=24)
year.grid(row=1, column=0, padx=10, sticky='ew')
frame.grid_columnconfigure(0, weight=1)

month = tk.Spinbox(frame, from_=1, to=12, width=3)
month.grid(row=1, column=1, padx=10, sticky='ew')
frame.grid_columnconfigure(1, weight=1)

button = tk.Button(frame, image=Go_icon, command=display_calendar)
button.grid(row=1, column=2, padx=10)

textfield = tk.Text(frame, height=10, width=30, foreground='black',font=("Courier", 24,'bold'))
textfield.grid(row=3, column=0, columnspan=3, padx=100, pady=50, sticky='nsew')
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Make the frame expand to fill the window
win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)

win.mainloop()