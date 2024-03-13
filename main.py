import tkinter as tk

def stop_text_input():
    text_widget.config(state=tk.DISABLED)
def get_text():
    text = text_widget.get("1.0", "end")
    text_list = text.split()
    num_of_words = len(text_list)
    print(f'Your WPM is {num_of_words}')
    show_result_window(num_of_words)

def show_result_window(num_of_words):
    # Create a new window
    global result_window
    result_window = tk.Toplevel(win)
    result_window.title("Result")
    result_window.geometry("200x100")

    result_label = tk.Label(result_window, text=f"Words_per_Minute: {num_of_words}")
    result_label.pack()

    restart_button = tk.Button(result_window, text="Restart Typing", command=restart_typing)
    restart_button.pack()

    quit_button = tk.Button(result_window, text="Quit", command=quit_application)
    quit_button.pack()

def restart_typing():
    result_window.destroy()
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)

def quit_application():
    win.destroy()


# Create the main window
win = tk.Tk()
win.geometry("800x600")
win.title("Typing Speed calculator")

# Create a Canvas widget
canvas = tk.Canvas(win, width=800, height=500, bg="white")
canvas.pack()

# Create a Text widget
text_widget = tk.Text(canvas, width=60, height=17)
canvas.create_window(250, 150, window=text_widget, anchor='center')

# Create a button to get the text
get_text_button = tk.Button(win, text="Get Result", command=get_text)
get_text_button.pack()


win.after(60000, stop_text_input)

# Run the main event loop
win.mainloop()







