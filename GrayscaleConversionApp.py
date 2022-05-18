# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:05:37 2021

@author: Mohamed Nowfal A
"""

from tkinter import *
from tkinter.filedialog import*
import cv2

root = Tk()
root.geometry('400x300')

l = Label(root, text="Grayscale Conversion, Upload the file", font=('Times New Roman',14,'bold'))
l.pack()

def buttonFunction():
    path = askopenfilename()
    global img
    img = cv2.imread(path, 0)

def buttonFunction2():
    cv2.imshow('Grayscale Conversion', img)
    
b = Button(root, text="Upload", command=buttonFunction, bg='#006666', fg='black', font=('Times New Roman',14,'bold','underline'))
b.pack(side=LEFT,ipady=10,ipadx=20,padx=20)


b2 = Button(root, text="Convert", command=buttonFunction2, bg='#006666', fg='black', font=('Times New Roman',14,'bold','underline'))
b2.pack(side=RIGHT,ipady=10,ipadx=20,padx=50)

root.mainloop()