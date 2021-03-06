# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:58:08 2021

@author: Aaron
"""


# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:43:42 2020

@author: lopezped
"""

import tkinter as tk
from PIL import ImageTk as itk
from PIL import Image

ventana=tk.Tk()
ventana.title("Mi primer ventana")
ventana.geometry("800x600")
ventana.configure(background="dark turquoise")

foto=itk.PhotoImage(file="d.png")
label = tk.Label(image=foto)
label.pack()

ventana.mainloop()
