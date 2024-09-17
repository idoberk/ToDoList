def print_menu():
	print(
		"Press 1 to add a new task\n"
		"Press 2 to delete a task\n"
		"Press 3 to edit an existing task\n"
		"Press 4 to mark task as completed\n"
		"Press 5 to print all tasks\n"
		"Press 6 to print tasks statistics\n"
		"press 0 to exit\n"
	)


class Menu:
	def __init__(self):
		print("Welcome\n")
		print_menu()

