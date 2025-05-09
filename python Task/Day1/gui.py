import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import joblib
import numpy as np

# Load the trained KNN model
model = joblib.load("knn_model.pkl")  # Make sure this file exists

# Create the main GUI window
root = tk.Tk()
root.title("🌸 Iris Flower Classifier")
root.geometry("400x450")
root.configure(bg="#f0f8ff")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12), background="#f0f8ff")
style.configure("TButton", font=("Segoe UI", 12), padding=6)
style.configure("TEntry", font=("Segoe UI", 12))

# Heading
heading = ttk.Label(root, text="Iris Flower Predictor 🌼", font=("Segoe UI", 16, "bold"))
heading.pack(pady=10)

# Function to predict species
def predict_species():
    try:
        # Get input values
        sl = float(entry_sepal_length.get())
        sw = float(entry_sepal_width.get())
        pl = float(entry_petal_length.get())
        pw = float(entry_petal_width.get())

        features = np.array([[sl, sw, pl, pw]])
        prediction = model.predict(features)
        predicted_label.set(f"Predicted Species: 🌺 {prediction[0]}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Input Fields
def create_input_field(label_text):
    frame = tk.Frame(root, bg="#f0f8ff")
    frame.pack(pady=5)
    label = ttk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=10)
    entry = ttk.Entry(frame, width=20)
    entry.pack(side=tk.RIGHT, padx=10)
    return entry

entry_sepal_length = create_input_field("Sepal Length:")
entry_sepal_width  = create_input_field("Sepal Width:")
entry_petal_length = create_input_field("Petal Length:")
entry_petal_width  = create_input_field("Petal Width:")

# Predict Button
ttk.Button(root, text="Predict 🌿", command=predict_species).pack(pady=15)

# Label to show result
predicted_label = tk.StringVar()
prediction_display = ttk.Label(root, textvariable=predicted_label, foreground="green", font=("Segoe UI", 13, "bold"))
prediction_display.pack(pady=10)

# Start the GUI
root.mainloop()
