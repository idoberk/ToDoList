from tkinter import *
from tkinter import ttk

# ---------------------------- CONSTANTS ------------------------------- #
WIDGET_STICKY = "ew"
X_PADDING = 5
Y_PADDING = 5
BUTTONS_WIDTH = 15

def center_window(root):
	"""Centering the window on the screen monitor."""
	root.update_idletasks()
	width = root.winfo_width()
	height = root.winfo_height()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width - width) // 2
	y = (screen_height - height) // 2
	root.geometry(f"{width}x{height}+{x}+{y}")

def open_new_window(root, button_name: str, command_type, tree_view):
	new_window = Toplevel(root)
	root.attributes('-disabled', True)

	new_window.geometry("325x200")
	center_window(new_window)
	new_window.config(padx = X_PADDING, pady = Y_PADDING)
	new_window.resizable(False, False) # Disables window being able to be resized
	new_window.grid_columnconfigure(0, weight = 1) # Makes column 0 expand
	new_window.grid_columnconfigure(1, weight = 1) # Makes column 1 expand
	new_window.grid_rowconfigure(2, weight = 1) # Makes row 2 expand (take extra space between the task_description_entry and the buttons)

	def on_close():
		root.attributes('-disabled', False)
		new_window.destroy()

	# ------ LABEL SETUP --------- #
	description_label = ttk.Label(new_window, text = "Description:")
	description_label.grid(column = 0, row = 0, padx = 1, sticky = "w")

	cancel_button = ttk.Button(new_window, width = BUTTONS_WIDTH, text = "Cancel", command = on_close)
	cancel_button.grid(column = 1, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

	# ------ BUTTON SETUP --------- #
	new_window.grab_set()  # Disabled interaction with other windows
	new_window.protocol("WM_DELETE_WINDOW", on_close)  # Handles the window close event

	if button_name == "Add":
		new_window.title(command_type.title)
		task_description_entry = ttk.Entry(new_window)
		task_description_entry.focus()
		task_description_entry.grid(column = 0, row = 1, columnspan = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)
		# ------ BUTTON SETUP --------- #
		submit_button = ttk.Button(new_window, width = BUTTONS_WIDTH, text = "Submit", command = lambda: command_type.submit_task(task_description_entry, tree_view))
		submit_button.grid(column = 0, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)
		task_description_entry.bind("<Return>", lambda event: command_type.submit_task(task_description_entry, tree_view, event))