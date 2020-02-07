# https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_target_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def open_training_files():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    
def open_result_file():
    """Open a file."""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="csv",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
    
def run():
    btn_run.bg = "red"
    """ run the calculation """
    print("run...")
    
def quit():
    """ quit the program """
    window.destroy()
    
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open_target = ttk.Button(fr_buttons, text="Open Target...", command=open_target_file)
btn_open_training = ttk.Button(fr_buttons, text="Open Training Files...", command=open_training_files)
btn_run = ttk.Button(fr_buttons, text="Run the calculation", command=run)

btn_open_result = ttk.Button(fr_buttons, text="Open Result File...", command=open_result_file)
btn_quit = ttk.Button(fr_buttons, text="Quit", command=quit)

btn_open_target.grid(row=0, column=0, sticky="EW", padx=5, pady=10)
btn_open_training.grid(row=1, column=0, sticky="EW", padx=5, pady=10)
btn_run.grid(row=2, column=0, sticky ="EW", padx=5, pady=10)
btn_open_result.grid(row=3, column=0, sticky="EW", padx=5, pady=10)
btn_quit.grid(row=4, column=0, sticky ="EW", padx=5, pady=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()