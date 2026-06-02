# 💳 Credit Card Validator (Luhn Algorithm) in Python

A lightweight command-line utility written in Python that validates credit card numbers using the standard **Luhn Algorithm** (also known as the "Mod 10" algorithm). 

This script quickly verifies whether a given card number is syntactically valid by performing specific arithmetic checks on its digits.

---

## 🛠️ Requirements & Environment

* **Python Version:** Python 3.x (Fully compatible with Python 3.12+)
* **IDE/Editor:** VS Code, PyCharm, or any text editor of your choice.
* **Dependencies:** None! This project relies purely on built-in Python string manipulation and basic mathematical operations.

---

## 🧠 How the Algorithm Works

The program processes the input card number using the following 5-step validation mechanism:

1. **Sanitization:** Removes any accidental or formatted spaces (` `) or hyphens (`-`) and reverses the string to easily calculate positions from right to left.
2. **Odd-Placed Digits:** Sums up all the digits sitting in the **odd positions** (1st, 3rd, 5th, etc.) counting from right to left.
3. **Even-Placed Digits:** Identifies digits in the **even positions** (2nd, 4th, 6th, etc.) from right to left, doubles them, and adds the resulting digits together if the doubled product is a two-digit number (e.g., $14 \rightarrow 1 + 4 = 5$).
4. **Total Summation:** Adds the final totals of both the odd and even position calculations together.
5. **Mod 10 Check:** If the grand total is perfectly divisible by 10 (`total % 10 == 0`), the card number is flagged as **Valid**; otherwise, it is **Invalid**.

---


