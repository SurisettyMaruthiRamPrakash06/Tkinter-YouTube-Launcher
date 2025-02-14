import tkinter as tk
import tkinter.simpledialog as tk3
import tkinter.messagebox as tk2
import webbrowser

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('Ram Prakash')
        self.master.geometry('800x350')

        # Make frame expandable
        self.pack(expand=True, fill="both")

        # Playlist Listbox
        self.playlistbox = tk.Listbox(self, width=50, height=15, selectmode=tk.SINGLE)
        self.playlistbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        self.playButton = tk.Button(self, text='Play', command=self.play)
        self.addButton = tk.Button(self, text='Add YouTube Link', command=self.add)

        self.playButton.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.addButton.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.playlist = []

    def add(self):
        url = tk3.askstring("YouTube Link", "Enter YouTube URL:")
        if url:
            self.playlist.append(url)
            self.playlistbox.insert(tk.END, url)

    def play(self):
        if not self.playlist:
            tk2.showinfo('Notice', 'No Videos in your playlist! Click Add to Video Link.')
            return

        selected = self.playlistbox.curselection()
        if not selected:  # If no selection is made
            tk2.showwarning('Warning', 'Please select a Video to play.')
            return

        url = self.playlist[selected[0]]
        webbrowser.open(url)

root = tk.Tk()
app = Application(root)
root.mainloop()
