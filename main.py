# from tkinter import *
#
# window = Tk()
# window.title("To Do List")
# window.config(width = 1000, height = 400)
#
# canvas = Canvas(width = 500, height = 200)
# title_text = canvas.create_text(250, 40, text = f"To Do List", font = ("Ariel", 40, "italic"))
# canvas.grid(column = 0, row = 0)
#
# add_btn = Button(width = 2, height = 1, text = f"Add", font = ("Ariel", 12, "italic"), bg = "green")
# add_btn.grid(column = 0, row = 1)
#
# window.mainloop()

# TODO 1: ListRecord class
# TODO 2: ListRecord object = string of the task
# TODO 3: Add task completed time and calculate the time it took to finish the task
# TODO 4: If user edits the task, it won't change the task created time


# TODO 100: Add checkbox button, delete button, edit button to the ListRecord object

from ListHandler import ListHandler
from ListRecord import ListRecord
from Menu import Menu
# counter = 1
# task = {"TaskID": counter, "Description": "xxxx", "Created": "xx.xx.xx", "Completed": "x"}
# print(task.items())

main_menu = Menu()
user_list = ListHandler()
is_program_running = True

while is_program_running:
	selection = int(input(f"What would you like to do? "))
	if selection == 1:
		add_more_tasks = True
		while add_more_tasks:
			new_task = ListRecord()

			# user_list.print_all_tasks()
			user_input = input(f"Would you like to add another record? Y / N: ").lower()
			if user_input == "n":
				add_more_tasks = False

	elif selection == 2:
		user_list.remove()
		user_list.print_all_tasks()

	elif selection == 3:
		user_list.edit()

	elif selection == 4:
		user_list.print_all_tasks()

	if selection == 0:
		is_program_running = False
		exit(0)

	main_menu.print_menu()