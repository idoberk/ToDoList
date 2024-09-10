from datetime import *

class ListRecord:
	def __init__(self):
		self.counter = 1
		current_date = datetime.now()
		#self.task = {"TaskID": self.counter, "Description": "", "Created": "", "Completed": ""}
		# self.task = self.add_new_record()
		self.task = {"TaskID": self.counter, "Description": input(f"Please enter your task: "), "Created": current_date.strftime("%d-%m-%Y %H:%M:%S"), "Completed": ""}


	# def add_new_record(self):
	# 	current_date = datetime.now()
	# 	new_task = {"TaskID": self.counter, "Description": input(f"Please enter your task: "), "Created": current_date.strftime("%d-%m-%Y %H:%M:%S"), "Completed": ""}
	# 	self.counter += 1
	# 	print(new_task.items())
	# 	return new_task
	def counter(self):
		self.counter += 1


