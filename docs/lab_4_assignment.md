# Lab Assignment 4: Object-Oriented Programming — Class Zoo

## 🎯 Topic

Encapsulation, Object Construction and Destruction, and String Representation Using Python Classes  
(Laboratory Work #4, Variant 6)

## 📌 Goal

- Understand and apply the core concepts of Object-Oriented Programming (OOP) in Python.
- Define a class that represents a real-world entity based on a table of attributes.
- Implement visibility modifiers (private and public attributes), getter and setter methods, and magic methods such as `__init__`, `__del__`, `__str__`, and `__repr__`.
- Practice instantiating objects using both default and parameterized constructors.
- Output object data using class methods and standard Python functions.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_4/
```

<table>
  <thead>
    <tr>
      <th>Filename</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>lab_4_class_zoo.py</code></td>
      <td>Contains the complete implementation of the <code>Zoo</code> class and test objects</td>
    </tr>
  </tbody>
</table>

⚠️ The Python script must be placed directly in `code/lab_4/` and named exactly as shown above.

## ✅ Tasks

1. Create a class `Zoo` that includes the following **private fields**:
   - `__visitors_per_year` (int)
   - `__name` (str)
   - `__animal_count` (int)

2. Add **two public fields**:
   - One numerical field (e.g., `public_species_amount`)
   - One string field (e.g., `public_animal_species`)

3. Write **getter and setter methods** for each private field:
   - Example: `get_name()`, `set_name(new_name)`, etc.

4. Override these **magic methods** in your class:
   - `__str__` for user-friendly text output
   - `__repr__` for developer-style object display
   - `__del__` to indicate object destruction

5. Implement:
   - A **default constructor** that assigns initial values
   - A **parameterized constructor** that accepts all values for initialization

6. Inside a `main()` function:
   - Create and initialize at least **three Zoo objects**
   - Output all field values using getter methods and print statements

7. Call `repr()` on each object and display the result.
8. Ensure the destructor message is shown when objects are deleted or the program ends.

---

📎 *Covers core OOP techniques in Python through class-based modeling, encapsulation, and object behavior management.*
