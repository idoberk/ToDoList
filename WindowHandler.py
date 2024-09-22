from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
WIDGET_STICKY = "ew"
X_PADDING = 5
Y_PADDING = 5
BUTTONS_WIDTH = 15

def open_new_window(root, button_name: str, command_type, tree_view):
	new_window = Toplevel(root)
	root.attributes('-disabled', True)
	if button_name == "Add":
		add_task_window(new_window, root, command_type, tree_view)

	elif button_name == "Edit":
		edit_task_window()

def add_task_window(add_window, root, command_type, tree_view):
	add_window.title("Add new task")
	add_window.geometry("325x200")
	add_window.config(padx = X_PADDING, pady = Y_PADDING)
	add_window.resizable(False, False) # Disables window being able to be resized
	add_window.grid_columnconfigure(0, weight = 1) # Makes column 0 expand
	add_window.grid_columnconfigure(1, weight = 1) # Makes column 1 expand
	add_window.grid_rowconfigure(2, weight = 1) # Makes row 2 expand (take extra space between the task_description_entry and the buttons)

	def on_close():
		root.attributes('-disabled', False)
		add_window.destroy()

	# ------ LABEL SETUP --------- #
	description_label = Label(add_window, text = "Description:")
	description_label.grid(column = 0, row = 0, padx = 1, sticky = "w")

	# ------ ENTRY SETUP --------- #
	task_description_entry = Entry(add_window)
	task_description_entry.focus()
	task_description_entry.grid(column = 0, row = 1, columnspan = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

	# ------ BUTTON SETUP --------- #
	submit_button = Button(add_window, width = BUTTONS_WIDTH, text = "Submit", command = lambda: command_type.submit_task(task_description_entry, tree_view))
	submit_button.grid(column = 0, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

	cancel_button = Button(add_window, width = BUTTONS_WIDTH, text = "Cancel", command = on_close)
	cancel_button.grid(column = 1, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

	add_window.grab_set() # Disabled interaction with other windows
	add_window.protocol("WM_DELETE_WINDOW", on_close) # Handles the window close event

def edit_task_window():
	pass