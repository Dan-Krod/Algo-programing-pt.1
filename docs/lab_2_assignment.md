# Lab Assignment 2: Function tabulation using conditional logic and power series expansion 

## 🎯 Topic

Conditional Logic-Based Function Evaluation and Series Approximation in Python

## 📌 Goal

- Develop block diagrams and Python scripts to tabulate two types of mathematical functions.
- Analyze and visualize function values over a specified interval with defined step `h`:
  - **Part 1**: Tabulate a function based on conditional logic (Table 1).
  - **Part 2**: Tabulate a function represented as an infinite series (Table 2) with absolute error control.

## 📂 Project Structure

All related code is located in the project’s root code folder, inside the subdirectory:

```
code/lab_2/
```

| Filename         | Description                                 |
|------------------|---------------------------------------------|
| `task_1.py`       | Conditional function tabulation (Table 1)   |
| `task_2.py`       | Power series function tabulation (Table 2)  |

⚠️ All Python scripts must be placed directly in `code/lab_2/` and named exactly as shown above.

## ✅ Tasks

### Part 1: Tabulation Based on Argument Value

- Use the function from **Table 1 (Variant 6)**:
  - 📈 Interval: `[0.5, 0.8]`
  - 📏 Step: `0.02`
  - 🧮 Apply conditional branching logic to select a function based on `x`

### Part 2: Series Expansion with Accuracy Control

- Use the function from **Table 2 (Variant 6)**:
  - 📈 Interval: `[-1, 1]`
  - 📏 Step: `0.5`
  - 🎯 Absolute error threshold: `d = 0.001`
  - 💡 Include logic to sum terms of the series until the next term is less than `d` by absolute value

---

📎 *Make sure your code outputs each `x` and corresponding function result clearly, and includes “Done :)” at the end of execution for both parts.*
```