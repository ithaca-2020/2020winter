import tkinter as tk


class MyCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('calculator')
        self.memory = 0
        self.create()

    def create(self):
        btn_list = ["C", "M->", "->M", "/",
                    "7", "8", "9", "*",
                    "4", "5", "6", "-",
                    "1", "2", "3", "+",
                    "+/-", "0", ".", "="]
        # row and column
        r = 1
        c = 1
        for buttom in btn_list:
            self.buttom = tk.Button(self, text=buttom, width=5, command=lambda x=buttom: self.click(x))
            self.buttom.grid(row=r, column=c, padx=3, pady=6)
            c += 1
            if c >= 5:
                c = 1
                r += 1
        self.entry = tk.Entry(self, width=24, borderwidth=2,
                              bg="yellow", font=("Consolas", 12))
        self.entry.grid(row=0, column=1, columnspan=4, padx=8, pady=6)

    def click(self, key):
        if key == '=':
            result = eval(self.entry.get())
            self.entry.insert(tk.END, '=' + str(result))
        elif key == 'C':
            self.entry.delete(0, tk.END)
        elif key == '->M':
            self.memory = self.entry.get()
            self.memory = self.entry.get()
            if "=" in self.memory:
                ix = self.memory.find("=")
                self.memory = self.memory[ix + 2:]
            self.title("M=" + self.memory)
        elif key == 'M->':
            self.title('calculator')
            self.entry.insert(tk.END, self.memory)
            self.memory = 0
        elif key == "+/-":  # 正负翻转
            if "=" in self.entry.get():
                self.entry.delete(0, tk.END)
            elif self.entry.get()[0] == "-":
                self.entry.delete(0)
            else:
                self.entry.insert(0, "-")
        else:
            if "=" in self.entry.get():
                self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    cal = MyCalculator()
    cal.mainloop()
