import Smart_Print as sp #Smart print file
import FP_inventory as inv #inventory file
import sys #To kil/exit game
import time as t #Used to give user time to read the story
import Lawyer_Choice as LC # Lawyer choices file
import Robber_Choice as RC # Robber choices file

# ANSI escape codes
ITALICS = '\x1b[3m'
RESET = '\x1b[0m'

# --- 1. GAME START ---
User_Name = input("Enter your name: ") #User Name
sp.smart_print(f"Your name will be ~{User_Name}~ for the rest of the game.")

sp.ancestry_check(User_Name) # Age Check

Story = input("Do you want to start the story? (yes/no): ") #Story initialization

if Story.lower() == "no":
    input("Press Enter to exit the game.")
    sys.exit(1)
elif Story.lower() == "yes":
    print("Game Starting...")
    t.sleep(4)
else:
    print("I AINT PLAYIN' THESE GAMES!")
    sys.exit(1)

# --- 2. SETUP INVENTORY ---
#Only happens if the Game start was completed (yes)
#Put here so the game doesn't create an empty txt file for no reason
inv.initialize_inventory_system()

# --- 3. STORY INTRO ---
sp.smart_print(f"Welcome {User_Name}! This is a lovely adventure game about life choices.") 
sp.smart_print("This story is set in America, in the late 1800's.")
sp.smart_print("Now for your very first life choice, you are going to pick your most important choice.")
Choice_1 = input(f"{User_Name}! Would you like to go to school? (yes/no): ")

# --- 4. PATH SELECTION ---
if Choice_1 == "yes":
    # --- LAWYER PATH ---
    LC.lawyer_Intro(User_Name) #Passing User_Name for namiing the user
    my_strategy = LC.lawyer_Choice_1(User_Name)#...
    score = LC.cross_examine_witnesses(my_strategy, User_Name)#Passing Strategy and User_Name
    LC.closing_statements(score, my_strategy, User_Name)#Passing Strategy, User_Name, and Score

elif Choice_1 == "no":
    # --- ROBBER PATH ---
    RC.robber_Intro(User_Name) #Passing User_Name for namiing the user
    heist_plan = RC.robber_Choice_1(User_Name) #...
    heist_score, plan_type_used = RC.execute_heist(heist_plan, User_Name) #Passing User_Name and hiest_plan
    RC.escape_result(heist_score, plan_type_used, User_Name)#Passing User_Name, hiest_score, and plan_type_used