from tkinter import *
import math
import parser
import tkinter.messagebox
import conversion

root = Tk()
root.title("GAMGY CALCULATOR")
root.configure(background="bisque")
root.resizable(width=False, height=False)
root.geometry("480x568")

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mul":
            self.total *= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == "div":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def BD(self):
        self.result = False
        self.current =conversion. binary_to_decimal(float(txtDisplay.get()))
        self.display(self.current)

    def BO(self):
        self.result = False
        self.current = conversion.binary_to_octal(int(txtDisplay.get()))
        self.display(self.current)

    def BH(self):
        self.result = False
        self.current = conversion.binary_to_hexadecimal(int(txtDisplay.get()))
        self.display(self.current)

    def OB(self):
        self.result = False
        self.current = conversion.octal_to_binary(int(txtDisplay.get()))
        self.display(self.current)

    def OD(self):
        self.result = False
        self.current = conversion.octal_to_decimal(float(txtDisplay.get()))
        self.display(self.current)

    def HD(self):
        self.result = False
        self.current = conversion.hexadecimal_to_decimal(float(txtDisplay.get()))
        self.display(self.current)

    def HO(self):
        self.result = False
        self.current = conversion.hexadecimal_to_octal(int(txtDisplay.get()))
        self.display(self.current)

    def HB(self):
        self.result = False
        self.current = conversion.hexadecimal_to_binary(int(txtDisplay.get()))
        self.display(self.current)

    def DB(self):
        self.result = False
        self.current = conversion.decimal_to_binary(int(txtDisplay.get()))
        self.display(self.current)

    def DH(self):
        self.result = False
        self.current = conversion.decimal_to_hexadecimal(int(txtDisplay.get()))
        self.display(self.current)

    def DO(self):
        self.result = False
        self.current = conversion.decimal_to_octal(int(txtDisplay.get()))
        self.display(self.current)

    def OH(self):
        self.result = False
        self.current = conversion.octal_to_hexadecimal(int(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()), 10)
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()), 2.71)
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)



added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="snow2", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, font=('arial', 20, 'bold'), bg="Sienna1", bd=4, width=6, height=2, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1
# ===============================================================================================================
btnclear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="red", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
btnallclear = Button(calc, text=chr(65) + chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="red", command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)
btnadd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
btnsqrt = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="gray30", fg="snow",
                   command=added_value.sqrt).grid(row=1, column=2, pady=1)
btnsub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
btnmul = Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=lambda: added_value.operation("mul")).grid(row=3, column=3, pady=1)
btndiv = Button(calc, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=lambda: added_value.operation("div")).grid(row=4, column=3, pady=1)
btndegrees = Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, fg="snow",
               bg="gray30").grid(row=5, column=3, pady=1)
btnzero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, fg="snow",
                 bg="gray30", command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
btnequal = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, fg="snow",
                  bg="gray30", command=added_value.sum_of_total).grid(row=5, column=1, pady=1)
btndecimal = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                    command=lambda: added_value.numberEnter(".")).grid(row=5, column=2, pady=1)

# ============================================scientific calculator======================================================
btnpi = Button(calc, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
               command=added_value.pi).grid(row=1, column=4, pady=1)
btnsin = Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=added_value.sin).grid(row=1, column=5, pady=1)
btncos = Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=added_value.cos).grid(row=1, column=6, pady=1)
btntan = Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=added_value.tan).grid(row=1, column=7, pady=1)
btnBO = Button(calc, text="BO", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.BO).grid(row=2,column=5, pady=1)
btnBD = Button(calc, text="BD", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.BD).grid(row=2, column=4, pady=1)
btnBH = Button(calc, text="BH", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.BH).grid(row=2, column=6, pady=1)
btnOB = Button(calc, text="OB", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.OB).grid(row=2, column=7, pady=1)
btnOD = Button(calc, text="OD", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.OD).grid(row=3, column=4, pady=1)
btnOH = Button(calc, text="OH", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.OH).grid(row=3, column=5, pady=1)
btnHD = Button(calc, text="HD", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.HD).grid(row=3, column=6, pady=1)
btnHO = Button(calc, text="HO", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.HO).grid(row=3, column=7, pady=1)
btnHB = Button(calc, text="HB", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.HB).grid(row=4, column=4, pady=1)
btnDB = Button(calc, text="DB", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.DB).grid(row=4, column=5, pady=1)
btnDH = Button(calc, text="DH", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.DH).grid(row=4, column=6, pady=1)
btnDO = Button(calc, text="DO", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="snow2",
               command=added_value.DO).grid(row=4, column=7, pady=1)
btne = Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
              command=added_value.e).grid(row=5, column=4, pady=1)
btnln = Button(calc, text="ln", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
               command=added_value.ln).grid(row=5, column=7, pady=1)
btnlog = Button(calc, text="log", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray30", fg="snow",
                command=added_value.log).grid(row=5, column=6, pady=1)
btnexp= Button(calc, text="exp",width=6,height=2, font=('arial',20,'bold'),bd=4,bg="gray30", fg="snow",
               command =added_value.exp).grid(row=5,column=5,pady=1)
W = Label(calc, text="Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
W.grid(row=0, column=4, columnspan=4)


# ==================================================MENU FUNCTIONS======================================
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific calculator", "Are you sure you want to exit GAMGY CALCULATOR ?")
    if iExit > 0:
        root.destroy()
        return


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


root.config(menu=menubar)
root.mainloop()

