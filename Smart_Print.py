import time as t 
import datetime

# Used to give user time to read the story
def smart_print(text):
    """
    Custom print function that adds a dynamic delay after printing text.
    This ensures the user has enough time to read the output before the next block of text appears.
    """
    print(text)
    
    # Calculate wait time based on text length:
    # - Multiplies the number of characters by 0.035 seconds.
    # - Uses max() to ensure that even very short strings have a minimum wait of 2 seconds.
    wait_time = max(2, len(text) * 0.035) 
    
    # Pauses the program execution for the calculated duration.
    t.sleep(wait_time)

def ancestry_check(User_Name):
    """
    Calculates the user's age and determines their generational relationship
    to the events of 1889.
    
    """
    current_year = datetime.datetime.now().year
    butch_trial_year = 1889
    avg_generation_gap = 23

    while True:
        try:
            birth_year_str = input(f"\nQuick check, {User_Name}. What year were you born? ")
            birth_year = int(birth_year_str)
            
            # Age Calculation
            user_age = current_year - birth_year
            
            # Ancestry Arithmetic
            years_since_trial = birth_year - butch_trial_year
            
            if years_since_trial < 0:
                smart_print(f"Wow, you are {user_age} years old! You're older than the story itself!")
                break
                
            # Arithmetic: Calculate generations
            generations_passed = int(years_since_trial / avg_generation_gap)
            
            print(f"\nAh, so you are roughly {user_age} years old.")
            print(f"Since the game is set in {butch_trial_year}, that is about {generations_passed} generations ago.")
            
            # String Logic for Titles
            if generations_passed <= 0:
                 ancestor_title = "YOU"
            elif generations_passed == 1:
                 ancestor_title = "your Parents"
            elif generations_passed == 2:
                 ancestor_title = "your Grandparents"
            else:
                num_greats = generations_passed - 2
                ancestor_title = "your " + ("Great-" * num_greats) + "Grandparents"

            smart_print(f"That means the people standing in this courtroom could have been {ancestor_title}!")
            print("-" * 40)
            break
            
        except ValueError:
            print("Please enter a valid 4-digit year (e.g., 2003).")

