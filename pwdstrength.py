import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

def estimate_password_strength(password):
    # Password metrics weights
    length_weight = 1
    complexity_weight = 2
    unpredictability_weight = 3

    # Calculate password strength based on metrics
    length_score = min(1, len(password) / 12)
    complexity_score = bool(re.search(r'[A-Z]', password)) + bool(re.search(r'[a-z]', password)) + bool(re.search(r'[0-9]', password)) + bool(re.search(r'[!@#$%^&*()\-_=+[{\]}\\|;:\'",<.>/?]', password))
    complexity_score /= 4
    unpredictability_score = 1 if not bool(re.search(r'(123|abc|password)', password.lower())) else 0

    # Calculate total strength score
    strength_score = (length_weight * length_score +
                      complexity_weight * complexity_score +
                      unpredictability_weight * unpredictability_score) / (length_weight + complexity_weight + unpredictability_weight)

    return strength_score

def check_password_strength():
    password = password_entry.get()
    strength_score = estimate_password_strength(password)
    
    if strength_score >= 0.75:
        messagebox.showinfo("Password Strength", "Strong Password!")
    elif strength_score >= 0.5:
        messagebox.showinfo("Password Strength", "Moderate Password.")
    else:
        messagebox.showinfo("Password Strength", "Weak Password. Consider improving it.")

# Create GUI
root = tk.Tk()
root.title("Password Strength Estimator-By vivek")

# Set window size and position it in the center of the screen
window_width = 1100
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Load and set the image background
image_path = r"C:\Users\VIVEK\OneDrive\Desktop\maxresdefault.jpg"  # Replace with the actual path to your image
background_image = Image.open(image_path)
background_image = background_image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Title label
title_label = tk.Label(root, text="Password Strength Estimator - By vivek", bg="white", fg="purple", font=("Comic Sans MS", 24, "bold"))
title_label.pack(pady=10)


# Load and display the image
image_path = r"C:\Users\VIVEK\OneDrive\Desktop\images (1).png"  # Replace with the actual path to your image
image = Image.open(image_path)
image = image.resize((200, 200))  # Adjust the size of the image
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image)
image_label.pack(pady=20)


# Password input
password_label = tk.Label(root, text="Enter your password:", font=("Helvetica", 12, "bold"), fg="white", bg="#007bff")
password_label.pack()
password_entry = tk.Entry(root, show="X", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333", relief=tk.FLAT,
                          highlightthickness=2, highlightcolor="cyan", highlightbackground="pink")
password_entry.pack(pady=5, ipadx=10, ipady=5)
# Check button
check_button = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#ff4500", fg="white", font=("Helvetica", 14, "bold"), relief=tk.RAISED, bd=0)
check_button.pack(pady=15, padx=80)

# Run the GUI main loop
root.mainloop()