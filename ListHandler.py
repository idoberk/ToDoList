from datetime import *
from ListRecord import ListRecord


class ListHandler:
	def __init__(self):
		self.user_to_do_list = []
		self.user_task = ListRecord()

	def add_new_task(self):

		self.user_to_do_list.append(self.user_task.add_new_record())

	def delete_task(self):
		remove_input = int(input(f"What number of task do you want to remove? "))
		try:
			self.user_to_do_list.pop(remove_input - 1)
		except IndexError:
			print("Unknown task number\n")

	def edit_task(self):
		edit_input = int(input(f"What number of task do you want to edit? "))
		try:
			if self.user_to_do_list[edit_input - 1]:
				self.user_to_do_list[edit_input - 1]["Description"] = input("Write the new task: ")

		except IndexError:
			print("Unknown task number\n")

	def mark_as_completed(self):
		mark_input = int(input(f"What number of task do you want to mark as completed? "))
		try:
			if self.user_to_do_list[mark_input - 1]:
				self.user_to_do_list[mark_input - 1]["Completed"] = True
				self.user_to_do_list[mark_input - 1]["Completed Time"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
				task_completion_time = datetime.strptime(self.user_to_do_list[mark_input - 1]["Completed Time"], "%d-%m-%Y %H:%M:%S")
				task_creation_time = datetime.strptime(self.user_to_do_list[mark_input - 1]["Created"], "%d-%m-%Y %H:%M:%S")
				self.user_to_do_list[mark_input - 1]["Task Completion Time"] = f"Task completed in {(task_completion_time - task_creation_time).total_seconds()} seconds."

		except IndexError:
			print("Unknown task number\n")

	def print_tasks_stats(self):
		completed_tasks = 0
		total_tasks = len(self.user_to_do_list)
		for i in range(total_tasks):
			if self.user_to_do_list[i]["Completed"]:
				completed_tasks += 1
		print(f"Total tasks: {total_tasks}\nCompleted tasks: {completed_tasks}\nIncomplete tasks: {total_tasks - completed_tasks}")

	def print_all_tasks(self):
		for record in self.user_to_do_list:
			print(record)

