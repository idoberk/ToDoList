from tkinter import ttk
from tkinter import *

FONT = ("Ariel", 8, "bold")
X_PADDING = 10
Y_PADDING = 10
BUTTONS_WIDTH = 15

def create_tree_view(root):
	tree_view = ttk.Treeview(columns = ("", "taskID", "description", "created"))
	vertical_scroll_bar = ttk.Scrollbar(root, orient = VERTICAL, command = tree_view.yview)
	# horizontal_scroll_bar = ttk.Scrollbar(root, orient = HORIZONTAL, command = tree_view.xview)
	vertical_scroll_bar.grid(column = 3, row = 0, sticky = (N, S, W), padx = (0, 6), pady = Y_PADDING)
	# horizontal_scroll_bar.grid(column = 0, row = 1, sticky = (W, E, N, S), pady = X_PADDING)
	tree_view['yscrollcommand'] = vertical_scroll_bar.set
	# tree_view['xscrollcommand'] = horizontal_scroll_bar.set

	style = ttk.Style()
	style.configure("Treeview.Heading", font = FONT)
	style.configure('Treeview', rowheight = 20)

	tree_view.heading("#1", text = "")
	tree_view.column("#1", minwidth = 30, width = 30, anchor = "center")

	tree_view.heading("#2", text = "TaskID")
	tree_view.column("#2", minwidth = 60, width = 60, anchor = "center")

	tree_view.heading("#3", text = "Description")
	tree_view.column("#3", minwidth = 200, width = 680)

	tree_view.heading("#4", text = "Created")
	tree_view.column("#4", minwidth = 80, width = 130, anchor = "center")

	tree_view['show'] = 'headings'
	tree_view.grid(column = 0, row = 0, columnspan = 3, padx = (10, 0), pady = Y_PADDING, sticky = "news")

	return tree_view
