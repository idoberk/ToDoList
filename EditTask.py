import tkinter as tk
from tkinter import ttk

def edit_task(event, tree_view):
	# selected_row = tree_view.focus()
	# print(tree_view.item(selected_row)['values'][2])
	# print(tree_view.identify_region(event.x, event.y))
	region_clicked = tree_view.identify_region(event.x, event.y)
	if region_clicked != "cell":
		return

	column = tree_view.identify_column(event.x)
	selected_iid = tree_view.focus()

	selected_values = tree_view.item(selected_iid)

	print(column, selected_iid, selected_values)

	if column == '#3':
		selected_description = selected_values.get("values")[2]

	print(selected_description)