# INTRODUCTION

## Purpose: 
This document outlines the system requirements for my 1500s style triumphs card game app that I am building as a tool 
to help promote the movie I am making. I am building the game in python using the django framework. Full disclosure - 
I realize it would be easier for me to make the game in javascript, sparing me the potential cost of the python runtime
environment server (which my hosting provider cannot accomodate) BUT idgaf, I have ulterior motives, namely I am on a quest to 
become a bonified pythonista, and see this as an opportunity for a practice project. 

## Scope:
This game integrates into a wordpress website that I have already partially built, which handles user authentication 
in the php. The scope of the game itself will include game logic implementation, database management, front-end presentation 
with animated displays of the cards of which there are 78 and each one is an absolute fucking masterpiece of art work created 
by my partner, star, and co-producer on the film Lee-Anne Langley. The game supports both human and bot players in various 
configurations of multiplayer scenarios. 

## Definitions: 
- **SRS:** System Requirements Specification 
- **DJango:** Web Framework for Python 
- **MariaDB:** Open-Source relational database management system
- **WordPress:** Content management system 
- **Plesk:** Web hosting control panel (via my hosting provider which is websavers) 
- **Visconti-Sforza:** The original 1500s deck of 78 cards on which the game is based
- **Trick:** Refers to a round or hand in the game, a game consists of the players playing "tricks" until they 
  have no remaining cards left to play, ending the game. 

# DESCRIPTION 

## Perspective 
The game will be integrated into the website and be available for users who are registered and have verified their email. 
As I mentioned before this will be handled via the sites php. The game will be integrated through a DJango back end and will 
interface with an existing mariaDB database the site uses. The game system will maintain its own unique tables for 
game-specific data. 

## Product Functions
- User authentication/authorization 
- Game Session management (waiting for human players to join before initializing a game or adding bots to begin immediately
  decided by the creator of the game instance. 
- Card Deck creation 
- Shuffling the cards into a random order and implementing the random prize distribution system via bonus cards
- Dealing the cards to begin the game  
- Keep a connection to several tables in the database 

## User Classes 
- **Verified Users:** only verified users can access the game portal in order to start or join a game. 
- **Game creator:** The user who starts a game instance that people can either join, or is started immediately with bots, 
  the user who created the game is the Game creator, this is really only relevant during the waiting period as only the 
  game creator can choose to cease waiting for other players to join and start automatically with the empty 
  chairs filled by bots. Additionally, we will track the number of games specific users have started so we can see who is most
  active in creating games, and potentially reward this behavior in the future.
- **Game PLayer:** Any user who has simply joined a game to play 
- ""Bot Player:** A bot who is playing with one or more human players and possibly a number of other bots. 

## Operating Environment 
- **Front-End:** Wordpress Website with PHP, Javascript, and CSS
- **Back-End:** Python Django framework 
- **Database:** MariaDB (plesk managed) 
- **Hosting:** Websavers with Plesk control panel (may change) 
- **Python runtime env:** TBD

## Assets
- **The Cards:** 78 PNG images hosted in the wordpress media files and referenced via url 
- **Dealing intro video:** An mp4 video of Johnny dealing the cards to the user will be played, the video will transition
  to a top down view of the table showing the users pile that they have been dealt, their won trick pile as the game progresses, 
  and the game play area where tricks are played (cards being played out onto one another, with some simple animation effect) 

# Functional Requirements

## User management
  Users must be successfully logged in and verified on the website in order to play the game. The game must be able to 
  read and understand attributes of the users session; their user_id, and session_id. 

## Game Logic 
  - Creates a deck of the normal 78 cards 
  - Shuffles the deck 
  - Creates the bonus prize cards based on the contents of the list of currently available prizes
  - adds bonus prize cards into the deck (or not) based on pre-defined odds that bonus cards of certain prize types
  will appear 
  - Deals cards , 18 to each player in the game 
  - A game will have 4 players total, regardless of whether there is 1 human player or 4, the remainder would be filled
  by bots to ensure a game always has 4 players
  - Plays a trick, tracking which cards are in the players dealt_pile and won_trick_pile as tricks end and begin throughout
  the game 
  - When all tricks have been played and the game ends, the scores will be processed in the database

## Front-End Presentation
  - The cards in a users hand will be displayed for them on a table background
  - They will also see the other players cards come out in the game play area
  - They will see the winning card identified with an animation around its border 
  - They will see the cards slide together and then dissapear out of frame together as a message is displayed 
  indicating how many points were added to the winning players won_tricks_pile 

# General Requirements

## Performance requirements: 
- Responsive game interface 
- Efficient database queries for real time game updates
- Smooth card animation performance 

## Security Requirements 
- User authentication 
- Session management 
- Basic security to pretect the database login credentials from being discoverable by a user to steal points or prizes
- Basic security to prevent users from cheating (potentially discovered in later testing) 

## Reliability Requirements 
- The game should always be up and available to play but if there is some intermittent downtime occassionally that 
can be tolerated to some degree, additionally the game will likely only be played consistently during the period that
the film is being promoted and prizes are actively being awarded through bonus cards, once the campaign has ended the game 
may stay up , may be shelved and brought back later, or perhaps left up for people to just play for fun depending on interest,
cost feasibility, etc. 
- Database back ups are essential but that is more so related to teh reliability of the website itself rather than the game 
- Error handling should be graceful, never causing the game to freeze on a user. 

## Compatibility Requirements
- Browser Compatibility with existing wordpress site 
- Database compatibility with MariaDB 
- Integration with Plesk control panel 
- Python runtime environment must integrate with existing set up whether self-hosted or through a service 

# System Architechture 
## Software Architechture
- **FRONT-END:** Wordpress with embedded Python DJango Application 
- **BACK-END:** Python DJango framework with MariaDB database hosted on websavers and managed in Plesk 
- **Database Layer:** MariaDB with existing wordpress users table and new game tables 
- **API Layer:** RESTful interfaces for communication between components 
## Data Flow 
- User authentication details through wordpress php and the sites database 
- Game portal access is granted through the authenticated wordpress session 
- DJango application processes the game logic 
- Database interactions 
- Front end presentations 

