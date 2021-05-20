from tkinter import *
import random
import time

master = Tk()
master.title("Tic-tac-toe")
master.configure(bg='white')


def chooser(n):
    lista = []
    if lis[n]["text"] != 'x' and lis[n]["text"] != 'o':
        lis[n]['text'] = 'x'
        c = 0
    else:
        label1["text"] = 'not valid'
        c = 1
    if winner(lis) == None:
        for i in range(len(lis)):
            if lis[i]["text"] != 'x' and lis[i]["text"] != 'o':
                lista.append(i)
        if len(lista) >= 8 and c == 0:
            lista = [0, 2, 6, 8]
            s = random.choice(lista)
            if lis[4]['text'] != 'x':
                lis[4]['text'] = 'o'
                c = 1
            elif lis[s]["text"] != 'x' and lis[s]["text"] != 'o':
                lis[s]['text'] = 'o'
                c = 1

        elif len(lista) >= 1 and c == 0:
            # s=random.choice(lista)
            for ite in lista:
                if c == 1:
                    break
                print(lista)
                temp = lis[ite]['text']
                print(temp)
                lis[ite]['text'] = 'o'
                if winner(lis) == 'o':
                    c = 1
                    print("o")
                    break
                else:
                    lis[ite]['text'] = temp
            for ite in lista:
                temp = lis[ite]['text']
                if c == 1:
                    break
                lis[ite]['text'] = 'x'
                if winner(lis) == 'x':
                    lis[ite]['text'] = 'o'
                    c = 1
                    print("x")
                    break
                else:
                    lis[ite]['text'] = temp
            if c == 0:
                s = random.choice(lista)
                if lis[s]["text"] != 'x' and lis[s]["text"] != 'o':
                    lis[s]['text'] = 'o'
                    c = 1
        elif c == 0:
            label1["text"] = 'unvalid/ no more moves'
        winner2(lis)


def winner(lister):
    if button1['text'] == button2['text'] == button3['text']:
        if button1['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button1['text'] == button4['text'] == button7['text']:
        if button1['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button1['text'] == button5['text'] == button9['text']:
        if button1['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button3['text'] == button5['text'] == button7['text']:
        if button3['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button3['text'] == button6['text'] == button9['text']:
        if button3['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button2['text'] == button5['text'] == button8['text']:
        if button2['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button4['text'] == button5['text'] == button6['text']:
        if button4['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'
    elif button7['text'] == button8['text'] == button9['text']:
        if button7['text'] == 'x':
            # label1['text']="player won"
            return 'x'
        else:
            # label1['text']='PC won'
            return 'o'


def winner2(lista):
    if winner(lista) == 'o':
        label1['text'] = 'PC won'
    elif winner(lista) == 'x':
        label1['text'] = 'Player won'


def restart(listat):
    listat[0]['text'] = ''
    for h in range(1, len(listat)):
        listat[h]["text"] = ' ' * h
    label1['text'] = ''


master.grid()

button1 = Button(master, text="", width=4, height=4, command=lambda: chooser(0))
button1.grid(row=0, column=0)
button2 = Button(master, text=" ", width=4, height=4, command=lambda: chooser(1))
button2.grid(row=0, column=1)
button3 = Button(master, text="  ", width=4, height=4, command=lambda: chooser(2))
button3.grid(row=0, column=2)
button4 = Button(master, text="   ", width=4, height=4, command=lambda: chooser(3))
button4.grid(row=1, column=0)
button5 = Button(master, text="    ", width=4, height=4, command=lambda: chooser(4))
button5.grid(row=1, column=1)
button6 = Button(master, text="     ", width=4, height=4, command=lambda: chooser(5))
button6.grid(row=1, column=2)
button7 = Button(master, text="       ", width=4, height=4, command=lambda: chooser(6))
button7.grid(row=2, column=0)
button8 = Button(master, text="        ", width=4, height=4, command=lambda: chooser(7))
button8.grid(row=2, column=1)
button9 = Button(master, text="         ", width=4, height=4, command=lambda: chooser(8))
button9.grid(row=2, column=2)
button10 = Button(master, text="res", width=4, height=4, command=lambda: restart(lis))
button10.grid(row=3, column=0, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=15, pady=15)
label1 = Label(master, text="", width=20, height=4)
label1.grid(row=4, column=3)
lis = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

master.mainloop()
