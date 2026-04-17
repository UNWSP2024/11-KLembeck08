# ------------------------------------------------------------
# Author: Kael
# Date: April 17, 2026
# Title: Favorite Saying GUI
# ------------------------------------------------------------

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Favorite Saying")

# Create a label with your favorite saying
saying_label = tk.Label(window, text="The only limit to our realization of tomorrow is our doubts of today.",
                        font=("Arial", 16), padx=20, pady=20)
saying_label.pack()

# Run the GUI loop
window.mainloop()
