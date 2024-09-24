from tkinter import *
from tkinter import messagebox

from AddNewTask import AddNewTask
from WindowHandler import open_new_window, BUTTONS_WIDTH, center_window
from TreeViewHandler import create_tree_view
from EditTask import edit_task

# ---------------------------- TODO ------------------------------- #
# strike todo 1: ListRecord class
# strike todo 2: Add task completed time and calculate the time it took to finish the task
# strike todo 3: If user edits the task, it won't change the task created time
# strike todo 4: Consider refactoring the code and add a new class per action (AddTask, DeleteTask, EditTask, MarkTaskAsCompleted)
# strike todo 5: Create a new "WindowHandler" module that creates a new window when clicking on certain buttons
# todo 6: Add EditTask module to edit existing tasks (description, etc...)
# todo 7: Add DeleteTask module to delete existing tasks
# todo 8: Each action (Add / Delete / Edit...) will have a "unique" window configuration
# strike todo 9: Add Exit button to the main window

# ---------------------------- CONSTANTS ------------------------------- #
FONT = ("Ariel", 8, "bold")
X_PADDING = 10
Y_PADDING = 10
# todo 100: Add more constants (padding, width, etc...)


# ---------------------------- FUNCTIONS ------------------------------- #
def exit_window():
	"""Exits the program."""
	if messagebox.askokcancel("Quit", "Would you like to quit?"):
		root.destroy()


def edit():

	selected_item = tree_view.focus()
	print(tree_view.item(selected_item)['values'][2])

	#if tree_view.item(selected_item)['values'][2]:

def on_double_click(event):
	edit_task(event, tree_view)

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("To Do List")
root.geometry("950x550")
center_window(root)
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)
root.resizable(False, False)

tree_view = create_tree_view(root)
tree_view.bind("<Double-1>", on_double_click)

new_task = AddNewTask()  # FIXME: Find new location.



# ------ BACKGROUND SETUP --------- #


# ------ ENTRY SETUP --------- #


# ------ LABEL SETUP --------- #


# ------ BUTTON SETUP --------- #
add_button = Button(text = "Add", width = BUTTONS_WIDTH, command = lambda: open_new_window(root, "Add", new_task, tree_view))
add_button.grid(column = 0, row = 1, sticky = "sw", padx = X_PADDING, pady = (0, 10))
edit_button = Button(text = "Edit", width = BUTTONS_WIDTH, command = edit)
edit_button.grid(column = 1, row = 1, sticky = "s", padx = X_PADDING, pady = (0, 10))
exit_button = Button(text = "Exit", width = BUTTONS_WIDTH, command = exit_window)
exit_button.grid(column = 2, row = 1, sticky = "se", pady = (0, 10))


root.protocol("WM_DELETE_WINDOW", exit_window)
root.mainloop()

