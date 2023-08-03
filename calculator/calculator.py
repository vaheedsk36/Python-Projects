import tkinter as tk

def on_button_click(button_text):
    current_text = result_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    else:
        result_var.set(current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Variable to hold the result
result_var = tk.StringVar()
result_var.set("")

# Create the result display
result_entry = tk.Entry(root, textvariable=result_var, font=("Helvetica", 24), bd=5, justify="right")
result_entry.pack(fill=tk.BOTH, expand=True)

# Create the buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for row in buttons:
    button_row = tk.Frame(root)
    button_row.pack(fill=tk.BOTH, expand=True)
    for button_text in row:
        button = tk.Button(button_row, text=button_text, font=("Helvetica", 20), bd=3,
                           command=lambda text=button_text: on_button_click(text))
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
