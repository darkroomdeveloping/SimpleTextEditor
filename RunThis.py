# https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app
#import harvestExpLearn3FullPathModule as harvest
import harvestExpLearn3Module as harvest
import tkinter as tk
import tkinter.ttk as ttk
#import io
import time
import sys
from tkinter.filedialog import askopenfilename, asksaveasfilename

script_path = ""
targetFile = ""
trainingTuples = ()
trainingSets = []

def select_python_script():
    global script_path
    """Select calculation script a file for."""
    filepath = askopenfilename(
        filetypes=[("Python Files", "*.py")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    script_path = filepath
    print("script_path: ", script_path)
    with open(filepath, "r") as input_script_file:
        text = input_script_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"BuildABear - {filepath}")
    print("input_script_file:",input_script_file)
    
def open_target_file():
    global targetFile
    """Select a target file."""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    targetFile = filepath
    print("STE targetFile: ", targetFile)
    with open(filepath, "r") as input_target_file:
        text = input_target_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"BuildABear - {filepath}")

def convert_tuple_into_list(tpl):
    list = []
    for element in tpl:
#        print("tuple elemetn: ", element)
        list.append(element)
    return list

def open_training_files():
    global trainingSets
    """Select training files."""
    filepaths = askopenfilename(multiple=True,
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepaths:
        return
    txt_edit.delete(1.0, tk.END)
    trainingTuples = filepaths
    print("\nSTE 66 - trainingTuples: ", trainingTuples, "\n")
    trainingList = convert_tuple_into_list(trainingTuples)
    print("\nSTE 68 trainingList: ", trainingList, "\n")
    trainingSets = trainingList # actually, a list
    txt_edit.insert(tk.END, trainingSets)
    print("\nSTE 70 trainingSets: ", trainingSets, "\n")
    window.title(f"BuildABear trainingFiles")
    
def run_harvest():
    global argv
    """ run the calculation """
#    sys.argv = [script_path, trainingSets, "-t ", targetFile]
    print("STE 73 - run() script_path: ", script_path)
    print("STE 74 - run() trainingSets: ", trainingSets)
    print("STE 75 - run() targetFile: ", targetFile)
    window.title(f"Calculations")
    sys.argv = [script_path, trainingSets, "-t", targetFile]
    print("\nSTE 77 -  run() sys.argv: ", sys.argv, "\n")
    print("running...")

    text = txt_edit.get(1.0, tk.END)
    txt_edit.replace(1.0, tk.END, "Running the calculation.")
    timeStart = time.time()
    harvest.run_harvest_orig()
    print("Finished...")
    timeEnd = time.time()
    elapsedTime = int(timeEnd-timeStart)

    result = "Finished the calculation in ", str(elapsedTime) , " seconds"
    txt_edit.replace(1.0, tk.END, result)
    
def open_text_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt")]
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
    with open(filepath, "r") as output_result_file:
        text = output_result_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Result - {filepath}")
    
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
    
def quit():
    """ quit the program """
    window.destroy()
    
window = tk.Tk()
window.title("Simple Text Editor => BuildABear")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, fg = "blue")
txt_edit_run = tk.Text(window, font = ('Comic Sans MS',30) )
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

style = ttk.Style()
style.configure('Dave.TButton', foreground='blue')

btn_load_script = ttk.Button(fr_buttons, text="1. Select Python Script...", command=select_python_script, style='Dave.TButton')
btn_open_target = ttk.Button(fr_buttons, text="2. Select Target...", command=open_target_file, style='Dave.TButton')
btn_open_training = ttk.Button(fr_buttons, text="3. Select Training Files (with ⌘-click) ...", command=open_training_files, style='Dave.TButton')
btn_run = ttk.Button(fr_buttons, text="4. Run the calculation", command=run_harvest, style='Dave.TButton')
btn_open_text_files = ttk.Button(fr_buttons, text="Display a Text File...", command=open_text_file)
btn_open_result = ttk.Button(fr_buttons, text="Open Result File...", command=open_result_file)
btn_quit = ttk.Button(fr_buttons, text="Quit", command=quit)

btn_load_script.grid(row=0, column=0, sticky="EW", padx=5, pady=10)
btn_open_target.grid(row=1, column=0, sticky="EW", padx=5, pady=10)
btn_open_training.grid(row=2, column=0, sticky="EW", padx=5, pady=10)
btn_run.grid(row=3, column=0, sticky ="EW", padx=5, pady=10)
btn_open_text_files.grid(row=4, column=0, sticky="EW", padx=5, pady=10)
btn_open_result.grid(row=5, column=0, sticky="EW", padx=5, pady=10)
btn_quit.grid(row=6, column=0, sticky ="EW", padx=5, pady=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()