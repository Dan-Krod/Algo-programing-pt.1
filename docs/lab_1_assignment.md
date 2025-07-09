# Lab Assignment 1: Python Environment & Basic Programming

## 🎯 Topic
Virtual Environment Setup, Package Management, HTTP Requests, and Basic Python Programming

## 📌 Goal
Familiarize students with Python's virtual environments, learn to manage packages, write and execute Python scripts, use the `requests` library for HTTP interactions, and apply logical and mathematical operations in Python.

## 📂 Project Structure
All related code is located in the project’s root `code` folder, inside the subdirectory:

```
code/lab_1/
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
      <td><code>task_1.py</code></td>
      <td>Script for activating and testing virtual environment</td>
    </tr>
    <tr>
      <td><code>task_2.py</code></td>
      <td>Shows installed packages using <code>pip list</code></td>
    </tr>
    <tr>
      <td><code>task_3.py</code></td>
      <td>Exports installed packages to <code>requirements.txt</code></td>
    </tr>
    <tr>
      <td><code>task_4.py</code></td>
      <td>Script performing an HTTP request using the <code>requests</code> lib</td>
    </tr>
    <tr>
      <td><code>task_5.py</code></td>
      <td>Script demonstrating logical and boolean operations</td>
    </tr>
    <tr>
      <td><code>task_6.py</code></td>
      <td>Script for computing a mathematical expression using <code>math</code></td>
    </tr>
    <tr>
      <td><code>requirements.txt</code></td>
      <td>File generated from <code>pip freeze</code> output</td>
    </tr>
  </tbody>
</table>

> ⚠️ All Python scripts must be placed directly in `code/lab_1/` and named exactly as shown above.

---

## ✅ Tasks (Total: 6)

### Part 1 – Environment & HTTP Request
1. **Activate Virtual Environment**  
   Use `python -m venv venv` to create and activate your environment.

2. **Check Installed Packages**  
   Run `pip list` to display current packages.

3. **Export Requirements**  
   Generate a `requirements.txt` file using `pip freeze > requirements.txt`.

4. **Write Python Script with HTTP Request**  
   - Use `requests.get(url)` to perform a GET request.
   - Store this code in `part1_script.py`.
   - URL example: https://uakino.club/filmy/genre-action/1-temnyi-lycar.html

5. **Execute Script**  
   Run the script and observe the printed response content. (Expected: a `404 Not Found` response confirms the request executed.)

### Part 2 – Logic & Math Programming
6. **Write Logic & Math Programs According to Variant 6**
   - `part2_logic.py` should define:
     - `car = "Ford Mustang"` and print it
     - `is_student = True`, `is_teacher = False` with logical operations
     - `is_red = True`, `is_blue = True` with boolean OR
   - `part2_math.py` should implement:
     - For `y = 6.153`, `z = 1.001`, compute  
       \[
       \tan(\cos(z)) + \frac{4 \cdot \sin(z)}{\cos(y)} + \sqrt{z \cdot y}
       \]
     - Use the `math` module
