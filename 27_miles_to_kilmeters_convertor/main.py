import tkinter


def on_calculate_click():
    miles = float(input_miles.get())
    km = round(miles * 1.60934, 2)
    value_km['text'] = km


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
label_equal.grid(column=0, row=1)

value_km = tkinter.Label(text="0", font=("Arial", 14, "normal"))
value_km.grid(column=1, row=1)

label_km = tkinter.Label(text="Km", font=("Arial", 14, "normal"))
label_km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=on_calculate_click)
button.grid(column=1, row=2)

window.mainloop()
