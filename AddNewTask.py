from datetime import *
from tkinter import *
from tkinter import messagebox

# ---------------------------- TODO ------------------------------- #
# strike todo 1: Refactor the open_new_window function so that the window will be configured based on the button pressed in the root window
# strike todo 2: Refactor the submit_task function
# strike todo 3: Refactor the class so that when creating a task, it will be an entire object (like in the ListRecord)
# strike todo 4: Add descriptions to functions
# todo 5: Close the add task window after submitting a new task (optional)

# ---------------------------- CONSTANTS ------------------------------- #
WIDGET_STICKY = "ew"
X_PADDING = 5
Y_PADDING = 5
BUTTONS_WIDTH = 15

class AddNewTask:
	def __init__(self):
		self.user_tasks_list = []
		self.tasks_ID = 1
		self.title = "Add new task"

	def update_task_id(self):
		"""Increment taskID"""
		self.tasks_ID += 1

	def submit_task(self, input_entry, tree_view):
		"""Adds a new row in the TreeView table."""
		task_text = input_entry.get().title()
		task_created_time = datetime.now()
		if task_text.strip():
			new_task = {
				"TaskID": self.tasks_ID,
				"Description": task_text.lstrip(),
				"Created": task_created_time.strftime("%d-%m-%Y %H:%M:%S"),
				# "Completed Time": "",
				# "Completed": task_completed,
				# "Task Completion Time": ""
			}
			input_entry.delete(0, END)
			self.user_tasks_list.append(new_task)
			tree_view.insert(
				"",
				END,
				values = (f"{self.tasks_ID}", self.user_tasks_list[self.tasks_ID - 1]["TaskID"], self.user_tasks_list[self.tasks_ID - 1]['Description'], self.user_tasks_list[
					self.tasks_ID - 1][
					"Created"])
			)
			self.update_task_id()
		else:
			messagebox.showwarning(title = "Oops", message = "Description can't be empty!")