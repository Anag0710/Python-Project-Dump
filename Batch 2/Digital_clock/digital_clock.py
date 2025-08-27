
import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("500x200")
        self.root.configure(bg="#232946")

        self.canvas = tk.Canvas(self.root, height=200, width=500, bg="#232946", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Shadow effect
        self.shadow = self.canvas.create_rectangle(60, 60, 440, 140, fill="#121629", outline="", width=0)
        # Rounded rectangle for clock display
        self.rounded_rect = self.canvas.create_rectangle(50, 50, 450, 150, fill="#eebbc3", outline="#232946", width=4)

        self.frame = tk.Frame(self.root, bg="#eebbc3")
        self.frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

        self.lbl = tk.Label(self.frame, font=("Segoe UI", 48, "bold"), background="#eebbc3", foreground="#232946")
        self.lbl.pack(expand=True)

        self.theme = "light"
        self.create_menu()
        self.update_time()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Light", command=self.set_light_theme)
        theme_menu.add_command(label="Dark", command=self.set_dark_theme)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        self.root.config(menu=menubar)

    def set_light_theme(self):
        self.theme = "light"
        self.root.configure(bg="#f7f7f7")
        self.canvas.itemconfig(self.rounded_rect, fill="#eebbc3", outline="#232946")
        self.canvas.itemconfig(self.shadow, fill="#d3d3d3")
        self.frame.configure(bg="#eebbc3")
        self.lbl.configure(background="#eebbc3", foreground="#232946")

    def set_dark_theme(self):
        self.theme = "dark"
        self.root.configure(bg="#232946")
        self.canvas.itemconfig(self.rounded_rect, fill="#232946", outline="#eebbc3")
        self.canvas.itemconfig(self.shadow, fill="#121629")
        self.frame.configure(bg="#232946")
        self.lbl.configure(background="#232946", foreground="#eebbc3")

    def update_time(self):
        string = strftime('%I:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
