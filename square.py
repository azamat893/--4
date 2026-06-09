from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        number = float(entry.get())

        square = number ** 2
        cube = number ** 3

        result_label.config(
            text=f"Квадраты: {square}\nКубы: {cube}"
        )

    except ValueError:
        messagebox.showerror("Қате", "Сан енгізіңіз!")

window = Tk()
window.title("Санның квадратын және кубын есептеу")
window.geometry("300x200")

label = Label(window, text="Санды енгізіңіз:")
label.pack(pady=5)

entry = Entry(window, width=20)
entry.pack(pady=5)





button = Button(window, text="Есептеу", command=calculate)
button.pack(pady=10)

result_label = Label(window, text="Нәтиже:")
result_label.pack(pady=10)

window.mainloop()