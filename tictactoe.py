from random import randrange
from time import sleep


class TicTacToe:
    board = [[" " for row in range(3)] for column in range(3)]
    mag_square = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    def show_board(self):
        i = 0
        while i < 3:
            for i in range(3):
                print("+-------+-------+-------+")
                print("|       |       |       |")
                print("|   {}   |   {}   |   {}   |".format(self.board[i][0], self.board[i][1],
                                                            self.board[i][2]))
                print("|       |       |       |")
                i += 1
            print("+-------+-------+-------+")

    def player_move(self):
        while True:
            move = int(input("Enter your move: ")) - 1
            if self.check_move(move):
                self.board[int(move / 3)][move % 3] = "X"
                if self.check_win(move):
                    self.show_board()
                    print("*** X won ***")
                    exit()
                break
            else:
                print("\n*** This square is already filled ***")
                continue

    def ai_move(self):
        print("\n\"AI\" move...")
        sleep(0.5)
        while True:
            move = randrange(1, 10) - 1
            if self.check_move(move):
                self.board[int(move / 3)][move % 3] = "O"
                if self.check_win(move):
                    self.show_board()
                    print("*** O won ***")
                    exit()
                break
            else:
                continue

    def check_move(self, move):
        return self.board[int(move / 3)][move % 3] == " "

    def check_win(self, move):
        x = int(move / 3)
        y = move % 3
        if self.board[0][y] == self.board[1][y] == self.board[2][y]:
            return True
        if self.board[x][0] == self.board[x][1] == self.board[x][2]:
            return True
        if x == y and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if x + y == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False


def main():
    board = TicTacToe()
    while True:
        board.show_board()
        try:
            board.player_move()
        except (IndexError, ValueError):
            print("\n*** Wrong input ***")
            continue
        board.ai_move()


if __name__ == "__main__":
    main()
