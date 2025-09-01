import tkinter as tk

window = tk.Tk()
window.geometry("1000x600")


def on_enter_btn_clicked():
    Inputted_URL = URL_Input.get()
    print(Inputted_URL)

Frame1 = tk.Frame()
Frame2 = tk.Frame()

Insert_URL = tk.Label(master=Frame1, text="Insert URL")
Insert_URL.pack()
URL_Input = tk.Entry(master=Frame2, fg="White", bg="Black", width=70)
URL_Input.pack()
enter_btn = tk.Button(master=Frame2, text="Enter", command=on_enter_btn_clicked)
enter.pack()


Frame1.pack()
Frame2.pack()


window.mainloop()