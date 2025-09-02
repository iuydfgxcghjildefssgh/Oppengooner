import tkinter as tk
from bs4 import BeautifulSoup
import requests

def on_enter_btn_clicked():
    url = URL_Input.get()   # get user input here
    requestURL(url)         # pass it into requestURL()
    SoupUse(soup)

def requestURL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def SoupUse(soup):
    images = soup.find_all('gallery_thumb')


# Tkinter setup
window = tk.Tk()
window.geometry("1000x600")

Frame1 = tk.Frame(window)
Frame2 = tk.Frame(window)

Insert_URL = tk.Label(master=Frame1, text="Insert URL")
Insert_URL.pack()

URL_Input = tk.Entry(master=Frame2, fg="white", bg="black", width=70)
URL_Input.pack()

enter_btn = tk.Button(master=Frame2, text="Enter", command=on_enter_btn_clicked)
enter_btn.pack()

Frame1.pack()
Frame2.pack()

window.mainloop()
