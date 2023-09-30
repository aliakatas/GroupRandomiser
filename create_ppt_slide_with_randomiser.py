import tkinter as tk
from tkinter import ttk
import random
from pptx import Presentation

####################################
def append_to_powerpoint(pptx_file, txt, mod_pptx_file=None):
    # Load the PowerPoint presentation
    presentation = Presentation(pptx_file)

    # Create a new slide with a title and content layout
    slide_layout = presentation.slide_layouts[5]  # 5 corresponds to Title and Content layout
    new_slide = presentation.slides.add_slide(slide_layout)

    # Set the title and content for the new slide
    title = new_slide.shapes.title
    title.text = "Random Grouping!"

    content = new_slide.placeholders[1]  # Placeholder for content
    content.text = txt

    if mod_pptx_file is not None:
        # Save the modified presentation
        presentation.save(mod_pptx_file)

####################################
def create_random_groups(n, group_size, allow_less=False):
    names = [f'{i + 1}' for i in range(n)]

    groups = list()
    if group_size > n:
        return groups

    while n >= group_size:
        group = list()
        for i in range(group_size):
            name = random.choice(names)
            group.append(name)
            names.remove(name)
        
        groups.append(group)
        n = len(names)
    
    if allow_less:
        groups.append(names)
    else:
        n_rem = len(names)
        for i in range(n_rem):
            group = random.choice(groups)
            group.append(names[i])
    
    return groups

# Function to calculate results based on input values
def calculate_results():
    # Get the input values as strings
    num_of_students_val = num_of_students.get()
    num_students_group_val = num_students_group.get()
    allow_less_in_group_val = allow_less_in_group.get()

    # Convert input values to float (you can add error handling)
    num_of_students_val = int(num_of_students_val)
    num_students_group_val = int(num_students_group_val)
    allow_less_in_group_val = int(allow_less_in_group_val) > 0

    # Process inputs
    groups = create_random_groups(num_of_students_val, num_students_group_val, allow_less=allow_less_in_group_val)

    # Display the results in the table
    result_table.delete(*result_table.get_children())  # Clear existing rows
    slide_txt = ""
    for idx, group in enumerate(groups):
        result_table.insert("", "end", values=(f"Group {idx + 1} ({len(group)})", group))
        slide_txt += f"Group {idx + 1} ({len(group)}) \t\t {group}"

####################################
def save():
    pass 

# Create the main application window
root = tk.Tk()
root.title("Simple Randomiser")

# Create labels and entry widgets for input values
label1 = tk.Label(root, text="Number of students:")
label1.pack()
num_of_students = tk.Entry(root)
num_of_students.pack()

label2 = tk.Label(root, text="Number of students in group:")
label2.pack()
num_students_group = tk.Entry(root)
num_students_group.pack()

# Create a checkbox for on-off control
allow_less_in_group = tk.IntVar()  # Variable to hold the checkbox state (0 or 1)
checkbox = tk.Checkbutton(root, text="Allow less in group", variable=allow_less_in_group)
checkbox.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_results)
calculate_button.pack()

# Create a button to trigger saving
save_button = tk.Button(root, text="Save", command=save)
save_button.pack()

# Create a table to display the results
columns = ("Description", "Result")
result_table = ttk.Treeview(root, columns=columns, show="headings")
result_table.heading("Description", text="Description")
result_table.heading("Result", text="Result")
result_table.pack()

# Run the application
root.mainloop()
