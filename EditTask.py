from tkinter import *
from tkinter import ttk


def edit_task(event, tree_view, frame, user_task):
	region_clicked = tree_view.identify_region(event.x, event.y)
	if region_clicked != "cell":
		return

	column = tree_view.identify_column(event.x) # Get the index of the column
	selected_iid = tree_view.focus() # Get the iid of the selected row

	selected_values = tree_view.item(selected_iid) # Get the values of the selected row

	if column == '#3':
		selected_description = selected_values.get("values")[2]

	column_box = tree_view.bbox(selected_iid, column) # Get the coordinates of the box attached to the column
	entry_edit = Entry(frame, width = column_box[2])

	# Record the column index and item iid
	entry_edit.editing_column_index = 2
	entry_edit.editing_item_iid = selected_iid

	entry_edit.insert(0, selected_description)
	entry_edit.select_range(0, END)

	entry_edit.focus()

	entry_edit.bind("<FocusOut>", on_focus_out)
	entry_edit.bind("<Return>", lambda event: on_enter_pressed(event, tree_view, user_task))

	entry_edit.place(
		x = column_box[0] + 10,
		y = column_box[1] + 5,
		width = column_box[2],
		height = column_box[3]
		)

def on_enter_pressed(event, tree_view, user_task):
	"""Edit the task's description when pressing Enter."""
	new_description = event.widget.get()
	selected_iid = int(event.widget.editing_item_iid)

	current_values = tree_view.item(selected_iid).get("values")

	current_values[2] = new_description.title()
	tree_view.item(selected_iid, values = current_values)
	user_task.user_tasks_list[selected_iid - 1]["Description"] = current_values[2]
	event.widget.destroy()

def on_focus_out(event):
	"""Destroys the Entry when it's focused out."""
	event.widget.destroy()