**Global Variables:**

* `board`: This list stores the game state, where each element represents a position on the board ("-", "X", or "O").
* `game_on`: This boolean variable indicates if the game is still ongoing (True) or over (False).
* `winner`: This variable stores the symbol of the winning player ("X", "O", or None if it's a tie).
* `current_player`: This variable keeps track of whose turn it is ("X" or "O").

**Functions:**

* `display_board()`: This function formats and prints the current board state to the console.

* `play_game()`: This is the main function that initiates the game. It calls `display_board()` to show the initial board, then enters a loop that continues as long as `game_on` is True. Inside the loop, it calls `handle_turn` to handle the current player's move, then checks for a winner or tie using `game_over()`, and finally switches players using `flip_player()`. Once the loop exits (because `game_on` becomes False), it displays a message depending on the outcome (winner or tie).

* `handle_turn(player)`: This function takes the current player's symbol (`player`) as input. It prompts the player to choose a position (1-9), validates the input to ensure it's within the valid range (1-9) and not an already occupied position. Once a valid position is entered, it updates the board state with the player's symbol and then displays the updated board.

* `game_over()`: This function calls `check_win` and `check_tie` to determine the game's status. 

* `check_win()`: This function checks for a winning condition. It utilizes helper functions `check_row`, `check_col`, and `check_diagonals` to check for winning combinations in rows, columns, and diagonals respectively. If a winner is found, it sets the `winner` global variable and sets `game_on` to False to end the game loop.

* `check_row()`, `check_col()`, `check_diagonals()`: These helper functions individually check for winning combinations in rows, columns, and diagonals respectively. They use global variables `game_on` and `winner` to update the game state if a winning condition is found.

* `check_tie()`: This function checks if all positions on the board are filled (no "-" characters) and sets `game_on` to False if it's a tie.

* `flip_player()`: This function simply switches the `current_player` global variable between "X" and "O" for the next turn. 

**Improvements:**

* This code uses global variables to store game state and track the winner and current player. 
* It implements functions to handle specific tasks like displaying the board, handling turns, checking for win/tie, and switching players. 
* It includes validation for user input to ensure valid positions are chosen.
* It checks for ties in addition to wins.

This code provides a more structured and well-organized implementation of the Tic-Tac-Toe game compared to the previous version. 
