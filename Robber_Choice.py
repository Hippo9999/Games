import FP_inventory as inv
import Smart_Print as sp
import time as t

ITALICS = '\x1b[3m'
RESET = '\x1b[0m'

def robber_Intro(User_Name):
    """
    Displays the introductory context for the Robber path.
    Sets the year (1889) and the goal (Bank Heist).
    """
    sp.smart_print(f"""
    {ITALICS}You chose NOT to go to school...{RESET}
    You chose the path of freedom. The path of the outlaw.
    
    You are {User_Name}. 
    It is June 24, 1889. You are sitting on your horse outside Telluride.
    The San Miguel Valley Bank is just down the street.
    """)
    sp.smart_print("What you have: a crew and saddlebags full of tools.")
    sp.smart_print("What you need: a plan to rob the bank and get away clean.")

def robber_Choice_1(User_Name):
    """
    Fills the inventory with Robber tools and asks the user to pick a heist plan.
    
    Returns:
        str: A keyword ('stealth', 'force', 'trickery', 'gentleman') representing the plan.
    """
    # 1. Fill Inventory with Robber Tools
    inv.fill_robber_inventory()
    sp.smart_print("\nYour saddlebags are packed with 30 different tools.")
    sp.smart_print("Open your inventory text file now to see what you have.")
    input("(Check your inventory file, then press Enter to begin the Heist...)")

    sp.smart_print("\nThe boys are waiting for your signal. How are we doing this?")
    print("1. 'The Ghost' (Stealth & Silence)")
    print("2. 'The Gunslinger' (Loud & Aggressive)")
    print("3. 'The Trickster' (Deception & Speed)")
    print("4. Or none of the above")
    print(f"{ITALICS}Remember that the plan you pick will decide what items you must use to succeed.{RESET}")
    print(f"{ITALICS}Each plan has only one specific set of items that work.{RESET}")

    while True:
        choice = input("\nWhat is the plan? (1/2/3/4): ").strip()
        
        if choice == "1":
            sp.smart_print(f"\n{ITALICS}Plan: The Ghost. We get in, we get out. No one hears a thing.{RESET}")
            print(f"{ITALICS}Any items you pick should follow the plan's style {RESET}")
            return "stealth"
        elif choice == "2":
            sp.smart_print(f"\n{ITALICS}Plan: The Gunslinger. We kick the door down and take what is ours.{RESET}")
            print(f"{ITALICS}Any items you pick should follow the plan's style {RESET}")
            return "force"
        elif choice == "3":
            sp.smart_print(f"\n{ITALICS}Plan: The Trickster. We confuse them and vanish before they know we were here.{RESET}")
            print(f"{ITALICS}Any items you pick should follow the plan's style {RESET}")
            return "trickery"
        elif choice == "4":
            sp.smart_print(f"\n{ITALICS}Plan: The Gentleman. Polite, professional, and prepared.{RESET}")
            sp.smart_print("We walk in, ask for the money, and leave before they realize they've been robbed.")
            print(f"{ITALICS}Any items you pick should follow the plan's style {RESET}")
            return "gentleman"
        else:
            print(f"Pick a plan, {User_Name}. 1, 2, 3, or 4.")

def execute_heist(plan_type, User_Name):
    """
    Manages the 3 stages of the heist (Entry, Vault, Escape).
    - Checks strategy ('plan_type') to determine correct tools.
    - Handles obstacles using an inner helper function.
    - Gives partial points (0.5) if the user fails once but gets it right on the second try.
    
    Returns:
        tuple: (score, plan_type)
    """
    score = 0
    sp.smart_print(f"\n--- THE HEIST BEGINS: Leader {User_Name} ---")
    
    # Define the winning tools for each plan
    strategies = {
        "stealth": ["Lockpick Set", "Stethoscope", "Telegraph Wire Cutters"],
        "force": ["Shotgun", "Stick of Dynamite", "Coil of Rope"],
        "trickery": ["Fake Sheriff Badge", "Map of the Bank", "Sleeping Gas Vial"],
        "gentleman": ["Colt .45 Revolver", "Empty Money Sack", "Sack of Horse Feed"]
    }
    
    winning_tools = strategies[plan_type]

    # Helper function for obstacles with RETRY LOGIC
    def handle_obstacle(obstacle_name, obstacle_desc, success_msg):
        nonlocal score # Allows modification of the 'score' variable in the outer function
        sp.smart_print(f"\nOBSTACLE: {obstacle_name}")
        sp.smart_print(obstacle_desc)
        
        # --- ATTEMPT 1 ---
        print("Check your inventory. What tool solves this problem?")
        tool_choice = input("Enter exact tool name: ").strip()
        current_inv = inv._read_file()
        
        success = False
        
        # Check Attempt 1
        if tool_choice in current_inv:
            inv.del_inventory(tool_choice, 1) # Consume item
            if tool_choice in winning_tools:
                sp.smart_print(f"\nSUCCESS! You used the {tool_choice}.")
                sp.smart_print(success_msg)
                score += 1
                success = True
            else:
                sp.smart_print(f"\nFAIL. You tried to use {tool_choice}... It didn't work!")
        else:
            sp.smart_print(f"\nFAIL. You dug for '{tool_choice}' but didn't have it!")

        # --- ATTEMPT 2 (If Attempt 1 failed) ---
        if not success:
            sp.smart_print(f"{ITALICS}The guards are getting suspicious! You have one split second to try something else!{RESET}")
            tool_choice_2 = input("Quick! Use another item: ").strip()
            current_inv = inv._read_file() # Re-read incase they used an item
            
            if tool_choice_2 in current_inv:
                inv.del_inventory(tool_choice_2, 1) # Consume item
                if tool_choice_2 in winning_tools:
                    sp.smart_print(f"\nPHEW! You managed to use the {tool_choice_2} just in time.")
                    sp.smart_print(success_msg)
                    score += 0.5 # Half points for being slow
                    success = True
                else:
                    sp.smart_print(f"\nCRITICAL FAIL. The {tool_choice_2} was useless!")
            else:
                sp.smart_print(f"\nCRITICAL FAIL. You don't have that item!")

        return success # Returns True if passed, False if caught

    # --- OBSTACLE 1: The Entry ---
    if plan_type == "stealth":
        desc = "The back door is locked tight. We can't break it down without noise."
        succ = "Click. The lock turns silently. You slip inside unseen."
    elif plan_type == "force":
        desc = "The Bank Teller looks up and reaches for the alarm bell!"
        succ = "BOOM! You fire a warning shot into the ceiling. Everyone hits the floor."
    elif plan_type == "trickery":
        desc = "A guard is blocking the front entrance. He looks bored."
        succ = "You flash the badge. He nods respectfully and lets 'Sheriff' pass."
    elif plan_type == "gentleman":
        desc = "We walk into the lobby. We need to control the room instantly, without firing a shot."
        succ = "The room freezes. The sight of the iron commands total silence."
    
    if not handle_obstacle("The Entry", desc, succ): return -1, plan_type 


    # --- OBSTACLE 2: The Vault ---
    # 1. SETUP DESCRIPTIONS
    if plan_type == "stealth":
        desc = "The massive iron safe is locked. We need to listen to the tumblers to find the code."
        succ = "You place the Stethoscope against the metal and listen intently..."
    elif plan_type == "trickery":
        desc = "The safe is locked. We need the manufacturer's override code from the blueprints."
        succ = "You unfurl the Map of the Bank to find the emergency override..."
    elif plan_type == "force":
        desc = "The safe is too thick to drill. We need to blow it open NOW."
        succ = "KA-BLAM! The door flies off its hinges. The gold is exposed."
    elif plan_type == "gentleman":
        desc = "The teller is trembling. We need him to hand over the gold, conveniently packaged."
        succ = "The teller obeys, filling the sack to the brim. The gold is secured."

    # 2. EXECUTE TOOL CHECK (Applies to ALL plans now)
    # This ensures the item is checked, removed, and scored BEFORE the puzzle starts.
    if not handle_obstacle("The Vault", desc, succ): 
        return -1, plan_type

    # 3. TRIGGER PUZZLE (Only for Stealth/Trickery)
    if plan_type in ["stealth", "trickery"]:
        vault_label = "PINKERTON"
        sp.smart_print(f"\nYou found the manufacturer's label: '{vault_label}'")
        
        correct_answer = ""
        
        if plan_type == "stealth":
            sp.smart_print("The Stethoscope reveals clicks at specific positions.")
            sp.smart_print("Clue: The combination is the 1st letter, the 4th letter, and the last letter of the name.")
            # Logic: P (index 0), K (index 3), N (index -1)
            correct_answer = vault_label[0] + vault_label[3] + vault_label[-1]
            
        elif plan_type == "trickery":
            sp.smart_print("The Map has a note about the override.")
            sp.smart_print("Clue: The code is the first 3 letters of the name, backwards.")
            # Logic: N (2), I (1), P (0) -> "NIP"
            correct_answer = vault_label[0:3][::-1] 

        # The Player Input (The "String Indexing" Challenge)
        print(f"\n(Solve the puzzle based on the word '{vault_label}')")
        player_attempt = input("Enter the code/letters exactly: ").strip().upper()

        if player_attempt == correct_answer:
            sp.smart_print("\nCLICK. Whirrrrrr...")
            sp.smart_print("The massive bolts retract. The door swings open!")
            # Note: Score was already incremented by handle_obstacle above.
        else:
            sp.smart_print(f"\nBUZZER! Wrong code. You guessed '{player_attempt}'.")
            sp.smart_print("The alarm triggers! You fumbled the lock!")
            return -1, plan_type


    # --- OBSTACLE 3: The Escape ---
    if plan_type == "stealth":
        desc = "The Sheriff is patrolling nearby. We need to disable his ability to call for help."
        succ = "Snip. You cut the telegraph wire. The town is isolated."
    elif plan_type == "force":
        desc = "We are on the roof! We need a way down to the horses in the alley."
        succ = "You rappel down the side of the building before they know you're gone."
    elif plan_type == "trickery":
        desc = "The stable hand is awake and watching our horses. He will scream if he sees us."
        succ = "You toss the vial. He slumps over, asleep. The horses are ours."
    elif plan_type == "gentleman":
        desc = "The posse is forming. Their horses are fresh, and ours will tire out in 5 miles. We need a backup."
        succ = "The relay works perfectly. You switch to fresh mounts and leave the posse in the dust."

    if not handle_obstacle("The Escape", desc, succ): return -1, plan_type

    return score, plan_type

def escape_result(score, plan_type, User_Name):
    """
    Calculates final ending based on the score returned from execute_heist.
    - Score -1: Immediate capture.
    - Score >= 2: Success. (Checks specifically for Gentleman Plan + Score 3 for a 'Legendary' ending).
    - Score 1.5: 'Last Stand' scenario where user chooses between betrayal or death.
    """
    sp.smart_print("\n--- THE GETAWAY ---")
    t.sleep(1)
    
    # CASE 1: TOTAL FAILURE (Used more than 3 items / Failed an obstacle twice)
    if score == -1:
        sp.smart_print("You fumbled with your tools too many times.")
        sp.smart_print("The guards swarm you before you can even leave the bank.")
        sp.smart_print(f"{ITALICS}BAD ENDING: {User_Name} is captured immediately.{RESET}")
        return

    # CASE 2: SUCCESS
    if score >= 2:
        sp.smart_print(f"You pulled off the job with {score}/3 points.")
        sp.smart_print("You ride into the sunset with $21,000 in gold.")
        
        # Check for Historical Bonus (Specific to Gentleman plan)
        if plan_type == "gentleman" and score == 3:
            sp.smart_print(f"\n{ITALICS}*** HISTORICAL FACT UNLOCKED ***{RESET}")
            sp.smart_print("""
            You just recreated the real Telluride Robbery of June 24, 1889!
            Butch Cassidy and his gang really did:
            1. Enter politely with Colts drawn but never fired.
            2. Force the teller to fill their sacks.
            3. Use a genius 'Horse Relay' system (stashing fresh horses with feed miles away).
            """)
            sp.smart_print(f"{ITALICS}LEGENDARY ENDING: The True Bandit King.{RESET}")
        else:
            sp.smart_print(f"{ITALICS}NORMAL ENDING: The Wild {User_Name} lives on.{RESET}")

    # CASE 3: THE LAST DITCH EFFORT (Score 1.5)
    elif score == 1.5:
        sp.smart_print(f"The heist was sloppy. You only got {score} points.")
        sp.smart_print("The Sheriff's posse has you pinned down in the canyon!")
        sp.smart_print("You have one bullet left and a terrible choice to make.")
        
        print("\n1. Stay and fight with your crew (Honorable Death)")
        print("2. Shoot your partner's horse to distract the posse and escape alone (Betrayal)")
        
        final_choice = input("What do you do? (1/2): ").strip()
        
        if final_choice == "2":
             sp.smart_print("\nBLAM. You fire at your friend's horse.")
             sp.smart_print("While the posse surrounds your screaming crew, you slip away into the shadows.")
             sp.smart_print(f"You survive, but you will never be trusted again.")
             sp.smart_print(f"{ITALICS}COWARDLY ENDING: The Traitor.{RESET}")
        elif final_choice == "1":
             sp.smart_print("\nYou nod to your friends. 'Lets give 'em hell.'")
             sp.smart_print("You charge out, guns blazing.")
             sp.smart_print(f"{ITALICS}BAD ENDING: {User_Name} went down fighting.{RESET}")
        else:
             sp.smart_print("\nIndecision is fatal. The posse overwhelms you all.")
             sp.smart_print(f"{ITALICS}BAD ENDING: {User_Name} is captured.{RESET}")

    # CASE 4: BAD RUN (Score < 1.5 but not -1)
    else:
        sp.smart_print(f"The heist was a mess. You only got {score}/3 points.")
        sp.smart_print("The Sheriff's posse catches up to you in the mountains.")
        sp.smart_print("A gunfight breaks out. You are surrounded.")
        sp.smart_print(f"{ITALICS}BAD ENDING: {User_Name} is captured.{RESET}")