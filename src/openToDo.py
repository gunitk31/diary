from tkinter import filedialog
from tkinter import messagebox
import openpyxl
import toDoList


def open_file(current_window, data_dir):
    todo_title = ""
    task_list = []

    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("To Do Lists", "*.xlsx")],
        initialdir=data_dir
    )

    if file_path:
        if file_path.endswith("xlsx"):
            try:
                todo_title = file_path.split("/")[-1].split(".")[0]

                todo_excel = openpyxl.load_workbook(f"{file_path}")
                sheet = todo_excel[todo_title]

                task_list = [row[0] for row in sheet.iter_rows(values_only=True)]

            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {e}")

    current_window.destroy()
    toDoList.create_new_todo(todo_title, task_list)
