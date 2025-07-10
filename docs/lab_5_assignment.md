# Lab Assignment 5: Dream Room Simulation Using Object-Oriented Design

## 🎯 Topic

Custom Object Modeling, Positioning, and Rearrangement Using Python Classes  
(Laboratory Work #5, Variant 6)

## 📌 Goal

- Design and implement a program simulating a dream room using object-oriented programming principles.
- Create classes representing room furniture (e.g. bed, table, carpet) with position and size attributes.
- Manage object positioning, rearrangement, and removal through encapsulated methods.
- Practice implementing class constructors, destructors, accessor methods, and object collection handling.
- Demonstrate functionality via a structured `main()` method.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_5/
```

| Filename      | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `lab_5.py`    | Full implementation of `Furniture` and `Room` classes with main logic       |

⚠️ The Python script must be placed directly in `code/lab_5/` and named exactly as shown above.

## ✅ Tasks

1. Define a class `Furniture` with the following attributes:
   - `name`: the name of the object (e.g. "Bed", "Carpet")
   - `coordinates`: list of 2 integers, representing object location in the room
   - `size`: list of 2 integers, representing object size (width × height)

2. Define a class `Room` with:
   - Attribute `size_room`: overall room dimensions
   - A list to store all added furniture objects

3. Implement the following methods in `Room`:
   - `add_object(furniture)`: adds object if it fits within room bounds
   - `remove_object(furniture)`: removes furniture if it exists
   - `rearrangement(object_name, new_coordinates)`: changes position of an existing object if valid
   - `check_size(furniture)`: internal check if the object fits the room
   - `find_object(name)`: retrieves object from the list by name
   - `display_info()`: prints out details of all room objects

4. Ensure that:
   - Each furniture object is represented with a `__str__()` method
   - `main()` function demonstrates full workflow: room creation, object addition, rearrangement, deletion

---

📎 Practical application of OOP principles using custom Python classes to manage spatial objects, their properties, and dynamic interactions in a simulated environment.
