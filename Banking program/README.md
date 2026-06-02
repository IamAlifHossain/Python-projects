# Simple Python Banking Program

A lightweight, console-based banking application written in Python. This program simulates basic ATM/banking operations such as checking account balances, making secure deposits, and processing withdrawals with built-in validation rules.

---

## Requirements

To run this program, you only need a standard Python environment setup:

* **Python Version:** Python 3.x (Fully compatible with Python 3.12+)
* **Editor:** Any text editor (Visual Studio Code recommended)
* **Dependencies:** None! This project uses pure, built-in Python standard libraries.

---

## Features & Validation Rules

The program operates in a continuous loop until explicitly exited, offering the following functionalities:

1. **See Balance:** Displays the current account balance formatted to two decimal places in Bangladeshi Taka (**BDT**).
2. **Deposit:** * Allows users to add funds to their account.
   * *Validation:* Prevents entering negative amounts or zero.
3. **Withdraw:** * Allows users to deduct funds from their account.
   * *Validation:* Prevents overdrafts (insufficient funds) and rejects negative/zero inputs.
4. **Exit:** Safely terminates the banking session with a departure message.


