# ------------------------------------------------------------
# Author: Kael
# Date: April 17, 2026
# Title: Show Info GUI Program
# ------------------------------------------------------------

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("User Info Display")

# Function to show name + fictional address
def show_info():
    info_label.config(text="Kael\n1234 Imaginary Lane\nRoseville, MN 55113")

# Create widgets
info_label = tk.Label(window, text="", font=("Arial", 14), pady=10)
show_button = tk.Button(window, text="Show Info", command=show_info, width=15)
quit_button = tk.Button(window, text="Quit", command=window.quit, width=15)

# Layout
info_label.pack()
show_button.pack(pady=5)
quit_button.pack(pady=5)

# Run the GUI loop
window.mainloop()
