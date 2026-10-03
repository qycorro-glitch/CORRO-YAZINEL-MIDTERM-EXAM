import tkinter as tk

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Midterm in OOP")
        self.root.geometry("400x200")

        # Row 0: Label and First Entry
        self.lbl1 = tk.Label(root, text="Enter your fullname:", fg="red")
        self.lbl1.place(x=30, y=50)

        self.txt1 = tk.Entry(root)
        self.txt1.place(x=200, y=50)

        # Row 1: Button and Second Entry
        self.btn = tk.Button(root, text="Click to display your Fullname", fg="red", command=self.show_name)
        self.btn.place(x=30, y=100)

        self.txt2 = tk.Entry(root)
        self.txt2.place(x=200, y=100)

    def show_name(self):
        self.txt2.delete(0, tk.END)
        self.txt2.insert(0, self.txt1.get())

# Main program
root = tk.Tk()
app = MyWindow(root)
root.mainloop()