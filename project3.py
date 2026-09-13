from tkinter import *

# Create the main window
root = Tk()
root.geometry("400x300")
root.setTitle = "Getting Started with Widgets" # Alternative: root.title("Getting Started with Widgets")
root.config(bg="#f0f8ff")

# Function to calculate the product
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        
        # Display the result in the Text box
        text_box.delete("1.0", END)
        text_box.insert(END, f"The product is: {result}")
    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Please enter valid numbers!")

# 3. Add a label to describe the functionality of this application
desc_label = Label(root, text="Product Calculator", bg="#f0f8ff", font=("Arial", 14, "bold"))
desc_label.pack(pady=10)

# 4. Add two labels for asking users to enter numbers
label1 = Label(root, text="Enter first number:", bg="#f0f8ff")
label1.pack()

# 5. Add two Entry widgets below the labels
entry1 = Entry(root)
entry1.pack(pady=5)

label2 = Label(root, text="Enter second number:", bg="#f0f8ff")
label2.pack()

entry2 = Entry(root)
entry2.pack(pady=5)

# 6. Add a button that will calculate the product when clicked
calc_button = Button(root, text="Calculate Product", command=calculate_product, bg="#4CAF50", fg="white")
calc_button.pack(pady=10)

# 7. Add a Text Box to display the result
text_box = Text(root, height=3, width=30)
text_box.pack(pady=5)

root.mainloop()