import tkinter as tk
from tkinter import ttk
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("COVID")
        self.setup()

    def setup(self):
        self.tk.call("source", resource_path("azure.tcl"))
        self.tk.call("set_theme", "light")

        # Configure
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        # text
        self.text = tk.Text(self, height=20)
        self.text.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # button
        self.button = ttk.Button(self, text="Confirm", command=self.confirm)
        self.button.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.bind("<Return>", lambda event: self.confirm())

        # tree
        self.result = ttk.Frame(self)
        self.result.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.result.columnconfigure(index=0, weight=1)
        self.result.rowconfigure(index=0, weight=1)

        self.scrollbar = ttk.Scrollbar(self.result, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="nsew")
        self.tree = ttk.Treeview(self.result, selectmode="none", height=10)
        self.tree.config(columns=["medicine", "caution"])
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree.yview)

        self.tree.column("#0", width=0, stretch="no")
        self.tree.heading("#0", text="Label", anchor="center")

        # dic
        self.dic = {
            "apple" : "Very Dangerous",
            "banana" : "Dangerous",
            "mango" : "Caution"
        }

    def confirm(self):
        self.data = self.text.get('1.0', 'end')
        self.data = self.data.lower()

        for item in self.tree.get_children():
            self.tree.delete(item)

        self.tree.config(column=(1,2))
        self.tree.column("#0", minwidth=0, stretch="no")
        self.tree.heading("#0", text="Label", anchor="center")
        self.tree.column(1, anchor="center", minwidth=100)
        self.tree.heading(1, text="medicine", anchor="center")
        self.tree.column(2, anchor="center", minwidth=100)
        self.tree.heading(2, text="caution", anchor="center")

        for x in self.dic:
            if self.data.find(x) != -1 :
                self.tree.insert('', index="end", values=[x, self.dic[x]])
        



if __name__ == "__main__":
    root = App()
    root.mainloop()
