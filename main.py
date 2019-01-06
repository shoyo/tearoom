import tkinter as tk
from tearoom import Tearoom


def main():
    """Run the art piece."""
    root = tk.Tk()
    root.title("Tearoom of Zero/One")
    root.minsize(798, 574)
    root.geometry("798x574")
    tearoom = Tearoom(7)
    art_piece = TearoomGUI(root, tearoom)
    root.mainloop()


class TearoomGUI(tk.Frame):
    """Tkinter GUI for rendition of Tearoom of Zero/One."""

    def __init__(self, parent, tearoom):
        """Create GUI for Tearoom and run the art piece.

        parent           -- parent widget (should be root)
        tearoom          -- Tearoom instance to display
        teacups          -- list of Teacups contained in Tearoom
        teacup_frames    -- list of Frame child widgets for each Teacup
                            (parent is root)
        teacup_labels    -- list of Label grandchild widgets for each Teacup's
                            value (parent is corresponding Frame widget)
        refresh_interval -- time between each graphical update (milliseconds)
        """
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH)
        self.config(bg=frame_theme['bg'])
        self.tearoom = tearoom
        self.teacups = tearoom.teacups
        self.teacup_frames = self._init_teacup_frames()
        self.teacup_labels = self._init_teacup_labels()
        self.refresh_interval = 100

        self._run()

    def _init_teacup_frames(self):
        """Create a Frame widget for each Teacup. Return as a list.

        Each widget's parent widget is root.
        """
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
        """Create a Label widget for each Teacup's value. Return as a list.

        Each widget's parent widget is the corresponding Teacup's Frame widget.
        Each parent widget's parent widget is root.
        """
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
        """Continuously update Tearoom and widgets while Tearoom is alive."""
        if not self.tearoom.is_alive:
            return
        else:
            self.tearoom.update()
            self._update()
            self.after(self.refresh_interval, self._run)

    def _update(self):
        """Reconfigure each Label widget according to Teacup's value."""
        for i in range(len(self.teacups)):
            value_repr = ""
            if self.teacups[i].value:
                value_repr = str(self.teacups[i].value)
            self.teacup_labels[i].configure(text=value_repr)


# -- THEMES --
black = "#000000"
neon_green = "#39ff14"

frame_theme = {
    "bg": black,
}

tearoom_theme = {
    "font": ("Helvetica", 64, "bold"),
    "fg": neon_green,
    "bg": black,
    "fontwidth": 3,
}
# ----

if __name__ == '__main__':
    main()
