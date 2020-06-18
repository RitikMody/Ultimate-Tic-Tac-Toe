# Ultimate-Tic-Tac-Toe

[![](https://img.shields.io/badge/Made_with-python-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-blue?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/  "Visual Studio Code")
<br>
A stategic boardgame for 2 players.<br>
<br>
## Rules:<br>
Each small 3 × 3 tic-tac-toe board is referred to as a local board, and the larger 3 × 3 board is referred to as the global board.<br>

The game starts with O playing wherever they want in any of the 81 empty spots. This move "sends" their opponent to its relative location.< For example, if O played in the top right square of their local board, then O needs to play next in the local board at the top right of the global board. X can then play in any one of the nine available spots in that local board, each move sending O to a different local board.<br>

If a move is played so that it is to win a local board by the rules of normal tic-tac-toe, then the entire local board is marked as a victory for the player in the global board.<br>

Once a local board is won by a player or it is filled completely, no more moves may be played in that board. If a player is sent to such a board, then that player may play in any other board.<br>

Game play ends when either a player wins the global board or there are no legal moves remaining, in which case the game is a draw.<br>
