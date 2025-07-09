# Lab Assignment 7: Exception Handling and Logging with Custom Decorators

## 🎯 Topic

Custom Exception Classes and Parameterized Logging Decorators in Python  
(Laboratory Work #7, Variant 6)

## 📌 Goal

- Integrate exception handling into an object-oriented Python program.
- Define and raise custom exceptions to reflect domain-specific errors.
- Create a parameterized decorator `@logged` that logs exceptions in different modes: `"console"` or `"file"`.
- Utilize the `logging` module to handle real-time event monitoring.
- Modify and extend the Room & Furniture code from Lab 5 to include decorated methods with exception handling.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_7/
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
      <td><code>lab_7_exceptions_logged.py</code></td>
      <td>Main Python file with Room and Furniture classes updated with custom exceptions and decorator logic</td>
    </tr>
    <tr>
      <td><code>error_log.txt</code></td>
      <td>Log file used for recording exceptions in "file" mode</td>
    </tr>
  </tbody>
</table>

⚠️ All Python scripts must be placed directly in `code/lab_7/` and named exactly as shown above.

## ✅ Tasks

1. Reuse and adapt the code from Lab 5, extending the `Room` and `Furniture` classes.

2. Define at least one custom exception by subclassing `Exception`, for example:
   - `SizeExceededException`
   - `ObjectNotExistException`

3. Create a parameterized decorator `@logged(exception, mode)` with:
   - `exception`: the custom exception class to catch
   - `mode`: `"console"` or `"file"` to control the output destination

4. When a decorated method raises the given exception:
   - If `mode == "console"`: log the message to terminal via `logging.error()`
   - If `mode == "file"`: append the error message to `error_log.txt`

5. Apply the decorator to methods like `add_object()` and `remove_object()` to enforce exception-based logic.

6. Demonstrate full functionality in `main()`:
   - Raise and log both handled and unhandled exceptions
   - Show how decorator behavior changes based on mode
   - Use `print()` and `display_info()` to visualize the room state

---

📎 Practical use of exceptions and decorators to enforce business logic and maintain traceable program behavior across runtime scenarios.