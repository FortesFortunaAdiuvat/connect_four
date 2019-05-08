from random import randint

class ConnectFour(object):

    def __init__(self):
        self.grid = {
            0: [0, 0, 0, 0, 0, 0],
            1: [0, 0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0, 0],
            3: [0, 0, 0, 0, 0, 0],
            4: [0, 0, 0, 0, 0, 0],
            5: [0, 0, 0, 0, 0, 0],
            6: [0, 0, 0, 0, 0, 0]}
        self.winner = None
        self.gameIsComplete = False
        # A playing board object to track which grid cells have been played
        # grid 2D array with seven columns and 6 elements

    def drop_token(self, player_uid):
        # loop through rows to see if column is full to pick a new column
        print(f'player {player_uid} is playing their turn...')
        turn_complete = False
        while turn_complete is False:
            # pick a random column between 0 and 6 to drop token, if all rows are already full choose another column
            chosen_column = randint(0, 6)
            print(f'chosen_column is {chosen_column}')
            # chosen_column # loop through the rows to find the cell that the token falls into or if it is full, pick a new column
            for i in range(0, 6):
                # Find the top most row to drop the token into...
                if self.grid[chosen_column][i] == 0:
                    self.grid[chosen_column][i] = player_uid
                    turn_complete = True
                    break
                elif self.grid[chosen_column][i] == 5 & turn_complete is False:
                    # column is full, must choose another column to drop token in
                    print("column is full, choosing another column...")
                    break

            turn_complete = True

        self.printCurrentBoard()

    def check_end_game_conditions(self):
        print("checking end game conditions")
        for i in range(0, 7):
            for j in range(0, 6):
                # Check Horizontal winning condition
                try:
                    if (self.grid[i][j] == self.grid[i][j+1] == self.grid[i][j+2] == self.grid[i][j+3]
                            & self.grid[i][j] != 0 & self.grid[i][j+1] != 0 & self.grid[i][j+2] != 0 & self.grid[i][j+3] != 0):
                        self.gameIsComplete = True
                        self.winner = self.grid[i][j]
                        print(f'Winner is player{self.winner} with a horizontal connect 4')
                        exit(1)
                except IndexError as error:
                    # print("range exceeded for row, testing next row")
                    continue

                # Check Vertical winning condition
                try:
                    if (self.grid[i][j] == self.grid[i+1][j] == self.grid[i+2][j] == self.grid[i+3][j]
                            & self.grid[i][j] != 0 & self.grid[i+1][j] != 0 & self.grid[i+2][j] != 0 & self.grid[i+3][j] != 0):
                        self.gameIsComplete = True
                        self.winner = self.grid[i][j]
                        print(f'Winner is player{self.winner} with a Vertical connect 4')
                        exit(1)
                except IndexError as error:
                    continue
                except KeyError as error:
                    continue

                # Check upward diagonal winning condition
                try:
                    if (self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] == self.grid[i+3][j+3]
                            & self.grid[i][j] != 0 & self.grid[i+1][j+1] != 0 & self.grid[i+2][j+2] != 0 & self.grid[i+3][j+3] != 0):
                        self.gameIsComplete = True
                        self.winner = self.grid[i][j]
                        print(f'Winner is player{self.winner} with an Upward diagonal connect 4')
                        exit(1)
                except IndexError as error:
                    continue
                except KeyError as error:
                    continue

        # Check downward diagonal winning condition
        for i in range(7, 0):
            for j in range(6, 0):
                try:
                    if (self.grid[i][j] == self.grid[i-1][j-1] == self.grid[i-2][j-2] == self.grid[i-3][j-3]
                            & self.grid[i][j] != 0 & self.grid[i-1][j-1] != 0 & self.grid[i-2][j-2] != 0 & self.grid[i-3][j-3] != 0):
                        self.gameIsComplete = True
                        self.winner = self.grid[i][j]
                        print(f'Winner is player{self.winner} with a Downward diagonal connect 4')
                        exit(1)
                except IndexError as error:
                    continue
                except KeyError as error:
                    continue

        #Check if board is entirely full
        fullBoard = True  # If any empty cells are found, this will turn False
        for i in range(0, 7):
            for j in range(0, 6):
                if self.grid[i][j] == 0:
                    print("Game still has potential")
                    fullBoard = False
                    continue
        if fullBoard is True:
            print("Game has ended in a tie")
            #self.printCurrentBoard()
            exit(1)

        if self.gameIsComplete is True:
            return True
        else:
            return False

    def printCurrentBoard(self):
        for i in range(0, 7):
            for j in range(0, 6):
                print(f'Column {i}: {self.grid[i][j]}')

class player(object):
    def __init__(self, uid):
        self.uid = uid
        return

    def make_move(self, board):
        board.drop_token(self.uid)
        print(self.uid)
        return


def main():
    # Each player takes turns until check_winning_condition is satisfied
    print("Connect4 Game")
    game = ConnectFour()
    playerOne = player(1)
    playerTwo = player(2)
    whosTurnIsIt = 1
    while game.gameIsComplete is False:
        if whosTurnIsIt == 1:
            print("player 1, it is your turn.")
            playerOne.make_move(game)
            game.check_end_game_conditions()
            whosTurnIsIt = 2
        elif whosTurnIsIt == 2:
            playerTwo.make_move(game)
            game.check_end_game_conditions()
            whosTurnIsIt = 1

# TODO: update ConnectFour Object to support indexing for the below tests
def test_board_creation():
    # Does the board have the proper number of columns and rows when created?
    creation_board_test = ConnectFour()
    row_counter = 0; column_counter = 0; rowsToCount = True; columnsToCount = True
    while rowsToCount is True:
        if creation_board_test[row_counter][column_counter] == 0:
            print(creation_board_test[row_counter][column_counter])
            rowsToCount += 1



    return

def test_player_taking_a_turn():
    # When a player makes a move and drops a token, does the correct grid cell get marked?
    testPlayer = player(1)
    testBoard = ConnectFour()
    testPlayer.make_move(testBoard)

    return

def test_board_is_full_end_game_scenario():
    # If all of the grid cells are filled, does the game correctly report this as a tie?
    return

# def test_if_player_won_horizontally():
#     horizontal_winning_game = ConnectFour()
#     horizontal_winning_game[0][0] = 1; horizontal_winning_game[0][1] = 1; horizontal_winning_game[0][2] = 1; horizontal_winning_game[0][3] = 1
#     assert horizontal_winning_game.check_end_game_conditions()
#     return

def test_if_player_won_vertically():
    return

def test_if_player_won_with_upward_diagonal():
    return

def test_if_player_won_with_downward_diagonal():
    return

if __name__ == '__main__':
    main()

