# SYTEM OVERVIEW

## System Architechture
The card game system essentially follows a 3 tier architecture:
1. Presentation Layer: Wordpress Website with embedded DJango application
2. Application Layer: DJango Framework will handle game logic
3. Data Layer: MariaDB database integrated with the rkgsunll_buddywilde_db database and its relevant tables

## System Componenets
- Website
- Game Engine
- Database / tables

# DATA DESIGN

## Database schema Design

### Users table (pre existing and is important for reasons beyodn the scope of the game) 

Table: users
Columns: 
- id (primary key) 
- first_name
- last_name
- display_name
- avatar
- email
- verification_code
- password_hash
- receive_email_udpates
- trick_score
- total_score
- badges
- email_verified
- created_at
- updated_at

## Game Specific Tables 

### Triumphs_game_Sessions
Table: triumphs_game_sessions
Columns:
-triumphs_session_id (primary key)
-game_state (enum: waiting, active, ended)
-created_at
-creator_user_id
-updated_at
-players (JSON array of user_ids of players)






