import tkinter as tk
from functools import partial



def call_result(label_result, n1, n2,n3,n4,n5,n6,n9,n10,n11,n12,n13,n14):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    num4 = (n4.get())
    num5 = (n5.get())
    num6 = (n6.get())
    num9 = (n9.get())
    num10 = (n10.get())
    num11 = (n11.get())
    num12 = (n12.get())
    num13 = (n13.get())
    num14 = (n14.get())

    result = int(num2)+int(num3)+int(num4)+int(num5)+int(num6)+int(num9)+int(num10)+int(num11)+int(num12)+int(num13)
    result=result+result*0.17
    label_result.config(text="Result = %d" % result,font=('arial',16,'bold'),bd=10,bg="powder blue",width=18)
    return




def bill(lr1,lr2,lr3,lr4,lr5,lr6,lr9,lr10,lr11,lr12,lr13,lr14,lr15,n1,n2,n3,n4,n5,n6,n9,n10,n11,n12,n13,n14,n15):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    num4 = (n4.get())
    num5 = (n5.get())
    num6 = (n6.get())
    num9 = (n9.get())
    num10 = (n10.get())
    num11 = (n11.get())
    num12 = (n12.get())
    num13 = (n13.get())
    num14 = (n14.get())

    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    num4=int(num4)
    num5=int(num5)
    num6=int(num6)
    num9 = int(num9)
    num10 = int(num10)
    num11 = int(num11)
    num12 = int(num12)
    num13 = int(num13)
    num14 = int(num14)
    num15 = num2+num3+num4+num5+num6+num9+num10+num11+num12+num13
    num15=int(num15+num15*0.17)


    lr1.config(text="ORDER NO = %d" % num1,font=('arial',12,'bold'),bd=10,bg="white",width=20)
    lr2.config(text="SAMOSA = %d" % num2,font=('arial',12,'bold'),bd=10,bg="white",width=20)
    lr3.config(text="DOSA ITEM = %d" % num3,font=('arial',12,'bold'),bd=10,bg="white",width=20)
    lr4.config(text="SANDWICH = %d" % num4,font=('arial',12,'bold'),bd=10,bg="white",width=20)
    lr5.config(text="LUNCH = %d" % num5,font=('arial',12,'bold'),bd=10,bg="white",width=20)
    lr6.config(text="IDLI = %d" % num6,font=('arial',12,'bold'),bd=10,bg="white",width=20)

    lr9.config(text="SCHEZWAN RICE = %d" % num9, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr10.config(text="SCHEZWAN NOODLES = %d" % num10, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr11.config(text="FRIED RICE = %d" % num11, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr12.config(text="IDLI CHILLY = %d" % num12, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr13.config(text="COLD DRINK = %d" % num13, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr14.config(text="GST = %d" % num14, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)
    lr15.config(text="TOTAL = %d" % num15, font=('arial', 12, 'bold'), bd=10, bg="white", width=20)


    
    return


def reset(labelResult, n1, n2,n3,n4,n5,n6,n9,n10,n11,n12,n13,n14,n15,lr1,lr2,lr3,lr4,lr5,lr6,lr9,lr10,lr11,lr12,lr13,lr14,lr15):
    n1.set(0)
    n2.set(0)
    n3.set(0)
    n4.set(0)
    n5.set(0)
    n6.set(0)

    n9.set(0)
    n10.set(0)
    n11.set(0)
    n12.set(0)
    n13.set(0)
    n14.set(17)
    n15.set(0)
    result=0
    res=17
    labelResult.config(text="%d" % result)
    lr1.config(text="%d" % result)
    lr2.config(text="%d" % result)
    lr3.config(text="%d" % result)
    lr4.config(text="%d" % result)
    lr5.config(text="%d" % result)
    lr6.config(text="%d" % result)
    lr9.config(text="%d" % result)
    lr10.config(text="%d" % result)
    lr11.config(text="%d" % result)
    lr12.config(text="%d" % result)
    lr13.config(text="%d" % result)
    lr14.config(text="%d" % res)
    lr15.config(text="%d" % result)


    return

root = tk.Tk()
root.geometry('400x200')

root.title('RESTAURANT BILLING SYSTEM')

#heading = tk.Label(root, text="BILLS",bg="DarkOrange2").grid(row=0, column=4)
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.StringVar()
number6 = tk.StringVar()


number9 = tk.StringVar()
number10 = tk.StringVar()
number11 = tk.StringVar()
number12 = tk.StringVar()
number13 = tk.StringVar()
number14 = tk.StringVar()
number15=tk.StringVar()


heading1=   tk.Label(root, text="FOOD ITEM",font=('arial',16,'bold'),anchor='w').grid(row=0,column=1)
labelNum1 = tk.Label(root, text="ORDER No.",font=('arial',16,'bold'),anchor='w').grid(row=1, column=1)
labelNum2 = tk.Label(root, text="SAMOSA",font=('arial',16,'bold'),anchor='w').grid(row=2, column=1)
labelNum3 = tk.Label(root, text="DOSA ITEM",font=('arial',16,'bold'),anchor='w').grid(row=3, column=1)
labelNum4 = tk.Label(root, text="SANDWICH",font=('arial',16,'bold'),anchor='w').grid(row=4, column=1)
labelNum5 = tk.Label(root, text="LUNCH",font=('arial',16,'bold'),anchor='w').grid(row=5, column=1)
labelNum6 = tk.Label(root, text="IDLI",font=('arial',16,'bold'),anchor='w').grid(row=6, column=1)


heading3=   tk.Label(root, text="FOOD ITEM",font=('arial',16,'bold'),anchor='w').grid(row=0,column=4)
labelNum9 = tk.Label(root, text="SCHEZWAN RICE",font=('arial',16,'bold'),anchor='w').grid(row=1, column=4)
labelNum10= tk.Label(root, text="SCHEZWAN NOODLES",font=('arial',16,'bold'),anchor='w').grid(row=2, column=4)
labelNum11 = tk.Label(root, text="FRIED RICE",font=('arial',16,'bold'),anchor='w').grid(row=3, column=4)
labelNum12= tk.Label(root, text="IDLI CHILLY",font=('arial',16,'bold'),anchor='w').grid(row=4, column=4)
labelNum13= tk.Label(root, text="COLD DRINK",font=('arial',16,'bold'),anchor='w').grid(row=5, column=4)
labelNum14= tk.Label(root, text="%GST",font=('arial',16,'bold'),anchor='w').grid(row=6, column=4)



labelResult = tk.Label(root,font=('arial',12,'bold'))
labelResult.grid(row=10, column=2)


heading2=   tk.Label(root,font=('arial',16,'bold'),anchor='w').grid(row=0,column=2)
entryNum1 = tk.Entry(root, textvariable=number1,font=('arial',16,'bold'),bd=10,insertwidth=4,bg="lawn green",justify='right').grid(row=1, column=2)
number1.initialize(0)
entryNum2 = tk.Entry(root, textvariable=number2,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=2, column=2)
number2.initialize(0)
entryNum3 = tk.Entry(root, textvariable=number3,font=('arial',16,'bold'), bd=10,insertwidth=4
                ,bg="lawn green",justify='right').grid(row=3, column=2)
number3.initialize(0)
entryNum4 = tk.Entry(root, textvariable=number4,font=('arial',16,'bold'), bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=4, column=2)
number4.initialize(0)
entryNum5 = tk.Entry(root, textvariable=number5,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="lawn green",justify='right').grid(row=5, column=2)
number5.initialize(0)
entryNum6 = tk.Entry(root, textvariable=number6,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=6, column=2)
number6.initialize(0)


heading4=   tk.Label(root,font=('arial',16,'bold'),anchor='w').grid(row=0,column=5)
entryNum9 = tk.Entry(root, textvariable=number9,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="lawn green",justify='right').grid(row=1, column=5)
number9.initialize(0)
entryNum10 = tk.Entry(root, textvariable=number10,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=2, column=5)
number10.initialize(0)
entryNum11= tk.Entry(root, textvariable=number11,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="lawn green",justify='right').grid(row=3, column=5)
number11.initialize(0)
entryNum12 = tk.Entry(root, textvariable=number12,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=4, column=5)
number12.initialize(0)
entryNum13= tk.Entry(root, textvariable=number13,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="lawn green",justify='right').grid(row=5, column=5)
number13.initialize(0)
entryNum14= tk.Entry(root, textvariable=number14,font=('arial',16,'bold'),bd=10,insertwidth=4
                ,bg="yellow",justify='right').grid(row=6, column=5)
number14.initialize(17)


call_result= partial(call_result, labelResult, number1, number2,number3,number4,number5,number6,number9,number10,number11,number12,number13,number14)

buttonCal = tk.Button(root, text="Calculate", command=call_result,activebackground='powder blue',font=('arial',16,'bold'),bd=10,bg="cyan2",width=10).grid(row=10, column=0)





lr1 = tk.Label(root)
lr1.grid(row=19, column=1)
lr2 = tk.Label(root)
lr2.grid(row=20, column=1)
lr3 = tk.Label(root)
lr3.grid(row=21, column=1)
lr4 = tk.Label(root)
lr4.grid(row=22, column=1)
lr5 = tk.Label(root)
lr5.grid(row=23, column=1)
lr6 = tk.Label(root)
lr6.grid(row=24, column=1)

lr9 = tk.Label(root)
lr9.grid(row=19, column=2)
lr10 = tk.Label(root)
lr10.grid(row=20, column=2)
lr11= tk.Label(root)
lr11.grid(row=21, column=2)
lr12 = tk.Label(root)
lr12.grid(row=22, column=2)
lr13= tk.Label(root)
lr13.grid(row=23, column=2)
lr14= tk.Label(root)
lr14.grid(row=24, column=2)
lr15= tk.Label(root)
lr15.grid(row=25, column=2)
bill= partial(bill, lr1,lr2,lr3,lr4,lr5,lr6,lr9,lr10,lr11,lr12,lr13,lr14,lr15,number1,number2,number3,number4,number5,number6,number9,number10,number11,number12,
              number13,number14,number15)

bC = tk.Button(root, text="bill", command=bill,activebackground='powder blue',font=('arial',16,'bold'),bd=10,bg="cyan2",width=10).grid(row=17,column=0)


reset = partial(reset, labelResult, number1, number2,number3,number4,number5,number6,number9,number10,number11,number12,number13,number14,number15,lr1,lr2,lr3,lr4,lr5,lr6,lr9,lr10,lr11,lr12,lr13,lr14,lr15)

btnReset=tk.Button(root,text="Reset",command=reset,activebackground='powder blue',font=('arial',16,'bold'),bd=10,bg="cyan2",width=10).grid(row=13,column=0)

root.mainloop()
