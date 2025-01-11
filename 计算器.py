from tkinter import *
import math


root = Tk()
root.geometry("295x280+150+150")
root.title('计算器')
root.attributes("-alpha",0.9)
root["background"]="#ffffff"

font=('宋体',20)
font_16=('宋体',16)
result_num=StringVar()
result_num.set('')
Label(root,textvariable=result_num,width=20,justify=LEFT,anchor=SE,font=font,height=2).grid(row=1,column=1,columnspan=4)

button_clear=Button(root,text='C',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')
button_back=Button(root,text='<',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')
button_division=Button(root,text='/',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')
button_multiplication=Button(root,text='*',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')
button_square=Button(root,text='√',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')

button_clear.grid(row=2,column=1,padx=4,pady=2)
button_back.grid(row=2,column=2,padx=4,pady=2)
button_division.grid(row=2,column=3,padx=4,pady=2)
button_multiplication.grid(row=2,column=4,padx=4,pady=2)
button_square.grid(row=5,column=4,padx=4,pady=2)


button_seven=Button(root,text='7',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_eight=Button(root,text='8',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_nine=Button(root,text='9',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_subtraction=Button(root,text='-',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')

button_seven.grid(row=3,column=1,padx=4,pady=2)
button_eight.grid(row=3,column=2,padx=4,pady=2)
button_nine.grid(row=3,column=3,padx=4,pady=2)
button_subtraction.grid(row=3,column=4,padx=4,pady=2)

button_four=Button(root,text='4',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_five=Button(root,text='5',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_six=Button(root,text='6',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_add=Button(root,text='+',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')

button_four.grid(row=4,column=1,padx=4,pady=2)
button_five.grid(row=4,column=2,padx=4,pady=2)
button_six.grid(row=4,column=3,padx=4,pady=2)
button_add.grid(row=4,column=4,padx=4,pady=2)

button_one=Button(root,text='1',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_two=Button(root,text='2',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_three=Button(root,text='3',width=5,font=font_16,relief=FLAT,bg='#eacda1')
button_equal=Button(root,text='=',width=5,font=font_16,relief=FLAT,bg='#b1b2b2')

button_one.grid(row=5,column=1,padx=4,pady=2)
button_two.grid(row=5,column=2,padx=4,pady=2)
button_three.grid(row=5,column=3,padx=4,pady=2)
button_equal.grid(row=6,column=4,padx=4,pady=2)

button_zero=Button(root,text='0',width=12,font=font_16,relief=FLAT,bg='#eacda1')
button_dot=Button(root,text='.',width=5,font=font_16,relief=FLAT,bg='#eacda1')

button_zero.grid(row=6,column=1,padx=4,pady=2,columnspan=2)
button_dot.grid(row=6,column=3,padx=4,pady=2)




def click_button(x):
    result_num.set(result_num.get()+x)
def calculation():
    opt_str=result_num.get()
    result=eval(opt_str)
    result_num.set(str(result))
def back():
    str1=result_num.get()
    n=len(str1)
    result_num.set(str1[:n-1])
def clear():
    result_num.set('')
def square():
    result_num.set(math.sqrt(float(result_num.get())))
    
button_one.config(command=lambda:click_button('1'))
button_two.config(command=lambda:click_button('2'))
button_three.config(command=lambda:click_button('3'))
button_four.config(command=lambda:click_button('4'))
button_five.config(command=lambda:click_button('5'))
button_six.config(command=lambda:click_button('6'))
button_seven.config(command=lambda:click_button('7'))
button_eight.config(command=lambda:click_button('8'))
button_nine.config(command=lambda:click_button('9'))
button_zero.config(command=lambda:click_button('0'))
button_add.config(command=lambda:click_button('+'))
button_subtraction.config(command=lambda:click_button('-'))
button_multiplication.config(command=lambda:click_button('*'))
button_division.config(command=lambda:click_button('/'))
button_dot.config(command=lambda:click_button('.'))

button_equal.config(command=calculation)
button_back.config(command=back)
button_clear.config(command=clear)
button_square.config(command=square)
root.mainloop()
