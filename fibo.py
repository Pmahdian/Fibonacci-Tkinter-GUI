#!/usr/bin/env python
# coding: utf-8

# ### 📌 Importing Required Libraries for GUI Development
# 
# 

# In[21]:


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from fibo_utils import generate_fibonacci

# ### 🖥️ Initializing the Main Window
# 

# In[22]:


root = Tk()
root.config(bg='#B3C8CF')
root.title('Fibonacci')


# ### 📌 Setting Window Size and Position in Tkinter

# In[23]:


rootw = 720
rooth = 340
screenw = (root.winfo_screenwidth()//2) - (rootw//2)
screenh = (root.winfo_screenheight()//2) - (rooth//2)
root.geometry("{}x{}+{}+{}".format(rootw,rooth,screenw,screenh))
root.minsize(400,200)
root.maxsize(1200,800)


# ### 🔳 Frame Layout and Styling in Tkinter
# 
# This section creates two frames, placing one on the left and the other on the right.  
# For the right frame, a border and background color have been set to enhance the UI appearance.
# 

# In[24]:


f1=Frame(root)
f2=Frame(root)
f1.pack(side='left')
f2.pack(side='right',padx=10)
f2.config(bd=2,bg='#B3C8CF')


# ### 🖼️ Loading and Resizing an Image with PIL  

# In[25]:


from PIL import ImageTk, Image

img = Image.open('R.eb38060a0e660040d3b7b421fe1de5c4.jpeg')
img = img.resize((250, 290))
img = ImageTk.PhotoImage(img)


# ### 🏷️ Displaying the Image in a Label 

# In[26]:


panel = Label(f2, image=img,bd=10)

panel.pack(padx=20,pady=10)


# ### 📖 Creating a Notebook with Tkinter  

# In[27]:


from tkinter import ttk 
from tkinter import *
nb = ttk.Notebook(root)
f_note1= Frame(nb,bd=0,bg='#F1EEDC')
f_note2=Frame(nb,bd= 0,bg='#F1EEDC')
f_note1.pack(fill= BOTH,expand=True)
f_note2.pack(fill = BOTH,expand=True)
nb.add(f_note1, text='about fibonacci')
nb.add(f_note2,text='fibonacci sequence')
nb.place(x=26,y=10)


# ### 🔢 Fibonacci Sequence Label
# 

# In[28]:


lab_note1 = Label(f_note1, text='The Fibonacci Sequence is infinitely \n large, but it begins like this:\n 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc. \n Each number is the sum of the \n two numbers that come before it. Also, \n when one number is divided \n by the one that comes right before it,\n the result gets closer \n and closer to the golden ratio.',fg='#000000')
lab_note1.pack(pady=50,padx=30)
lab_note1.config(bg='#F1EEDC')


# ### 📊 Fibonacci Sequence Calculator
# 
# This Python script uses **tkinter** to create a graphical user interface that calculates the Fibonacci sequence based on user input.

# In[29]:


import tkinter as tk
from tkinter import ttk

def fib(number):
    try:
        answer = generate_fibonacci(number)
        inv_lab.config(text=answer)
    except ValueError as e:
        inv_lab.config(text=str(e))
   
            
    # final_ans = tk.Label(f_note2, text=answer)
    # final_ans.pack()
    inv_lab.config(text=answer)

def clearing():
    inv_lab.config(text="")

sp_lab= Label(f_note2,text='')
sp_lab.pack(pady=16)
sp_lab.config(bg='#F1EEDC')

enter_lab = Label(f_note2,text='Pleas Enter s Number:')
enter_lab.pack()
enter_lab.config(bg='#F1EEDC')
# Create the input entry
x = Entry(f_note2,bg='old lace')
x.pack(pady=5,padx=5)

# Create the button to trigger Fibonacci calculation
btn = tk.Button(f_note2, bg= 'blue', text="Calculate", command=lambda: fib(int(x.get())))
btn.pack(padx=5,pady=5)
btn.config(fg='#51829B')

# Create the button to clear the error message
back_btn = tk.Button(f_note2, text="Clear", command=clearing)
back_btn.pack()
back_btn.config(fg='#51829B')
inv_lab = tk.Label(f_note2, text="")
inv_lab.pack()
inv_lab.config(bg='#F1EEDC')


# ## final step
# 

# In[ ]:


root.mainloop()

