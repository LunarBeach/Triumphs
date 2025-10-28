import mysql.connector
import json
from datetime import datetime

def create_game_session(user_id, max_players=4):
    """
    Create a new game session
    Returns the game_session_id
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor()
        
        query = """
        INSERT INTO triumphs_game_sessions 
        (game_creator, game_state, max_players, players)
        VALUES (%s, %s, %s, %s)
        """
        
        # Initialize players as empty array
        players = []
        players_json = json.dumps(players)
        
        cursor.execute(query, (user_id, 'waiting', max_players, players_json))
        connection.commit()
        
        game_session_id = cursor.lastrowid
        return game_session_id
        
    except mysql.connector.Error as err:
        print(f"Error creating game session: {err}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_waiting_games():
    """
    Get all game sessions in 'waiting' state
    Returns list of game sessions
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM triumphs_game_sessions WHERE game_state = 'waiting'"
        cursor.execute(query)
        games = cursor.fetchall()
        
        return games
        
    except mysql.connector.Error as err:
        print(f"Error fetching waiting games: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def join_game_session(game_session_id, user_id):
    """
    Add a user to a waiting game session
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        # Get current game session
        query = "SELECT players, total_players FROM triumphs_game_sessions WHERE game_session_id = %s"
        cursor.execute(query, (game_session_id,))
        game = cursor.fetchone()
        
        if not game:
            return False
            
        # Parse existing players
        players = json.loads(game['players']) if game['players'] else []
        
        # Check if user already joined
        if user_id in players:
            return True
            
        # Add user to players
        players.append(user_id)
        
        # Update total players count
        total_players = len(players)
        
        # Update the game session
        update_query = """
        UPDATE triumphs_game_sessions 
        SET players = %s, total_players = %s 
        WHERE game_session_id = %s
        """
        
        players_json = json.dumps(players)
        cursor.execute(update_query, (players_json, total_players, game_session_id))
        connection.commit()
        
        return True
        
    except mysql.connector.Error as err:
        print(f"Error joining game session: {err}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def start_game_session(game_session_id, creator_user_id):
    """
    Start a game session - only creator can start
    Automatically adds bots if needed to reach 4 players
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        # Verify creator is starting the game
        query = "SELECT game_creator, players, total_players FROM triumphs_game_sessions WHERE game_session_id = %s"
        cursor.execute(query, (game_session_id,))
        game = cursor.fetchone()
        
        if not game or game['game_creator'] != creator_user_id:
            return False
            
        # Check current players
        players = json.loads(game['players']) if game['players'] else []
        current_player_count = len(players)
        
        # Add bots if needed to reach 4 players
        bots_to_add = max(0, 4 - current_player_count)
        
        if bots_to_add > 0:
            # Add bot users (assuming bot IDs start from 9999 or some convention)
            for i in range(bots_to_add):
                players.append(9999 + i)  # Simple bot ID convention
        
        # Update game state to active
        update_query = """
        UPDATE triumphs_game_sessions 
        SET game_state = 'active', 
            players = %s, 
            total_players = %s,
            game_start_time = %s
        WHERE game_session_id = %s
        """
        
        players_json = json.dumps(players)
        cursor.execute(update_query, (players_json, len(players), datetime.now(), game_session_id))
        connection.commit()
        
        return True
        
    except mysql.connector.Error as err:
        print(f"Error starting game session: {err}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_game_session(game_session_id):
    """
    Get details of a specific game session
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM triumphs_game_sessions WHERE game_session_id = %s"
        cursor.execute(query, (game_session_id,))
        game = cursor.fetchone()
        
        return game
        
    except mysql.connector.Error as err:
        print(f"Error fetching game session: {err}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def end_game_session(game_session_id):
    """
    End a game session
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor()
        
        query = "UPDATE triumphs_game_sessions SET game_state = 'ended' WHERE game_session_id = %s"
        cursor.execute(query, (game_session_id,))
        connection.commit()
        
        return True
        
    except mysql.connector.Error as err:
        print(f"Error ending game session: {err}")
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_active_games():
    """
    Get all active game sessions
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT * FROM triumphs_game_sessions WHERE game_state = 'active'"
        cursor.execute(query)
        games = cursor.fetchall()
        
        return games
        
    except mysql.connector.Error as err:
        print(f"Error fetching active games: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_user_game_sessions(user_id):
    """
    Get all game sessions a user has participated in (either created or joined)
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='dkgsunll_buddywilde_db',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT * FROM triumphs_game_sessions 
        WHERE game_creator = %s OR players LIKE %s
        """
        
        players_json_pattern = f'%{user_id}%'
        cursor.execute(query, (user_id, players_json_pattern))
        games = cursor.fetchall()
        
        return games
        
    except mysql.connector.Error as err:
        print(f"Error fetching user's game sessions: {err}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

