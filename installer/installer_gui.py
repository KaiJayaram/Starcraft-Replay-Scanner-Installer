from tkinter.filedialog  import askdirectory
import tkinter as tk
from pathlib import Path
from installer import install
import sys

## GUI for Installer
class GUI():
	def __init__(self):
		self.home = str(Path.home())
		self.default_loc = "{}\\Documents\\Starcraft Replay Scanner".format(self.home)
		self.root = tk.Tk()
		self.root.title("Starcraft Replay Scanner Installer")
		self.c_width = 800
		self.c_height = 300
		self.canvas = tk.Canvas(self.root, width=self.c_width, height=self.c_height)
		self.loc_entry_string = tk.StringVar()
		self.loc_entry_string.set(self.default_loc)
		self.installer_entry = tk.Entry (self.root, textvariable=self.loc_entry_string, width=60)
		self.title = tk.Label(self.root, text='Starcraft Replay Scanner Installer')
		self.title.config(font=('Arial', 20))
		self.help_text = tk.Label(self.root, text="Select Directory To Install")
		self.help_text.config(font=('Arial',12))
		self.browse_button = tk.Button (self.root, text='Browse',command=self.browse, font=('Arial', 11, 'bold')) 
		self.install_button = tk.Button (self.root, text='Install',command=self.install, font=('Arial', 11, 'bold'))
		self.error_text = tk.Label(self.root, text="failed to install to directory", fg="red")

	
	def start(self):
		self.canvas.pack()
		self.canvas.create_window(400, 50, window=self.title)
		self.canvas.create_window(100, 150,window=self.help_text)
		self.canvas.create_window(400, 150, window=self.installer_entry) 
		self.canvas.create_window(620, 150, window=self.browse_button)
		self.canvas.create_window(400, 250, window=self.install_button)
		self.root.mainloop()

	def browse(self):
		self.loc_entry_string.set(askdirectory())


	def install(self):
		res = install(self.loc_entry_string.get())
		if not res:
			self.canvas.create_window(275,250, window=self.error_text)
		else:
			self.success()

	def success(self):
		self.canvas.delete("all")
		self.canvas.config(width=300,height=100)
		succ = tk.Label(self.root, text="Install Complete!", fg="green")
		succ.config(font=('Arial', 14))
		self.canvas.create_window(150,50, window=succ)

def main():
	gui = GUI()
	gui.start()

if __name__ == '__main__':
	main()