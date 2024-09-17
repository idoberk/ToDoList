from tkinter import *

# ---------------------------- TODO ------------------------------- #
# todo 1: Refactor the open_new_window function so that the window will be configured based on the button pressed in the root window
# todo 2: Refactor the submit_task function
# todo 3: Refactor the class so that when creating a task, it will be an entire object (like in the ListRecord), with an 'empty' checkButton associated to each newly created task
# todo 4: Add descriptions to functions

# ---------------------------- CONSTANTS ------------------------------- #
WIDGET_STICKY = "ew"
X_PADDING = 5
Y_PADDING = 5
BUTTONS_WIDTH = 15

class AddNewTask:
	def __init__(self):
		self.user_tasks_list = []
		self.tasks_ID = 1

	def submit_task(self, input_entry):
		task_text = input_entry.get()
		if task_text:
			check_button = Checkbutton()
			check_button.grid(column = 0, row = self.tasks_ID)
			check_button.config(text = f'{task_text}')
			self.tasks_ID += 1
			self.user_tasks_list.append(check_button)
		input_entry.delete(0, END)

	def open_new_window(self, root):
		add_task_window = Toplevel(root)
		add_task_window.title("Add new task")
		add_task_window.geometry("325x200")
		add_task_window.config(padx = X_PADDING, pady = Y_PADDING)
		add_task_window.resizable(False, False) # Disables window being able to be resized
		add_task_window.grid_columnconfigure(0, weight = 1) # Makes column 0 expand
		add_task_window.grid_columnconfigure(1, weight = 1) # Makes column 1 expand
		add_task_window.grid_rowconfigure(2, weight = 1) # Makes row 2 expand (take extra space between the task_description_entry and the buttons)
		root.attributes('-disabled', True) # Disabled root window

		def on_close():
			"""Re-enables the root window and closes the current window."""
			root.attributes('-disabled', False)
			add_task_window.destroy()

		# ------ LABEL SETUP --------- #
		description_label = Label(add_task_window, text = "Description:")
		description_label.grid(column = 0, row = 0, padx = 1, sticky = "w")

		# ------ ENTRY SETUP --------- #
		task_description_entry = Entry(add_task_window)
		task_description_entry.focus()
		task_description_entry.grid(column = 0, row = 1, columnspan = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

		# ------ BUTTON SETUP --------- #
		submit_button = Button(add_task_window, width = BUTTONS_WIDTH, text = "Submit", command = lambda: self.submit_task(task_description_entry))
		submit_button.grid(column = 0, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

		cancel_button = Button(add_task_window, width = BUTTONS_WIDTH, text = "Cancel", command = on_close)
		cancel_button.grid(column = 1, row = 3, padx = X_PADDING, pady = Y_PADDING, sticky = WIDGET_STICKY)

		add_task_window.grab_set() # Disabled interaction with other windows
		add_task_window.protocol("WM_DELETE_WINDOW", on_close) # Handles the window close event