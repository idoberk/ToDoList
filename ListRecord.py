from tkinter import *
from datetime import *

class ListRecord:
	def __init__(self):
		self.counter = 1
		self.check_button = self.add_check_button()

	def update_task_id(self):
		self.counter += 1

	def add_description(self):
		task_description = Entry(width = 50)
		task_description.focus()
		task_description.grid(column = 0, row = 0)
		save_button = Button(text = "Add", width = 35, command = self.add_check_button)
		save_button.grid(column = 1, row = 0)
		task_text = task_description.get()
		self.check_button.config(text = task_text)

	def add_check_button(self):
		check_button = Checkbutton()
		check_button.grid(column = 0, row = self.counter)
		self.update_task_id()
		return check_button

	def add_new_record(self):
		pass
		# task_description = input(f"Please enter your task: ").title()
		# task_completed = False
		# task_created_time = datetime.now()
		# new_task = {
		# 	"TaskID": self.counter,
		# 	"Description": task_description,
		# 	"Created": task_created_time.strftime("%d-%m-%Y %H:%M:%S"),
		# 	"Completed Time": "",
		# 	"Completed": task_completed,
		# 	"Task Completion Time": ""
		# }
		# self.update_task_id()
		# check_button = Checkbutton(command = add_description)
		# check_button.config(text = add_description())
		# check_button.grid(column = 0, row = self.counter)
		# self.update_task_id()
		# check_button = self.add_check_button()

		# return new_task