# ---------------------------- TODO ------------------------------- #
# strike todo 1: ListRecord class
# strike todo 2: Add task completed time and calculate the time it took to finish the task
# strike todo 3: If user edits the task, it won't change the task created time
# strike todo 4: Consider refactoring the code and add a new class per action (AddTask, DeleteTask, EditTask, MarkTaskAsCompleted)
# strike todo 5: Create a new "WindowHandler" module that creates a new window when clicking on certain buttons
# todo 6: Add EditTask module to edit existing tasks (description, etc...)
# todo 7: Add DeleteTask module to delete existing tasks
# todo 8: Each action (Add / Delete / Edit...) will have a "unique" window configuration
# todo 9: Add Exit button to the main window

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

from ListHandler import ListHandler
from Menu import Menu, print_menu
from AddNewTask import AddNewTask
from WindowHandler import open_new_window

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Ariel", 8, "bold")

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("To Do List")
root.geometry("920x400")
root.resizable(True, False)
tree_view = ttk.Treeview(columns = ("", "taskID", "description", "created"))
vertical_scroll_bar = ttk.Scrollbar(root, orient = VERTICAL, command = tree_view.yview)
horizontal_scroll_bar = ttk.Scrollbar(root, orient = HORIZONTAL, command = tree_view.xview)
vertical_scroll_bar.grid(column = 1, row = 0, sticky = (N, S))
horizontal_scroll_bar.grid(column = 0, row = 1, sticky = (W, E))
tree_view['yscrollcommand'] = vertical_scroll_bar.set
tree_view['xscrollcommand'] = horizontal_scroll_bar.set

style = ttk.Style()
style.configure("Treeview.Heading", font = FONT)
style.configure('Treeview', rowheight = 30)
tree_view.heading("#1", text = "")
tree_view.column("#1", minwidth = 30, width = 30, anchor = "center")
tree_view.heading("#2", text = "TaskID")
tree_view.column("#2", minwidth = 60, width = 60, anchor = "center")
tree_view.heading("#3", text = "Description")
tree_view.column("#3", minwidth = 200, width = 680)
tree_view.heading("#4", text = "Created")
tree_view.column("#4", minwidth = 80, width = 130, anchor = "center")

new_task = AddNewTask()  # FIXME: Find new location.

# tree_view.insert(
# 	"",
# 	END,
# 	values = (new_task.user_tasks_list[0]["TaskID"], new_task.user_tasks_list[0]['Description'], new_task.user_tasks_list[0]["Created"])
# )
tree_view['show'] = 'headings'
tree_view.grid(column = 0, row = 0)

# ------ BACKGROUND SETUP --------- #

# new_task = AddNewTask() # FIXME: Find new location.


# ------ ENTRY SETUP --------- #


# ------ LABEL SETUP --------- #


# ------ BUTTON SETUP --------- #
add_button = Button(text = "Add", command = lambda: open_new_window(root, "Add", new_task, tree_view))
add_button.grid(column = 0, row = 2)

# main_menu = Menu()
# user_list = ListHandler()
# is_program_running = True
# check_button = Checkbutton(user_list.add_new_task())


root.mainloop()

# while is_program_running:
# 	user_selection = int(input(f"What would you like to do? "))
# 	if user_selection == 1:
# 		while True:
# 			user_list.add_new_task()
#
# 			user_input = input(f"Would you like to add another record? Y / N: ").lower()
# 			if user_input == "n":
# 				break
#
# 	elif user_selection == 2:
# 		user_list.delete_task()
# 		user_list.print_all_tasks()
#
# 	elif user_selection == 3:
# 		user_list.edit_task()
#
# 	elif user_selection == 4:
# 		user_list.mark_as_completed()
#
# 	elif user_selection == 5:
# 		user_list.print_all_tasks()
#
# 	elif user_selection == 6:
# 		user_list.print_tasks_stats()
#
# 	if user_selection == 0:
# 		is_program_running = False
# 		exit(0)
#
# 	print_menu()