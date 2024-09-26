from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from AddNewTask import AddNewTask
from WindowHandler import open_new_window, BUTTONS_WIDTH, center_window
from TreeViewHandler import create_tree_view
from EditTask import edit_task
from DeleteTask import delete_task, on_treeview_select

# ---------------------------- TODO ------------------------------- #
# strike todo 1: ListRecord class
# strike todo 2: Add task completed time and calculate the time it took to finish the task
# strike todo 3: If user edits the task, it won't change the task created time
# strike todo 4: Consider refactoring the code and add a new class per action (AddTask, DeleteTask, EditTask, MarkTaskAsCompleted)
# strike todo 5: Create a new "WindowHandler" module that creates a new window when clicking on certain buttons
# strike todo 6: Add EditTask module to edit existing tasks (description, etc...)
# strike todo 7: Add DeleteTask module to delete existing tasks
# strike todo 8: Each action (Add / Delete / Edit...) will have a "unique" window configuration
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

def on_double_click(event):
	edit_task(event, tree_view, tree_view_frame, new_task)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
var = IntVar()
root.title("To Do List")
root.option_add('*TButton*takeFocus', 0)
root.option_add('*TRadiobutton*takeFocus', 0)
root.option_add('*TCombobox*takeFocus', 0)
root.geometry("935x370")
center_window(root)
root.minsize(width = 935, height = 370)

new_task = AddNewTask()  # FIXME: Find new location.



# ------ BACKGROUND SETUP --------- #
top_frame = ttk.Frame(root, padding = (10, 5))
top_frame.grid(row = 0, sticky = "news")

tree_view_frame = ttk.Frame(root)
tree_view_frame.grid(row = 1, sticky = "news")

buttons_frame = ttk.Frame(root, padding = (0, 10))
buttons_frame.grid(row = 3, sticky = "news")

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)

top_frame.grid_columnconfigure(2, weight = 1)

tree_view_frame.grid_columnconfigure(0, weight = 1)

buttons_frame.grid_columnconfigure(0, weight = 1)
buttons_frame.grid_columnconfigure(1, weight = 1)
buttons_frame.grid_columnconfigure(2, weight = 1)

tree_view = create_tree_view(tree_view_frame)
tree_view.bind("<Double-1>", on_double_click)

# ------ COMBOBOX SETUP --------- #
sort_by_combo_box = ttk.Combobox(top_frame, state = "readonly")
sort_by_combo_box['values'] = ('TaskID', 'Completion Time')
sort_by_combo_box.grid(column = 3, row = 0, padx = (0, 12))
sort_by_combo_box.current(0)


# ------ LABEL SETUP --------- #
sort_by_label = ttk.Label(top_frame, text = "Sort By: ")
sort_by_label.grid(column = 2, row = 0, sticky = "e")

# ------ BUTTON SETUP --------- #
add_button = ttk.Button(buttons_frame, text = "Add", width = BUTTONS_WIDTH, command = lambda: open_new_window(root, "Add", new_task, tree_view))
add_button.grid(column = 0, row = 0, sticky = "sw", padx = X_PADDING)

delete_button = ttk.Button(buttons_frame, text = "Delete", width = BUTTONS_WIDTH, state = DISABLED, command = lambda: delete_task(tree_view, new_task))
delete_button.grid(column = 1, row = 0, padx = X_PADDING)

exit_button = ttk.Button(buttons_frame, text = "Exit", width = BUTTONS_WIDTH, command = exit_window)
exit_button.grid(column = 2, row = 0, sticky = "se", padx = X_PADDING)

# ------ RADIO BUTTON SETUP --------- #
active_tasks = ttk.Radiobutton(top_frame, text = "Active Tasks", variable = var, value = 1)
active_tasks.grid(column = 0, row = 0, padx = (0, 20), sticky = "w")

completed_tasks = ttk.Radiobutton(top_frame, text = "Completed Tasks", variable = var, value = 2)
completed_tasks.grid(column = 1, row = 0, sticky = "w")


tree_view.bind("<<TreeviewSelect>>", lambda event: on_treeview_select(event, tree_view, delete_button))

root.protocol("WM_DELETE_WINDOW", exit_window)
root.mainloop()

