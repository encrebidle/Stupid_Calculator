from tkinter import *
import random

root =Tk()
root.title("Stupid Calculator")
#Your name
quotes=["Common sense is calculation applied to life.","We are more often\n treacherous through weakness than through calculation."
        "Dear Math, please grow up and solve your own problems, I'm tired\n of solving them for you.",
        "Math is fun, it teaches you life and death information, like when\n you're cold, you should go to a corner since it's 90 degrees there.",
        "If I had just one hour left to live, I'd spend it in Math class...\n it never ends.",
        "4 out 3 people struggle with math.",
        "Think of a number between 1 and 10. Multiply it by 9 and subtract\n 1. Now close your eyes. It's dark isn't it?"
        ,"I stopped understanding math when the alphabet decided to get\n involved.",
        "To the guy who created imaginary numbers in Math: I hate you.",
        "Finding a Job is like working on algebra equations, all you have\n to do is find the X.",
        "It's easy to identify people who can't count to ten. They're in\n front of you in the supermarket.",
        "Some of the greatest ideas of all time have come to people during\n Math class... none of which had anything to do with Math."
        
         
        ]
e=Entry(root,width =40,borderwidth=2)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#your input
sol=Entry(root,width =40,borderwidth=5)
sol.grid(row=1,column=0,columnspan=3,padx=10,pady=10)

mylabel= Label(root,text=random.choice(quotes),padx=30,pady=40, relief=GROOVE)#.grid(row=0,column=0)
mylabel1= Label(root,text="This is developed by Kumar Atulya(PSYCHO).\n This calculator is simple,stupid and lazy.",padx=40,pady=20)#


def button_click(number):
    #e.delete(0,END)
    e.insert(0,number)
def button_clear():
    e.delete(0,END)
    
def button_add():
    first_number=e.get()
    global f_num
    f_num= first_number +"+"
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global f_num
    f_num= first_number +"-"
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global f_num
    f_num= first_number +"*"
    e.delete(0,END)
def button_div():
    first_number=e.get()
    global f_num
    f_num= first_number +"/"
    e.delete(0,END)

def button_equal():
    second_number= e.get()
    e.delete(0,END)
    sol.insert(0,f_num+second_number)
    
#define Buttons
button_1= Button(root,text="1",padx=60,pady=20,command =lambda : button_click(1) )
button_2= Button(root,text="2",padx=60,pady=20,command =lambda :  button_click(2))
button_3= Button(root,text="3",padx=60,pady=20,command =lambda :  button_click(3))
button_4= Button(root,text="4",padx=60,pady=20,command =lambda :  button_click(4))
button_5= Button(root,text="5",padx=60,pady=20,command =lambda :  button_click(5))
button_6= Button(root,text="6",padx=60,pady=20,command =lambda :  button_click(6))
button_7= Button(root,text="7",padx=60,pady=20,command =lambda : button_click(7))
button_8= Button(root,text="8",padx=60,pady=20,command =lambda : button_click(8))
button_9= Button(root,text="9",padx=60,pady=20,command =lambda :  button_click(9))
button_0= Button(root,text="0",padx=60,pady=20,command =lambda : button_click(0))

button_ad= Button(root,text="+",padx=60,pady=20,command = button_add)
button_sub= Button(root,text="-",padx=60,pady=20,command =button_sub)
button_mul= Button(root,text="*",padx=60,pady=20,command =button_mul)
button_div= Button(root,text="/",padx=60,pady=20,command =button_div)

button_equal= Button(root,text="=",padx=120,pady=20,command =button_equal)
button_clear= Button(root,text="Clear",padx=120,pady=20,command =button_clear)


#
#put the buttons on the screen
button_1.grid(row=4, column=1)
button_9.grid(row=4, column=0)
button_7.grid(row=4, column=2)

button_3.grid(row=3, column=2)
button_4.grid(row=3, column=0)
button_6.grid(row=3, column=1)

button_8.grid(row=5, column=1)
button_5.grid(row=5, column=2)
button_0.grid(row=5, column=0)

button_2.grid(row=6, column=0)

button_ad.grid(row=7, column=0)
button_sub.grid(row=8, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_equal.grid(row=7, column=1,columnspan=2)
button_clear.grid(row=8, column=1,columnspan=2)

mylabel1.grid(row=10, column=0,columnspan=3)
mylabel.grid(row=11, column=0,columnspan=4)
root.mainloop()

