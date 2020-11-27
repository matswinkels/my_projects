import tkinter as tk

window = tk.Tk()
window.resizable(width=False, height=False)
window.title('Program')
window.geometry('600x600')

btn1 = tk.Button(window,
                 text='Button1',
                 height=10,
                 width=10)
btn2 = tk.Button(window,
                 text='Button2',
                 height=10,
                 width=10)
btn3 = tk.Button(window,
                 text='Button3',
                 height=10,
                 width=10)
btn4 = tk.Button(window,
                 text='Button4',
                 height=10,
                 width=10)
text1 = tk.Text(width=19, height=1)

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)
btn3.grid(row=0, column=1)
btn4.grid(row=1, column=1)
text1.grid(row=1, column=2, sticky='N')

window.mainloop()