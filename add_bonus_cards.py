import random
import mysql.connector
from card_creation import Card

def create_bonus_cards():
    """
    Main function to create bonus cards for the game based on prize inventory
    Returns list of bonus cards or empty list if no bonus cards created
    """
    
    # Get current prize inventory from database
    current_prize_inventory = get_current_prize_inventory()
    
    # If no prizes available, exit gracefully
    if not current_prize_inventory:
        return []
    
    # Determine if bonus cards should be created
    bonus_card_qty = 0
    while random.random() < 0.1:  # 10% chance of creating bonus cards
        bonus_card_qty += 1
    
    # If no bonus cards to create, exit gracefully
    if bonus_card_qty == 0:
        return []
    
    # Create bonus card objects
    bonus_cards = []
    for _ in range(bonus_card_qty):
        # Create card with bonus suit and all other attributes as None/zero
        bonus_card = Card(
            rank=None,
            trick_power=None,
            suit='bonus',
            score_value=None
        )
        bonus_cards.append(bonus_card)
    
    # Assign ranks to bonus cards from available prizes
    list_of_bonus_cards = assign_ranks_to_bonus_cards(bonus_cards, current_prize_inventory)
    
    # Update database to remove used prizes
    update_prize_inventory(current_prize_inventory)
    
    return list_of_bonus_cards

def get_current_prize_inventory():
    """
    Fetch current prize inventory from database and create list with appropriate quantities
    """
    try:
        # Database connection
        connection = mysql.connector.connect(
            host='localhost',  # Adjust as needed
            database='dkgsunll_buddywilde_db',
            user='your_username',  # Replace with actual username
            password='your_password'  # Replace with actual password
        )
        
        cursor = connection.cursor(dictionary=True)
        
        # Query to get all prizes with quantity > 0
        query = "SELECT prize_type, quantity FROM prize_inventory WHERE quantity > 0"
        cursor.execute(query)
        prizes = cursor.fetchall()
        
        # Create inventory list with appropriate quantities
        current_prize_inventory = []
        for prize in prizes:
            current_prize_inventory.extend([prize['prize_type']] * prize['quantity'])
        
        return current_prize_inventory
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def assign_ranks_to_bonus_cards(bonus_cards, current_prize_inventory):
    """
    Assign ranks to bonus cards by randomly selecting from available prizes
    """
    list_of_bonus_cards = []
    
    for bonus_card in bonus_cards:
        if not current_prize_inventory:
            break
            
        # Randomly select a prize from available inventory
        selected_prize = random.choice(current_prize_inventory)
        
        # Set the rank of the bonus card to the selected prize type
        bonus_card.rank = selected_prize
        
        # Remove one instance of this prize from inventory
        current_prize_inventory.remove(selected_prize)
        
        # Add card to list of bonus cards
        list_of_bonus_cards.append(bonus_card)
    
    return list_of_bonus_cards

def update_prize_inventory(current_prize_inventory):
    """
    Update database to reduce prize quantities based on what was used
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor()
        
        # Count occurrences of each prize type in the inventory list
        prize_counts = {}
        for prize in current_prize_inventory:
            prize_counts[prize] = prize_counts.get(prize, 0) + 1
        
        # Update database for each prize type
        for prize_type, count in prize_counts.items():
            update_query = "UPDATE prize_inventory SET quantity = quantity - %s WHERE prize_type = %s"
            cursor.execute(update_query, (count, prize_type))
        
        connection.commit()
        
    except mysql.connector.Error as err:
        print(f"Database update error: {err}")
        # In production, you might want to rollback or handle this more gracefully
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Global variable to store bonus cards for this session
bonus_card_list = []

def main():
    """
    Main execution function - this will be called by the card creation module
    """
    global bonus_card_list
    
    # Clear any previous bonus cards
    bonus_card_list = []
    
    # Create bonus cards
    bonus_cards = create_bonus_cards()
    
    # Store in global list for access by card creation module
    bonus_card_list = bonus_cards
    
    return bonus_cards

# This is the function that will be called by the card creation module
def get_bonus_cards():
    """
    Function to be called by card_creation.py to get bonus cards
    """
    return bonus_card_list

# Example usage (this would be called by the main game logic)
if __name__ == "__main__":
    # This would be called by your main game logic
    bonus_cards = main()
    print(f"Created {len(bonus_cards)} bonus cards")
