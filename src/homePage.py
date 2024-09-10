import tkinter as tk
import os
import entry
import toDoList
import openEntry
import openToDo


def launch_home_page():
    root = tk.Tk()
    root.title("Profess")
    root.geometry("600x700")  # Set the window size

    # Create a frame widget
    frame = tk.Frame(root, bg="#FF9999", bd=5, relief=tk.FLAT)
    frame.pack(fill=tk.BOTH, expand=True)  # Pack the frame with padding

    title_lbl = tk.Label(frame, text="Welcome to Profess!",
                         bg="#FF9999", fg="#5B9BD5",
                         font=("Harlow Solid Italic", 36))
    title_lbl.pack(pady=(100, 10))

    subtitle_lbl = tk.Label(frame, text="An Online Journal",
                            bg="#FF9999", fg="#5B9BD5",
                            font=("Harlow Solid Italic", 28))
    subtitle_lbl.pack(pady=(10, 30))

    add_entry_button = tk.Button(frame,
                                 text="Add a new entry",
                                 font=("Comic Sans MS", 16),
                                 command=lambda: [root.destroy(), entry.add_new_entry()])
    add_entry_button.pack(pady=(30, 5))

    create_todo_button = tk.Button(frame,
                                   text="Create a To Do List",
                                   font=("Comic Sans MS", 16),
                                   command=lambda: [root.destroy(), toDoList.create_new_todo()])
    create_todo_button.pack(pady=(5, 10))

    journal_data_dir = os.getenv("JOURNAL_DATA")
    entries_data_dir = f"{journal_data_dir}Entries"
    view_entries_button = tk.Button(frame,
                                    text="View all Journal Entries",
                                    font=("Comic Sans MS", 16),
                                    command=lambda: [openEntry.open_file(root, entries_data_dir)])
    view_entries_button.pack(pady=(5, 10))

    todo_data_dir = f"{journal_data_dir}To Do"
    view_todo_button = tk.Button(frame,
                                 text="View all To Do Lists",
                                 font=("Comic Sans MS", 16),
                                 command=lambda: [openToDo.open_file(root, todo_data_dir)])
    view_todo_button.pack(pady=(5, 10))

    exit_button = tk.Button(frame,
                            text="Exit",
                            font=("Comic Sans MS", 16),
                            command=lambda: [root.destroy()])
    exit_button.pack(pady=(5, 10))

    # Start the main event loop
    root.mainloop()


if __name__ == '__main__':
    launch_home_page()
