import time
import tkinter as tk
from tearoom import Tearoom


def main():
    """Run the art piece."""
    root = tk.Tk()
    root.title("Tearoom of Zero/One")
    root.minsize(735, 525)
    root.geometry("735x525")
    tearoom = Tearoom(5)
    art_piece = TearoomGUI(root, tearoom)
    root.mainloop()


class TearoomGUI(tk.Frame):
    def __init__(self, parent, tearoom):
        """--documenation.--"""
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH)
        self.config(bg=frame_theme['bg'])
        self.refresh_interval = 100
        self.tearoom = tearoom
        self.teacups = tearoom.teacups
        self.teacup_frames = self._init_teacup_frames()
        self.teacup_labels = self._init_teacup_labels()

        self._run()

    def _init_teacup_frames(self):
        frames = []
        for _ in self.teacups:
            frames.append(tk.Frame(self))
        for i in range(len(self.teacups)):
            frames[i].config(bg=tearoom_theme['fg'])
        for i in range(self.tearoom.width):
            for j in range(self.tearoom.width):
                frames[i * self.tearoom.width + j] \
                    .grid(row=i, column=j)
        return frames

    def _init_teacup_labels(self):
        labels = []
        for i in range(len(self.teacups)):
            label = tk.Label(self.teacup_frames[i],
                             text="",
                             font=tearoom_theme["font"],
                             fg=tearoom_theme["fg"],
                             bg=tearoom_theme["bg"],
                             width=tearoom_theme["fontwidth"])
            label.pack()
            labels.append(label)
        return labels

    def _run(self):
        if not self.tearoom.is_alive:
            return
        else:
            self.tearoom.update()
            self._update()
            self.after(self.refresh_interval, self._run)

    def _update(self):
        for i in range(len(self.teacups)):
            value_repr = ""
            if self.teacups[i].value:
                value_repr = str(self.teacups[i].value)
            self.teacup_labels[i].configure(text=value_repr)


black = "#000000"
neon_green = "#39ff14"

frame_theme = {
    "bg": black,
}

tearoom_theme = {
    "font": ("Helvetica", 84, "bold"),
    "fg": neon_green,
    "bg": black,
    "fontwidth": 3,
}

if __name__ == '__main__':
    main()
