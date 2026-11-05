# ==========================================================
# 🎯 PROJECT TITLE : NUMBER GUESSING GAME (PS NO: 98) 🎮
# 🏫 UNIVERSITY    : RUNGTA INTERNATIONAL SKILLS UNIVERSITY 🎓
# 📚 PROGRAM       : BACHELOR OF COMPUTER APPLICATION (BCA) 💻
# 🛠️ LANGUAGE     : PYTHON 3 🐍
# ==========================================================

import random

def play_game():
    # ------------------------------------------------------
    # ⚙️ GAME INITIALIZATION & CONFIGURATION ⚙️
    # ------------------------------------------------------
    # For testing requirement, fixed secret number: 42
    # Standard implementation uses random: secret_number = random.randint(1, 100)
    secret_number = 42
    max_attempts = 5
    attempts_left = max_attempts
    attempt_count = 0

    # ------------------------------------------------------
    # 🔁 MAIN GAME LOOP (MAX 5 ATTEMPTS) 🔁
    # ------------------------------------------------------
    while attempts_left > 0:
        user_input = input("Enter your guess: ").strip()
        
        # 🔍 STEP 1: VALIDATE INPUT (CHECK IF INTEGER)
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Enter a whole number.")
            continue
            
        guess = int(user_input)
        
        # 🔍 STEP 2: VALIDATE RANGE (1 TO 100)
        if guess < 1 or guess > 100:
            print("Out of range. Enter a number between 1 and 100.")
            print(f"Attempts left: {attempts_left} (no attempt lost)")
            continue
            
        # 🎯 STEP 3: PROCESS VALID GUESS
        attempt_count += 1
        attempts_left -= 1
        
        # 🏁 STEP 4: CHECK WIN OR GIVE HINT
        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempt_count} attempt{'s' if attempt_count > 1 else ''}.")
            break
        elif guess < secret_number:
            if attempts_left > 0:
                print(f"Too low! Attempts left: {attempts_left}")
            else:
                print("Too low")
        else:
            if attempts_left > 0:
                print(f"Too high! Attempts left: {attempts_left}")
            else:
                print("Too high")

    # ------------------------------------------------------
    # 💀 GAME OVER CONDITION 💀
    # ------------------------------------------------------
    if attempts_left == 0 and guess != secret_number:
        print(f"Game Over! The number was {secret_number}.")

def main():
    # ------------------------------------------------------
    # 🔁 PLAY AGAIN REPEAT LOGIC 🔁
    # ------------------------------------------------------
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
