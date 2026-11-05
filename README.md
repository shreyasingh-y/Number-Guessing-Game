# 🎮 Number Guessing Game (Python 3)

**Course:** Bachelor of Computer Application (BCA)  
**University:** Rungta International Skills University  
**School:** School of Information Technology  
**Project ID:** PS No. 98  
**Academic Session:** 2026-27  

---

## 👤 Student & Submission Details

- **Student Name:** Shreya Singh
- **ERP Number:** RU-26-04631
- **Section:** B
- **Submitted To:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

---

## 📌 Project Overview

The **Number Guessing Game** is a console-based interactive Python application. The computer assigns a secret number (fixed to `42` for testing compliance), and the player has a maximum of **5 attempts** to guess the correct number while receiving dynamic hints (`Too high` or `Too low`).

---

## 🚀 Features & Rules

1. **Fixed Secret Number for Testing:** Set to `42` as per testing criteria.
2. **Attempt Control:** Player gets exactly 5 attempts to guess the number.
3. **Input Validation:**
   - Non-numeric inputs (e.g., `abc`) trigger an invalid input warning without deducting attempts.
   - Out-of-range inputs (less than `1` or greater than `100`) prompt a range warning without deducting attempts.
4. **Interactive Hints:** Provides feedback (`Too low! Attempts left: X` / `Too high! Attempts left: X`) after every valid guess.
5. **Replay Functionality:** Option to play multiple rounds (`y/n`) after win or game over conditions.

---

## 🧪 Test Cases & Expected Outcomes

| Test Case | Scenario / Inputs | Expected Output |
| :--- | :--- | :--- |
| **Test Case 1: Normal Input** | Secret: 42<br>Guess: `42` | `Congratulations! You guessed it in 1 attempt.` |
| **Test Case 2: Boundary Inputs** | Secret: 42<br>Guesses: `1`, `100` | `Too low! Attempts left: 4`<br>`Too high! Attempts left: 3` |
| **Test Case 3: Invalid Inputs** | Secret: 42<br>Guesses: `abc`, `150` | `Invalid input. Enter a whole number.`<br>`Out of range. Enter a number between 1 and 100.`<br>*(No attempt lost)* |
| **Test Case 4: Exhausted Attempts** | Secret: 42<br>Guesses: `10`, `90`, `50`, `30`, `20` | Dynamic hints given for each attempt, concluding with:<br>`Game Over! The number was 42.` |

---

## 💻 How to Run the Program

1. Ensure Python 3 is installed on your system.
2. Clone or download the repository.
3. Open terminal/command prompt in the project directory.
4. Execute the Python script:

```bash
python one.py
```
