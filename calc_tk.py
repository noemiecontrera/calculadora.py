import tkinter as tk

calc = tk.Tk()
calc.title("Calculadora")
calc.geometry("235x300")
calc.resizable(False, False)

calc_input = tk.Entry(calc, borderwidth=5)
calc_input.grid(columnspan=4, ipadx=50, pady=5)
calc_input.delete(0, tk.END)

def click(vlr):
    calc_input.insert(tk.END, str(vlr))

def clear():
    calc_input.delete(0, tk.END)

def calculate():
    try:
        result = eval(calc_input.get())
        calc_input.delete(0,tk.END)
        calc_input.insert(0, str(result))
       
    except: 
        calc_input.delete(0, tk.END)
        calc_input.insert(0, "Erro")


button1 = tk.Button(calc, text="1", fg='black', bg='pink', command=lambda: click(1) ,height=3, width=4)
button1.grid(row=1, column=0, padx=5, pady=2)

button4 = tk.Button(calc, text="4", fg='black', bg='pink', command=lambda: click(4) ,height=3, width=4)
button4.grid(row=2, column=0, padx=5, pady=2)

button7 = tk.Button(calc, text="7", fg='black', bg='pink',command=lambda: click(7), height=3, width=4)
button7.grid(row=3, column=0, padx=5, pady=2)

button2 = tk.Button(calc, text="2", fg='black', bg='pink', command=lambda: click(2),height=3, width=4)
button2.grid(row=1, column=1, padx=5, pady=2)

button5 = tk.Button(calc, text="5", fg='black', bg='pink', command=lambda: click(5),height=3, width=4)
button5.grid(row=2, column=1, padx=5, pady=2)

button8 = tk.Button(calc, text="8", fg='black', bg='pink', command=lambda: click(8), height=3, width=4)
button8.grid(row=3, column=1,padx=5, pady=2)

button3 = tk.Button(calc, text="3", fg='black', bg='pink', command=lambda: click(3) ,height=3, width=4)
button3.grid(row=1, column=2, padx=5, pady=2)

button6 = tk.Button(calc, text="6", fg='black', bg='pink',command=lambda: click(6) ,height=3, width=4)
button6.grid(row=2, column=2, padx=5, pady=2)

button9 = tk.Button(calc, text="9", fg='black', bg='pink', command=lambda: click(9), height=3, width=4)
button9.grid(row=3, column=2, padx=5, pady=2)

button_clear = tk.Button(calc, text="cl", fg='black', bg='bisque1', command=clear, height=3, width=4)
button_clear.grid(row=4, column=0, padx=5, pady=2)

button0 = tk.Button(calc, text="0", fg='black', bg='pink', command=lambda: click(0) ,height=3, width=4)
button0.grid(row=4, column=1, padx=5, pady=2)

button_equals = tk.Button(calc, text="=",fg='black', bg='indian red', height=3, width=4,  command=calculate)
button_equals.grid(row=4, column=2, padx=5, pady=2)

button_sum = tk.Button(calc, text="+", fg='black', bg='AntiqueWhite1',command=lambda: click('+'), height=3, width=4)
button_sum.grid(row=1, column=3, padx=5, pady=2)

button_sub = tk.Button(calc, text="-", fg='black', bg='AntiqueWhite1',command=lambda: click('-'), height=3, width=4)
button_sub.grid(row=2, column=3, padx=5, pady=2)

button_mult = tk.Button(calc, text="*", fg='black', bg='AntiqueWhite1',command=lambda: click('*'), height=3, width=4)
button_mult.grid(row=3, column=3, padx=5, pady=2)

button_div = tk.Button(calc, text="/", fg='black', bg='AntiqueWhite1', command=lambda: click('/'),height=3, width=4)
button_div.grid(row=4, column=3, padx=5, pady=2)


""" botoes = [
  ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
  ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
  ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
  ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
  ("=", 5, 0, 4)
] """

calc.mainloop()