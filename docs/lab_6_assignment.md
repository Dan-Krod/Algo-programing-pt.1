# Lab Assignment 6: Unit Testing & Code Style Validation in Python

## 🎯 Topic

Testing Class Behavior with PyTest and Enforcing PEP8 Compliance with PyLint  
(Laboratory Work #6, Variant 6)

## 📌 Goal

- Explore fundamental principles of software testing by writing unit tests for custom Python classes.
- Cover all class methods with automated tests using the `pytest` framework.
- Practice fixture usage, assertions, and parameterization to verify code correctness.
- Analyze and improve code quality using `pylint` to ensure full compliance with PEP8.
- Achieve a PyLint score of 10.00/10 as validation of code clarity and maintainability.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_6/
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
      <td><code>lab_5_code_doc_strings.py</code></td>
      <td>Modified version of Lab 5 with docstrings and clean PEP8 structure</td>
    </tr>
    <tr>
      <td><code>lab_6_tests.py</code></td>
      <td>PyTest test suite covering all methods of the Room and Furniture classes</td>
    </tr>
  </tbody>
</table>

⚠️ All Python scripts must be placed directly in `code/lab_6/` and named exactly as shown above.

## ✅ Tasks

1. **Prepare core logic**  
   Use the code from Lab 5 (`lab_5_code_doc_strings.py`) with improved docstrings and formatting.

2. **Create unit tests**  
   In `lab_6_tests.py`, write test functions to validate all public methods of:
   - `Furniture` class: initialization, `__str__`, `display_info()`
   - `Room` class: `add_object()`, `remove_object()`, `rearrangement()`, `find_object()`, `display_info()`, `check_size()`

3. **Use PyTest features**  
   - Define reusable fixtures for sample objects (e.g., `@pytest.fixture`).
   - Use assertions to verify correctness of outcomes and side effects.
   - Validate rearrangements, removals, and failure cases.

4. **Verify code style**  
   - Run `pylint lab_5_code_doc_strings.py` and eliminate all warnings/errors.
   - Achieve a final pylint score of **10.00/10**.

5. **Confirm output**  
   - Demonstrate that all test cases pass: `pytest lab_6_tests.py` returns ✅
   - Present final pylint report confirming clean code style.

---

📎 Reinforces Python testing practices and code quality assurance using PyTest and PyLint to ensure reliable, maintainable, and standards-compliant solutions.

