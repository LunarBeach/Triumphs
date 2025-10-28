# INTRODUCTION

## Purpose: 
This document serves as a unified specification for the card game application, integrating all functional and non-functional requirements into a single coherent document for development and implementation purposes.
## Project overview:
The card game application will be built using Python Django framework and integrated with an existing WordPress website. The system will implement a strategic card game based on historical Visconti-Sforza deck with modern web technologies and database management.

# TECHNICAL SPECIFICATIONS

## Development Environment 
- **Framework:** DJango (verison to be determined)
- **Language:** Python 3.8 
- **Database:** MariaDB (version to be updated later)
- **Hosting:** Websavers with Plesk control panel for the DB and website
- **Python runtime env hosting:** TBD
- **Front-End:** PHP, Javascript, CSS

## Database schema
- **Primary DB:** rkgsunll_buddywilde_db
- **user table:** users
- **Game tables:** Game instances will be able to create, update, and delete tables for game session management
- **Connection:** DB username is rkgsunll_buddy

# Game Data Model

## Game_session:
- session_id
- players (many-to-many relationship)
- game_state
- created_at
- updated_at
- game_creator (a user_id)

## Player:
- user_id (foreign key to users table)
- score
- dealt_pile
- won_tricks_pile
- is_bot

## Card:
- card_id
- card_type
- trick_value
- point_value
- suit
- prize_id (null for a regular card)
- image_path

# IMPLEMENTATION REQUIREMENTS

## Modular Design
- **Card Creation Module:** .py file for deck creation , prize card decisions, shuffling into a game deck that will be passed to the dealing module.
- **Dealing Module:** .py file that will distribute 18 cards to each player randomly from the game deck
- **Trick Module:** .py file for the trick play logic as new tricks are played, ending when all the players have played their final hand card.
- **Main Module:** .py file that initializes a game session into a waiting_state , then into an active state where it will call the card creation module, the dealing module, the trick module, and finally end the game and handle updating each human players total_points value in the users table of the database. 
