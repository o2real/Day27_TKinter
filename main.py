from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=f"{new_text} Button got clicked")

button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
print(input.get())






window.mainloop()