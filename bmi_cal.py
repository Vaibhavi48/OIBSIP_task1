import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def check_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_and_show_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = calculate_bmi(weight, height)
    category = check_bmi_status(bmi)

    result_label.config(text=f"Your BMI is: {bmi:.2f}\nYour category is: {category}")

# New function to clear the entry fields
def clear_data():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

def main():
    global weight_entry, height_entry, result_label

    window = tk.Tk()
    window.title("BMI Calculator")
    
    window.geometry("400x300")
    
    font=('Adobe Myungjo Std',14)

    weight_label = tk.Label(window, text="Weight (kg):",font=font)
    weight_label.grid(row=0, column=0, padx=10, pady=10)

    height_label = tk.Label(window, text="Height (m):",font=font)
    height_label.grid(row=1, column=0, padx=10, pady=10)

    weight_entry = tk.Entry(window, bg="lightyellow", fg="black",font=font)
    weight_entry.grid(row=0, column=1, padx=10, pady=10)

    height_entry = tk.Entry(window, bg="lightyellow", fg="black",font=font)
    height_entry.grid(row=1, column=1, padx=10, pady=10)

    calculate_button = tk.Button(window, text="Calculate", command=calculate_and_show_bmi, bg="lightblue", fg="black",font=font)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # New clear button
    clear_button = tk.Button(window, text="Clear", command=clear_data, bg="lightcoral", fg="black",font=font)
    clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    result_label = tk.Label(window, text="", bg="lightgrey",font=font)
    result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
