from tkinter import *

def delete_task(tree_view, tasks):
	selected_row = tree_view.focus()
	for idx in range(0, len(tasks.user_tasks_list)):
		if int(selected_row) == int(tasks.user_tasks_list[idx]['TaskID']):
			tasks.user_tasks_list.pop(idx)
			break
	tree_view.delete(selected_row)

def on_treeview_select(event, tree_view, del_button):
	selected_row = tree_view.focus()
	if selected_row:
		del_button.config(state = NORMAL)
	else:
		del_button.config(state = DISABLED)
