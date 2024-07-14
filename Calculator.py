import tkinter as tk

# Function for expression updation
def press(num):
    global exp
    exp += str(num)
    equation.set(exp)

# Function for final expression value determination
def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set(" error ")
        exp = ""

# Function to clear the contents of the entry box
def clear():
    global exp
    exp = ""
    equation.set("")

# Function to remove the last character from the entry
def remove_last():
    global exp
    exp = exp[:-1]
    equation.set(exp)

# Main code
if __name__ == "__main__":
    window = tk.Tk()
    window.configure(background="pink")
    window.title("Simple Calculator")
    window.geometry("260x220")

    global exp
    exp = ""
    equation = tk.StringVar()

    fexp = tk.Entry(window, textvar=equation)
    fexp.grid(columnspan=4, ipadx=70, rowspan=2)

    b1 = tk.Button(window, text=' 1 ', fg='black', bg='light green', command=lambda: press(1), height=2, width=8)
    b1.grid(row=2, column=0)

    b2 = tk.Button(window, text=' 2 ', fg='black', bg='light green', command=lambda: press(2), height=2, width=8)
    b2.grid(row=2, column=1)

    b3 = tk.Button(window, text=' 3 ', fg='black', bg='light green', command=lambda: press(3), height=2, width=8)
    b3.grid(row=2, column=2)

    b4 = tk.Button(window, text=' 4 ', fg='black', bg='light green', command=lambda: press(4), height=2, width=8)
    b4.grid(row=3, column=0)

    b5 = tk.Button(window, text=' 5 ', fg='black', bg='light green', command=lambda: press(5), height=2, width=8)
    b5.grid(row=3, column=1)

    b6 = tk.Button(window, text=' 6 ', fg='black', bg='light green', command=lambda: press(6), height=2, width=8)
    b6.grid(row=3, column=2)

    b7 = tk.Button(window, text=' 7 ', fg='black', bg='light green', command=lambda: press(7), height=2, width=8)
    b7.grid(row=4, column=0)

    b8 = tk.Button(window, text=' 8 ', fg='black', bg='light green', command=lambda: press(8), height=2, width=8)
    b8.grid(row=4, column=1)

    b9 = tk.Button(window, text=' 9 ', fg='black', bg='light green', command=lambda: press(9), height=2, width=8)
    b9.grid(row=4, column=2)

    plus = tk.Button(window, text=' + ', fg='black', bg='light green', command=lambda: press("+"), height=2, width=8)
    plus.grid(row=2, column=3)

    sub = tk.Button(window, text=' - ', fg='black', bg='light green', command=lambda: press("-"), height=2, width=8)
    sub.grid(row=3, column=3)

    mult = tk.Button(window, text=' * ', fg='black', bg='light green', command=lambda: press("*"), height=2, width=8)
    mult.grid(row=4, column=3)

    div = tk.Button(window, text=' / ', fg='black', bg='light green', command=lambda: press("/"), height=2, width=8)
    div.grid(row=5, column=3)

    equal = tk.Button(window, text=' = ', fg='black', bg='light pink', command=equalpress, height=2, width=8)
    equal.grid(row=5, column=2)

    clear = tk.Button(window, text='Clear', fg='black', bg='orange', command=clear, height=2, width=8)
    clear.grid(row=5, column=0)

    remove = tk.Button(window, text='Remove', fg='black', bg='light blue', command=remove_last, height=2, width=8)
    remove.grid(row=5, column=1)

    window.mainloop()
