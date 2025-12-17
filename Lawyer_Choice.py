import FP_inventory as inv
import Smart_Print as sp
import time as t

ITALICS = '\x1b[3m' 
RESET = '\x1b[0m'

# --- Intro Section ---
def lawyer_Intro(User_Name):
    """
    Displays the introductory narrative for the Lawyer path.
    Sets the scene, explains the background of the case (Butch Cassidy),
    and provides the details required for the trial.
    """
    sp.smart_print(f"""
    Congrats, {User_Name}! You just selected the most successful step in your life! {ITALICS}No matter how boring {RESET}
    If you picked this choice, you have completed most of the game. 
    Don't be discouraged! You picked the boring route! In life you can't take back any choices!
    For your valiant effort I'll give you a summary of your progress.
    """)

    sp.smart_print("""
    Life Choice 1: Go to School - Successful Step
    You chose to go to school and become a lawyer!
    You passed the bar on the first try and have been hired by 'XXXXXX Law Firm' 
    Now let's continue with the story!
    """)

    sp.smart_print("""
    For your first case you are DEFENDING a suspected bank robber.
    These are the details:
    
    Incident: On a bright Monday morning, three men rode into town.
    One stayed with the horses; two entered the bank.
    They were polite, professional, and quiet.
    
    They walked up to the teller, drew their Colt .45s,
    and demanded the teller fill a sack with gold coins and banknotes.
    They walked out with $21,000, mounted their horses, and vanished
    into the mountains without firing a single shot.
    
    Your client's name is Butch Cassidy.
    The location of the crime is the San Miguel Valley Bank.
    The date the crime happened is June 24, 1889. Time: 10:45 AM.
    Your client's court session is in 3 hours.
    """)


# --- Strategy Selection ---
def lawyer_Choice_1(User_Name):
    """
    Prompts the user to select a defense strategy.
    
    Returns:
        str: A keyword ('mistaken_identity', 'rider', 'gambler', 'guilty') 
             representing the chosen strategy. This keyword drives the logic 
             in the cross-examination phase.
    """
    # Populates the external text file with evidence items needed for the trial
    inv.fill_inventory()
    sp.smart_print("Your inventory has been filled with all the evidence available.")
    sp.smart_print("You should take a look at the text file now before you make any choices.")
    
    # Pauses until the user presses Enter, simulating the time taken to review evidence
    input("\n(Open your inventory file, check the items, then press Enter to continue...)")

    sp.smart_print("While you were looking at the inventory, the court case started.")
    sp.smart_print("You are now in the courtroom, and the judge is looking at you.")
    sp.smart_print(f"JUDGE: {User_Name}! Is the defense ready to proceed?")
    sp.smart_print("It's your turn to weave your opening statement.")
    sp.smart_print("You have 4 choices:")
    
    print("1. 'The Ghost in the Rain' (Mistaken Identity)")
    print("2. 'The Impossible Rider' (The Timeline Alibi)")
    print("3. 'The Gambler's Luck' (The Honest Scoundrel)")
    print(f"4. 'The Coward's Way Out' (Plead Guilty/No Contest)")
    print(f"{ITALICS}Remember that the plan you pick will decide what items you must use to succeed.{RESET}")
    print(f"{ITALICS}Each plan has only one specific set of items that work.{RESET}")

    while True:
        choice_alibi = input("\nWhich opening statement do you choose? (1/2/3/4): ").strip()

        if choice_alibi == "1":
            sp.smart_print(f"\n{ITALICS}You chose 'The Ghost in the Rain'...{RESET}")
            sp.smart_print("""
            Ladies and gentlemen, the prosecution describes a villain with a thick mustache 
            riding a fresh, powerful stallion through the mud of the high peaks.
            
            But look at my client. You will see a clean-shaven man. You will see boots caked 
            in red clay, not grey mountain mud. They are convicting a ghost; my client is 
            just the man who happened to walk into the wrong saloon.
            """)
            return "mistaken_identity"

        elif choice_alibi == "2":
            sp.smart_print(f"\n{ITALICS}You chose 'The Impossible Rider'...{RESET}")
            sp.smart_print("""
            Time is a stubborn thing. The prosecution claims my client was standing in that 
            bank at 10:45 AM sharp. 
            
            But we live in a world of schedules and timestamps. We will introduce records—
            messages sent across the wire and tickets punched by conductors—that place 
            Butch Cassidy miles away at the very moment the vault was opened. 
            Unless my client can fly, he simply wasn't there.
            """)
            return "rider" 

        elif choice_alibi == "3":
            sp.smart_print(f"\n{ITALICS}You chose 'The Gambler's Luck'...{RESET}")
            sp.smart_print("""
            I will not stand here and tell you Butch Cassidy is a saint. He is a drifter. 
            He is a drinker. And yes, when they arrested him, his pockets were full of crisp cash. 
            
            The prosecution shouted 'Thief!' But we will show you exactly where that money 
            came from. It wasn't taken at gunpoint; it was won with a full house. 
            He is a scoundrel, ladies and gentlemen, but he is a lucky one, not a criminal.
            """)
            return "gambler" 

        elif choice_alibi == "4":
            # --- THE PLEA BARGAIN ENDING (Happens Immediately) ---
            # If the user pleads no contest, the trial logic is bypassed.
            sp.smart_print(f"\n{ITALICS}You chose to Plead No Contest...{RESET}")
            sp.smart_print("""
            You stand up, straightening your tie. You look at Butch, who shakes his head in disappointment.
            
            "Your Honor," you say clearly. "My client wishes to enter a plea of Nolo Contendere."
            
            The courtroom gasps. The Judge nods, appreciating the time saved.
            
            JUDGE: "Very well. In light of your cooperation, I sentence Butch Cassidy 
            to 5 years in the State Penitentiary, rather than the usual 20."
            
            It wasn't a win. But it wasn't a total loss. 
            You kept him from the gallows, but he will still rot in a cell.
            """)
            sp.smart_print(f"{ITALICS}NEUTRAL ENDING: The Deal Maker.{RESET}")
            return "guilty" # This key tells the other functions to skip

        else:
            sp.smart_print("The Judge looks annoyed. Please choose 1, 2, 3, or 4.")

# --- Flavor Failure Helper ---
def check_flavor_failure(item_choice):
    """
    Returns a specific failure message for miscellaneous items (Flavor Text).
    Returns None if the item is not a flavor item.
    """
    # Group 1: Documents that are legal but useless as evidence
    legal_fluff = ["Blackstones Law Dictionary", "Colorado Bar License", "Copy of the Constitution", 
                   "Subpoena for the Sheriff", "Jury List", "Leather Briefcase", "Ink-Stained Notebook", "Fountain Pen"]
    if item_choice in legal_fluff:
        return f"You wave the {item_choice} around. It makes you look like a lawyer, but it proves absolutely nothing about the case."

    # Group 2: Random Junk
    junk = ["Dried Beef Jerky", "Flask of Whiskey", "Tin of Tobacco", "Box of Lucifer Matches", "Rabbits Foot", "Silver Pocket Watch", "Photograph of a Lady"]
    if item_choice in junk:
        return f"You offer the {item_choice} to the witness. The Judge bangs his gavel. 'Counselor! Stop trying to bribe the witness with your personal belongings!'"

    # Group 3: Weapons (Instant Danger)
    if item_choice == "Derringer Pistol":
        return "You pull out the Derringer! The Bailiff puts his hand on his holster. The Judge screams, 'Put that away or I will hold you in contempt!'"

    # Group 4: Useless Evidence
    if item_choice == "Weather Almanac":
        return "You argue about the weather. 'It was sunny!' ... 'Yes,' says the witness, 'We know. That changes nothing.'"
    
    if item_choice == "Magnifying Glass":
        return "You hold the magnifying glass up to the witness's face. It just makes their nose look huge. The jury giggles."

    return None

# --- Cross Examination ---
def cross_examine_witnesses(alibi_type, User_Name):
    """
    Executes the trial logic.
    - Uses a dictionary to map the chosen strategy ('alibi_type') to specific witnesses and required items.
    - Loops through 3 witnesses.
    - Checks the external inventory file to see if the user possesses and inputs the correct item.
    
    Returns:
        int: The number of correct objections made (points).
    """
    # --- CHECK FOR GUILTY PLEA ---
    # If they pleaded guilty, we skip the trial entirely.
    if alibi_type == "guilty":
        return -1 # Return a dummy score so the game doesn't crash

    defense_points = 0
    sp.smart_print("\n--- THE CROSS EXAMINATION ---")
    sp.smart_print(f"JUDGE: Counselor {User_Name}, you may cross-examine the witnesses.")
    sp.smart_print(f"Remember your strategy: {alibi_type.upper().replace('_', ' ')}")

    # 1. SETUP THE SCENARIOS
    # Now includes 'failure_msgs' for items that are valid evidence but WRONG for the specific context.
    scenarios = {
        "mistaken_identity": [
            {
                "witness": "Mrs. Gable (The Baker)",
                "statement": "I saw him clear as day! He was staring right at me through the window. He had these cold, sharp eyes.\n He looked like a sharpshooter, squinting at his target!",
                "valid_items": ["Reading Spectacles"],
                "success_msgs": {
                    "Reading Spectacles": "You hand the spectacles to the Bailiff. 'The defendant is nearly blind without these. He wasn't \nsquinting because he's mean; he was squinting because he couldn't see you!'"
                },
                "failure_msgs": {
                    "Muddy Spurs": "You show the spurs. 'His boots are muddy!' ... Mrs. Gable looks confused. 'What do his feet have to do with his eyes?'",
                    "Witness Sketch": "You show the sketch. 'He doesn't look like this!' ... Mrs. Gable shrugs. 'Drawings are never perfect. I saw his eyes.'",
                    "Train Ticket Stub": "You show the ticket. 'He was on a train!' ... The Judge interrupts. 'That is a timeline argument, Counselor. \nAddress the witness's visual description.'",
                    "Sloppy Poker Ledger": "You show the ledger. 'He is a gambler!' ... 'So?' asks Mrs. Gable. 'Gamblers can still stare at people.'"
                }
            },
            {
                "witness": "Sheriff Jim",
                "statement": "We tracked his boot prints from the bank all the way to the saloon. There was grey mud on the carpet. \nIt matches the mud from the mountain pass exactly!",
                "valid_items": ["Muddy Spurs"],
                "success_msgs": {
                    "Muddy Spurs": "You slam the boots on the table. Red Clay. 'These boots are covered in Valley Clay, Sheriff. He hasn't \nbeen up the mountain in weeks.'"
                },
                "failure_msgs": {
                    "Reading Spectacles": "You show the glasses. 'He can't see!' ... The Sheriff laughs. 'He doesn't need to see to leave footprints, Counselor.'",
                    "Train Ticket Stub": "You show the ticket. 'He was travelling!' ... 'Maybe,' says the Sheriff, 'But he walked into that saloon eventually.'",
                    "Receipt for a New Horse": "You show the receipt. 'He bought a horse!' ... 'And he walked that horse through the mud,' relies the Sheriff."
                }
            },
            {
                "witness": "Mr. Rich (The Banker)",
                "statement": "I described the robber to the police artist immediately. Big mustache, scar on his cheek. That man \nsitting right there is the man I described!",
                "valid_items": ["Witness Sketch"],
                "success_msgs": {
                    "Witness Sketch": "You hold up the sketch next to Butch's face. No scar. No mustache. 'Mr. Rich, this drawing looks \nmore like the Sheriff than my client.'"
                },
                "failure_msgs": {
                    "Muddy Spurs": "You point at his boots. 'Look at the mud!' ... Mr. Rich rolls his eyes. 'I am talking about his face, not his shoes.'",
                    "Crisp $100 Bill": "You show the money. 'He has cash!' ... 'Yes! My cash!' screams Mr. Rich. You just made him angrier.",
                    "Telegram from Denver": "You show the telegram. 'He was in Denver!' ... Mr. Rich shakes his head. 'I saw his face right here in my bank.'"
                }
            }
        ],
        "rider": [
            {
                "witness": "Mrs. Gable (The Baker)",
                "statement": "I looked at the clock tower. It was exactly 10:45 AM when they rode out. I saw the defendant on the \nlead horse!",
                "valid_items": ["Railroad Schedule", "Train Ticket Stub"],
                "success_msgs": {
                    "Railroad Schedule": "You present the Schedule. 'The train to Denver leaves at 10:30 AM. If he was on that train, he \ncouldn't be on a horse at 10:45.'",
                    "Train Ticket Stub": "You show the ticket stub. 'He boarded the 10:30 train, Mrs. Gable. It would be physically impossible \nfor him to be on a horse 15 minutes later.'"
                },
                "failure_msgs": {
                    "Muddy Spurs": "You show the spurs. 'He rides in mud!' ... 'Yes, I saw him riding,' Mrs. Gable agrees. You just helped the prosecution.",
                    "Reading Spectacles": "You show the glasses. 'He is blind!' ... 'He was holding the reins just fine,' she insists.",
                    "Sloppy Poker Ledger": "You show the poker ledger. 'He was playing cards!' ... 'Not at 10:45 AM he wasn't,' she replies."
                }
            },
            {
                "witness": "Sheriff Jim",
                "statement": "He didn't leave town! My deputies were watching the roads. He was hiding in the saloon the whole time!",
                "valid_items": ["Telegram from Denver", "Train Ticket Stub"],
                "success_msgs": {
                    "Telegram from Denver": "You read the timestamp on the Telegram. 'Sent from Denver: 12:00 PM.' It is physically impossible \nto ride from Telluride to Denver in one hour.",
                    "Train Ticket Stub": "You wave the ticket stub. 'Sheriff, he wasn't in the saloon. This ticket proves he was on a train \nheaded for Denver while your deputies were watching empty roads.'"
                },
                "failure_msgs": {
                    "Witness Sketch": "You show the sketch. 'This doesn't look like him!' ... The Sheriff grunts. 'Doesn't matter. We caught him in the saloon.'",
                    "Deck of Marked Cards": "You show the cards. 'He was playing cards!' ... 'In the saloon! Exactly!' says the Sheriff. You walked right into that one.",
                    "Bank Layout Map": "You show the map. 'He knew the layout!' ... 'So he is guilty!' yells the Sheriff. Why did you show that?"
                }
            },
            {
                "witness": "Mr. Rich (The Banker)",
                "statement": "He was in my bank when the vault opened! I punched the alarm myself at 10:40!",
                "valid_items": ["Train Ticket Stub"],
                "success_msgs": {
                    "Train Ticket Stub": "You show the ticket punch. 'This ticket was punched by the conductor at 10:40 AM... fifty miles away.'"
                },
                "failure_msgs": {
                    "Telegram from Denver": "You show the telegram. 'He was in Denver at noon!' ... Mr. Rich argues, 'He could have robbed the bank at 10:40 and rode fast!' (The telegram came too late to prove the 10:40 timeline).",
                    "Crisp $100 Bill": "You show the money. Mr. Rich tries to grab it. 'That's mine!' This didn't help your timeline argument."
                }
            }
        ],
        "gambler": [
            {
                "witness": "Mrs. Gable (The Baker)",
                "statement": "He's a thief! I saw him counting money in the alleyway. Honest men don't hide in alleys to count cash!",
                "valid_items": ["Sloppy Poker Ledger", "Deck of Marked Cards"],
                "success_msgs": {
                    "Sloppy Poker Ledger": "You open the Ledger. 'He wasn't hiding loot, Mrs. Gable. He was counting his winnings from the game \nat the hotel.'",
                    "Deck of Marked Cards": "You fan out the marked cards. 'He wasn't counting stolen money, Mrs. Gable. He was sorting his \nmarked deck. He is a cheat, perhaps, but not a bank robber.'"
                },
                "failure_msgs": {
                    "Crisp $100 Bill": "You show the bill. 'It is old money!' ... Mrs. Gable sniffs. 'Money is money. Honest men don't count it in alleys.'",
                    "Muddy Spurs": "You show the spurs. 'He was riding!' ... 'No, he was standing still counting cash,' she corrects you.",
                    "Train Ticket Stub": "You show the ticket. 'He travels!' ... 'So do thieves,' she says."
                }
            },
            {
                "witness": "Sheriff Jim",
                "statement": "We found exactly $3,000 in his pocket. He had no job. That is clearly a share of the stolen bank money!",
                "valid_items": ["Crisp $100 Bill", "Receipt for a New Horse"],
                "success_msgs": {
                    "Crisp $100 Bill": "You verify the serial numbers. 'The bank reported stolen gold. This is a Federal Note, printed in 1880. \nIt's old money, Sheriff, not the new batch from the vault.'",
                    "Receipt for a New Horse": "You hand over the receipt. 'He just sold a horse for $2,500 cash this morning, Sheriff. That explains \nthe money in his pocket better than your theory.'"
                },
                "failure_msgs": {
                    "Sloppy Poker Ledger": "You show the ledger. 'He wins at poker!' ... The Sheriff shakes his head. 'Ledgers can be faked. The cash in his pocket is real.'",
                    "Witness Sketch": "You show the sketch. 'Wrong face!' ... 'He had the money in his pocket!' The Sheriff doesn't care about the face right now.",
                    "Reading Spectacles": "You show the glasses. 'He is blind!' ... 'He could see the money well enough to steal it,' says the Sheriff."
                }
            },
            {
                "witness": "Mr. Rich (The Banker)",
                "statement": "He is a bum! A drifter! He has no income! The only way a man like that gets rich is by robbing my bank!",
                "valid_items": ["Receipt for a New Horse", "Sloppy Poker Ledger"],
                "success_msgs": {
                    "Receipt for a New Horse": "You show the Receipt. 'He sold a prize mare yesterday for $2,500. He isn't a bum, Mr. Rich. He's just \na better businessman than you.'",
                    "Sloppy Poker Ledger": "You slam the ledger down. 'Look at the numbers, Mr. Rich. He makes more playing Poker in a week \nthan you pay your tellers in a year.'"
                },
                "failure_msgs": {
                    "Crisp $100 Bill": "You show the bill. 'It's old money!' ... Mr. Rich scoffs. 'A bum with old money is still a thief.'",
                    "Train Ticket Stub": "You show the ticket. 'He can afford trains!' ... 'Robbers can afford trains too,' says Mr. Rich."
                }
            }
        ]
    }

    current_path = scenarios[alibi_type]
    
    # Iterate through each witness in the selected path
    for round_data in current_path:
        # Helper logic inside the loop
        sp.smart_print(f"\nWITNESS: {round_data['witness']}")
        sp.smart_print(f"'{round_data['statement']}'")
        print(f"\n(Hint: You need something related to {alibi_type.replace('_', ' ')} logic)")
        
        item_choice = input("Check your inventory. Enter exact item name: ").strip()
        
        # Read the file to get current inventory state
        current_inv = inv._read_file()
        
        # Check if the user actually has the item in their file
        if item_choice in current_inv:
            inv.del_inventory(item_choice, 1) # Remove the item after use
            
            # --- CHECK 1: Is it the CORRECT item? ---
            if item_choice in round_data['valid_items']:
                sp.smart_print(f"\nSUCCESS! You presented the {item_choice}.")
                # Use the dictionary mapping to get the specific success text
                msg = round_data['success_msgs'][item_choice]
                sp.smart_print(msg)
                defense_points += 1
            
            # --- CHECK 2: Is it a SPECIFIC FAILURE (Valid evidence, wrong context)? ---
            elif 'failure_msgs' in round_data and item_choice in round_data['failure_msgs']:
                 sp.smart_print(f"\nFAIL. You presented the {item_choice}.")
                 fail_msg = round_data['failure_msgs'][item_choice]
                 sp.smart_print(f"The Judge looks annoyed. {fail_msg}")

            # --- CHECK 3: Is it FLAVOR TEXT (Random junk items)? ---
            else:
                flavor_msg = check_flavor_failure(item_choice)
                if flavor_msg:
                    sp.smart_print(f"\nFAIL. {flavor_msg}")
                else:
                    # Generic Fallback if they used an item not defined anywhere else
                    sp.smart_print(f"\nFAIL. You presented the {item_choice}.")
                    sp.smart_print("The Judge looks confused. 'Counselor, I fail to see how that object is relevant to this case.'")

        else:
            sp.smart_print("\nFAIL. You reach into your briefcase...")
            sp.smart_print(f"...but you don't have a '{item_choice}'!")

    return defense_points


# --- Closing Statements ---
def closing_statements(points, alibi_type, User_Name):
    """
    Determines the final verdict based on the points accumulated in cross_examination.
    - If points >= 2: Automatic win.
    - If points < 2: User gets a 'Hail Mary' chance to pick a closing speech. 
      If the speech matches their original strategy, they win; otherwise, they lose.
    """
    # --- CHECK FOR GUILTY PLEA ---
    # If they pleaded guilty, we skip the closing arguments.
    if alibi_type == "guilty":
        return 

    sp.smart_print(f"\n--- CLOSING STATEMENTS: Counselor {User_Name} ---")
    t.sleep(1)
    
    if points >= 2:
        sp.smart_print(f"You presented a strong case with {points}/3 correct pieces of evidence.")
        sp.smart_print("The jury doesn't even need to hear your speech.")
        sp.smart_print(f"{ITALICS}VERDICT: NOT GUILTY.{RESET}")
        sp.smart_print("Butch Cassidy tips his hat to you and walks free.")
        return 

    else:
        sp.smart_print(f"Things look bad. You only got {points}/3 points.")
        sp.smart_print("The jury is glaring at Butch. You need a MIRACLE closing speech.")
        sp.smart_print("You must pick the speech that matches your original opening strategy.")
        
        print("\n1. 'He was in Denver on a Train!' (Timeline Defense)")
        print("2. 'He is just a lucky card player!' (Gambler Defense)")
        print("3. 'That wasn't him, check the boots!' (Identity Defense)")
        
        final_choice = input("Pick your final argument (1/2/3): ").strip()
        
        won_case = False
        
        # Logic to check if the final speech matches the original alibi type
        if final_choice == "1" and alibi_type == "rider":
            won_case = True
        elif final_choice == "2" and alibi_type == "gambler":
            won_case = True
        elif final_choice == "3" and alibi_type == "mistaken_identity":
            won_case = True
            
        if won_case:
            sp.smart_print("\nIt was a risky move... but it worked!")
            sp.smart_print("The jury remembered your opening statement and the pieces clicked together.")
            sp.smart_print(f"{ITALICS}VERDICT: NOT GUILTY.{RESET}")
        else:
            sp.smart_print("\nYour closing statement contradicted your own evidence.")
            sp.smart_print("The jury is confused and angry.")
            sp.smart_print(f"{ITALICS}VERDICT: GUILTY.{RESET}")
            sp.smart_print("Butch Cassidy is dragged away in chains.")