from tkinter import filedialog
from tkinter import messagebox
import docx
import entry


def open_file(current_window, data_dir):
    entry_title = ""
    entry_content = ""

    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Word Documents", "*.docx")],
        initialdir=data_dir
    )

    if file_path:
        if file_path.endswith("docx"):
            try:
                entry_doc = docx.Document(file_path)
                for content_p in entry_doc.paragraphs:
                    if content_p.style.name == 'Title':
                        entry_title = content_p.text
                    else:
                        entry_content += content_p.text
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {e}")

    current_window.destroy()
    entry.add_new_entry(entry_title, entry_content)
