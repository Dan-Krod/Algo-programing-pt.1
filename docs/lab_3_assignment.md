# Lab Assignment 3 : Custom Like Text Generator

## 🎯 Topic

Generating “Like” Text Based on Input Names Using Custom Conditional Logic  
(Laboratory Work #3, Variant 6)

## 📌 Goal

- Implement three different variants of the `like()` function that generate formatted strings simulating social media "like" behavior.
- Practice conditional logic, list processing, and string formatting in Python.
- Avoid using built-in shortcuts (e.g. `reverse()`, `join()`); implement all logic manually.
- Compare and document implementation strategies across all three variants.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_3/
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
      <td><code>variant_1.py</code></td>
      <td>Function-based solution with multiple if-branches</td>
    </tr>
    <tr>
      <td><code>variant_2.py</code></td>
      <td>Interactive <code>input()</code>-based implementation</td>
    </tr>
    <tr>
      <td><code>variant_3.py</code></td>
      <td>Compact return expression using nested <code>if</code></td>
    </tr>
  </tbody>
</table>

⚠️ All Python scripts must be placed directly in `code/lab_3/` and named exactly as shown above.

## ✅ Tasks

Each implementation must support the following logic:

- `[]` → `"no one likes this"`
- `["Peter"]` → `"Peter likes this"`
- `["Jacob", "Alex"]` → `"Jacob and Alex like this"`
- `["Max", "John", "Mark"]` → `"Max, John and Mark like this"`
- `["Alex", "Jacob", "Mark", "Max"]` → `"Alex, Jacob and 2 others like this"`
- For 5+ names: show `"{first}, {second} and N others like this"`

### Constraints

- Do **not** use built-in functions like `reverse()`, `join()`, slicing `[::-1]`, etc.
- Each script should include embedded test cases:
  ```python
  print(like([]))
  print(like(["Peter"]))
  ...
  ```
- Input must **not** be modified inside the function.

---

📎 *This lab showcases your ability to write flexible formatting logic using only fundamental Python tools. The different variants illustrate various programming styles and interaction methods.*
