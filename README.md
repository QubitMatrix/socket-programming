# Socket Programming
Multiplayer game using socket programming

## Problem Statement:
Understanding the working of game built on socket programming using TCP and UDP and building our own multiplayer game over a TCP network. 

## Description:
A multiplayer gaming project consisting of two games. Text based Hangman game where one client can choose the word and the other can guess it. Traditional Rock, Paper, Scissors game between two players. The server will act as the meeting point for both the client interactions. The entire project will be done over a TCP network by using welcoming sockets to set up the connections and connection sockets to listen to that client. The concept of threads will be used to support multiplayers to interact with the server without restarting the connection for every move in the game.

## Working
### Server 
The server code consists of two functions- one for hangman and the other for Stone Paper Scissors.   
A TCP socket connection is established with multithreading for managing multiple clients in parallel ensuring that the TCP connections remain active till the game ends. The game of Hangman ends if the client guesses the correct word or he has more than 3 incorrect guesses and in the Game 2, the winner is declared based on their respective points. The client that connects first to server is denoted as Player1 and the subsequent one is Player2. The server here only acts as a medium for the clients to interact.

### Client
When a user runs the client code, a TCP connection is established between the client and the server. The client then chooses the game they wish to play- 1 for Hangman and 2 for Stone Paper Scissor. The two clients then wait for each other moves so that the game can continue.   
HANGMAN: Player 1 in hangman is given the task to choose a word for Player 2 to guess. Player 2 guesses letters in the words, if the letters are present in the word Player one gives the positions. A ‘*’ string will be replaced with the letters in its correct positions.   
STONE PAPER SCISSORS: Player 1 and Player 2 make their move by specifying the option they choose. A point is given to the player that wins that round. The game goes on for 3 tries and the player with the highest points is declared the winner.


## Replicating the setup:
- The entire process of creating the project was documented therefore there are multiple files which are not needed for the final version.
  The project initially started with the idea of creating a game between a client and a server and UDP sockets were used. The second game was added later in version 2.0 . 

  In the final version we turned it into multiplayer game where multiple clients are connected to a central server. For this the entire process had to be changed from UDP to TCP sockets where threads were used for concurrent execution.
- Run `python3 client_multi.py` on the client machines (The IP should b changed in the file to point to the server)
- Run `python3 server_multi.py` on the server machine to set up a central server

## Future Scope
In the project's initial phase, OpenCV was employed to enable webcam-based gameplay for Stone, Paper, Scissors. However this approach had performance issues and was not practical in a scenario of local testing on multiple VMs on a single machine with a single webcam. Additionally the accuracy of the predictions were not meeting the expectations. The resolution of these issues remains a focal point for our project's future enhancements.
