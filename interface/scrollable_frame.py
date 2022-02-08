import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.canvas = tk.Canvas(self, highlightthickness=0, **kwargs)
        self.vsb = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.sub_frame = tk.Frame(self.canvas, **kwargs)
        
        self.sub_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.create_window((0, 0), window=self.sub_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        
    def _on_frame_configure(self, event: tk.Event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))