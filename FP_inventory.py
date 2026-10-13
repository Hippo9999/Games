import os
import random # Imported for shuffling inventory items

# 1. Initialize with a default
current_file = "default_inventory.txt" 

# --- Function to Handle the Filename ---
def set_filename(user_name):
    """Sets the global variable 'current_file' to the user's input."""
    global current_file
    if not user_name.endswith(".txt"):
        user_name += ".txt"
    current_file = user_name

# --- Helper Functions ---
# Read File
def _read_file():
    """
    Reads the 'current_file', parses lines separated by commas (item,quantity),
    and returns a dictionary of the inventory.
    """
    data = {}
    if os.path.exists(current_file): 
        with open(current_file, "r") as f:
            for line in f:
                if "," in line:
                    name, qty = line.strip().split(",")
                    data[name] = int(qty)
    return data

# Edit and Save File
def _save_file(data):
    """
    Takes a dictionary 'data' and overwrites the 'current_file' 
    in the format 'item,quantity' for each line.
    """
    with open(current_file, "w") as f: 
        for name, qty in data.items():
            f.write(f"{name},{qty}\n")


# --- Main Inventory Functions ---
# Deletes text in inventory
def reset_inventory():
    """Wipes the CURRENT file clean."""
    open(current_file, "w").close()
    # print(f"Inventory '{current_file}' has been reset.") # Optional: Commented out to reduce clutter during startup

# Function for adding singular items to inventory
def add_inventory(name, quantity):
    """Reads the file, increments the count for a specific item, and saves it back."""
    inventory = _read_file()
    inventory[name] = inventory.get(name, 0) + quantity
    _save_file(inventory)
    print(f"Added {quantity} {name}(s) to {current_file}.")

# Function for Deleting Singular Items from the Inventory
def del_inventory(name, quantity):
    """
    Reads the file, decrements the item count.
    If count reaches 0 or less, the item is removed from the dictionary entirely.
    """
    inventory = _read_file()
    if name in inventory:
        inventory[name] -= quantity
        if inventory[name] <= 0:
            del inventory[name]
        _save_file(inventory)
        print(f"Removed {quantity} {name}(s) from {current_file}.")
    else:
        print(f"Error: {name} not found.")

# Inventory Fill for Lawyer Path
def fill_inventory():
    """Populates the current file with the Lawyer items."""
    starting_gear = [
        "Crisp $100 Bill", "Sloppy Poker Ledger", "Witness Sketch", "Weather Almanac", 
        "Train Ticket Stub", "Muddy Spurs", "Bank Layout Map", "Telegram from Denver", 
        "Dear John Letter", "Receipt for a New Horse", "Leather Briefcase", 
        "Blackstones Law Dictionary", "Ink-Stained Notebook", "Fountain Pen", 
        "Subpoena for the Sheriff", "Jury List", "Magnifying Glass", "Colorado Bar License", 
        "Copy of the Constitution", "Reading Spectacles", "Derringer Pistol", 
        "Silver Pocket Watch", "Flask of Whiskey", "Deck of Marked Cards", 
        "Tin of Tobacco", "Box of Lucifer Matches", "Dried Beef Jerky", 
        "Rabbits Foot", "Photograph of a Lady", "Railroad Schedule"
    ]
    
    # Randomize the order so the user has to actually search the text file
    random.shuffle(starting_gear)
    
    data = _read_file()
    for item in starting_gear:
        data[item] = 1
    _save_file(data)

# Inventory Fill for Robber Path
def fill_robber_inventory():
    """Populates the inventory with Heist Tools."""
    starting_gear = [
        "Colt .45 Revolver", "Stick of Dynamite", "Stethoscope", "Lockpick Set", 
        "Coil of Rope", "Bandana Mask", "Sack of Horse Feed", "Telegraph Wire Cutters",
        "Crowbar", "Fake Sheriff Badge", "Map of the Bank", "Sleeping Gas Vial",
        "Shotgun", "Empty Money Sack", "Bowie Knife", "Bottle of Whiskey",
        "Ace of Spades", "Box of Matches", "Rusty Key", "Wanted Poster (You)",
        "Pocket Watch", "Compass", "Canteen of Water", "Binoculars",
        "Bag of Sand", "Gloves", "Grappling Hook", "Signal Mirror", "Tobacco Plug", "Lucky Coin"
    ]
    
    # Randomize the order
    random.shuffle(starting_gear)
    
    data = _read_file()
    for item in starting_gear:
        data[item] = 1
    _save_file(data)

# --- The Inventory Setup Function---
def initialize_inventory_system():
    """
    Runs at the start of the game.
    Asks the user to name their inventory file.
    Checks if that file already exists to prevent accidental overwrites.
    """
    print("For more organization and safety, this program uses a self named inventory system!")
    
    while True:
        user_file = input("Enter a name for your inventory file: ").strip()
        
        # Error check to ensure .txt extension
        if user_file.endswith(".txt"):
            user_file = user_file[:-4]

        expected_filename = user_file + ".txt"

        # Check existence
        if os.path.exists(expected_filename):
            print(f"\n[ALERT] A file named '{expected_filename}' already exists!")
            choice = input("Do you want to overwrite this file? (yes/no): ").lower()

            if choice == "yes":
                print(f"Overwriting '{expected_filename}'...")
                set_filename(user_file)
                reset_inventory()
                break
            else:
                print("Overwrite cancelled. Please choose a different name.\n")
                continue 
        else:
            print(f"Creating new file: '{expected_filename}'")
            set_filename(user_file)
            reset_inventory()
            break