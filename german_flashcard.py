# Visit Our facebook page: Uncle Engineer
# www.facebook.com/UncleEngineer
# www.uncle-engineer.com/python
# if error open cmd: pip install Pillow

from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import random
import time


    
def germandict():

    Voc = Toplevel()
    DE_EN = {'Katze':'katze.jpg',
             'Mann':'mann.jpg',
             'Ingenieur':'ingenieur.png'}
    voc, pic = random.choice(list(DE_EN.items()))

    image = Image.open(pic)
    photo = ImageTk.PhotoImage(image)

    label = Label(Voc,image=photo)
    label.image = photo 
    label.pack()

    translate = Label(Voc, text = voc)
    translate.config(font=("Courier", 44))
    translate.pack(ipady=20)
    Voc.mainloop()
        
if __name__=='__main__':
    
    GUI = Tk()
    GUI.title('German Flash Card by Uncle Engieer')
    GUI.geometry("400x200+30+30") 


    German = Label(GUI, text = "German Flash Card\n by Uncle Engineer")
    German.config(font=("tohama", 25))
    German.pack(padx=20,pady=20)

    B = ttk.Button(GUI, text ="Vocab", command = germandict)
    B.pack()

    GUI.mainloop()
