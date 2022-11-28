from tkinter import *


def miles_converter():
    miles = float(m_input.get())
    km = miles * 2
    print(km)
    mi_label.config(text=f"{miles} mi =")
    km_label.config(text=f"{km} km")


window = Tk()
window.title("Mile to Km. Converter",)
window.minsize(width=220, height=220)
window.config(padx=11, pady=11, bg="white")

m_input = Entry(width=8)
m_input.grid(column=1, row=0)

miles_label = Label(text="", padx=11, pady=11, bg="white")
miles_label.grid(column=0, row=0)

miles_label = Label(text="Miles", fg="violet", padx=11, pady=11, bg="white", font=("Courier", 11, "bold"))
miles_label.grid(column=2, row=0)

mi_label = Label(text="___ mi =", fg="violet", padx=11, pady=11, bg="white", font=("Courier", 11, "bold"))
mi_label.grid(column=0, row=2)

km_label = Label(text=" ___ km", fg="violet",padx=11, pady=11, bg="white", font=("Courier", 11, "bold"))
km_label.grid(column=1, row=2)

input_btn = Button(text="Calculate", fg="violet", padx=11, pady=11, bg="white", command=miles_converter)
input_btn.grid(column=1, row=3)


window.mainloop()
