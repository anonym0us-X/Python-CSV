# Python CSV Practice

This repository contains basic practice examples for working with CSV files in Python.

---

## 📌 What This Project Covers

- Creating CSV files
- Writing rows using `csv.writer`
- Understanding file modes (`r`, `w`, `a`)
- Fixing newline issues

---

# 🐍 Writing to a CSV File (Create or Overwrite)

```python
import csv

data = [
    ["language", "creator", "year"],
    ["Python", "Guido van Rossum", 1991],
    ["C", "Dennis Ritchie", 1972],
    ["C++", "Bjarne Stroustrup", 1985],
    ["Java", "James Gosling", 1995],
    ["JavaScript", "Brendan Eich", 1995],
]

with open("lang.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
