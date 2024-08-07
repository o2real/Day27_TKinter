from tkinter import *


def button_clicked():
    miles = float(input.get())
    print("Calculate")
    km = round(miles * 1.609, 2)
    my_label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=0)

my_label_equal = Label(text="is equal", font=("Arial", 24, "bold"))
my_label_equal.grid(column=0, row=1)

my_label_result = Label(text="0", font=("Arial", 24))
my_label_result.grid(column=1, row=1)

my_label_km = Label(text="Km", font=("Arial", 24, "bold"))
my_label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
