import tkinter as tk

def insert_char(char):
    global entry, text_window

    if len(entry) != 18:
        entry = entry + char
        i = float(len(entry))
        insert(char, i)
        info['text'] = str(entry)
    else:
        info['text'] = 'Too many characters given (max=19)'

def cancel_one():
    global entry, text_window

    entry = entry[:-1]
    clean()
    insert(entry)
    info['text'] = str(entry)

def cancel_all():
    global entry, text_window

    entry = ''
    clean()
    info['text'] = str(entry)

def clean():
    text_window['state'] = 'normal'
    text_window.delete(.0, 'end')
    text_window['state'] = 'disabled'

def insert(x, i=.0):
    text_window['state'] = 'normal'
    text_window.insert(i, x)
    text_window['state'] = 'disabled'

def equals():
    global entry, text_window, score

    try:
        score = eval(entry)
        entry = str(score)
        text_window['state'] = 'normal'
        text_window.delete(.0, 'end')
        text_window.insert(.0, str(score))
        text_window['state'] = 'disabled'
        info['text'] = str(entry)
    except:
        info['text'] = 'Inserted value can not be evaluated'


window = tk.Tk()
window.resizable(width=False, height=False)
window.title('Calculator')
window.geometry('435x720')

button_size, font, bd = (2, 4), ('Arial', 30), 5

entry = ''
score = 0

b_cancel    = tk.Button(window, text='C', height=button_size[0], width=button_size[1], font=font, bd=bd, command=cancel_one)
b_divide    = tk.Button(window, text='/', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('/'))
b_times     = tk.Button(window, text='x', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('*'))
b_ce        = tk.Button(window, text='CE', height=button_size[0], width=button_size[1], font=font, bd=bd, command=cancel_all)
b_7         = tk.Button(window, text='7', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('7'))
b_8         = tk.Button(window, text='8', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('8'))
b_9         = tk.Button(window, text='9', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('9'))
b_minus     = tk.Button(window, text='-', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('-'))
b_4         = tk.Button(window, text='4', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('4'))
b_5         = tk.Button(window, text='5', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('5'))
b_6         = tk.Button(window, text='6', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('6'))
b_plus      = tk.Button(window, text='+', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('+'))
b_1         = tk.Button(window, text='1', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('1'))
b_2         = tk.Button(window, text='2', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('2'))
b_3         = tk.Button(window, text='3', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('3'))
b_equal     = tk.Button(window, text='=', height=button_size[0], width=button_size[1], font=font, bd=bd, command=equals)
b_b1        = tk.Button(window, text='(', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('('))
b_0         = tk.Button(window, text='0', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('0'))
b_coma      = tk.Button(window, text=',', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char('.'))
b_b2        = tk.Button(window, text=')', height=button_size[0], width=button_size[1], font=font, bd=bd, command=lambda: insert_char(')'))
text_window = tk.Text(window, width=19, height=1, font=font, state='disabled')
text_window.grid(row=0, columnspan=4, sticky='S')
info = tk.Label(window, text=' ')
info.grid(row=6, columnspan=4, sticky='SW')

buttons = [b_cancel, b_divide, b_times, b_ce,
           b_7, b_8, b_9, b_minus,
           b_4, b_5, b_6, b_plus,
           b_1, b_2, b_3, b_equal,
           b_b1, b_0, b_coma, b_b2]
positions = [(1,0), (1,1), (1,2), (1,3),
             (2,0), (2,1), (2,2), (2,3),
             (3,0), (3,1), (3,2), (3,3),
             (4,0), (4,1), (4,2), (4,3),
             (5,0), (5,1), (5,2), (5,3)]

for index, button in enumerate(buttons):
    button.grid(row=positions[index][0], column=positions[index][1])


window.mainloop()
