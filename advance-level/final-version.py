import random
from random import randint
import time
import itertools


class TictactoeAbstract:
    """abstract class for tic tac toe game"""

    def __init__(self, empty_board, board, winning_rows, player):
        """create empty board as game begins"""
        self.empty_board = empty_board
        self.board = board
        self.winning_rows = winning_rows
        self.player = player

    def ttt_board(self):
        """draw empty board and get the all the valid index from board"""
        idx = [index for index, value in enumerate(
            list(board)) if value == '0']
        print("!!!!! Welcome to Tic Tac toe game !!!!!\n")
        print("You have to provide input between 1 to 9")
        print(board)
        return idx


class MainTictactoe(TictactoeAbstract):
    """core logic(alg) of ttt game"""
    used_index_list = []
    used_index_list_actuals = []
    updated_board_list = []
    player_places = []
    possible_indexes = []
    position_dict = {1: 1, 2: 5, 3: 9, 4: 24,
                     5: 28, 6: 32, 7: 46, 8: 50, 9: 54}

    def get_actual(self, user_input):
        """convert user input into actual index"""
        if user_input in self.used_index_list:
            print("Alredy occupied its a invalide choice !!!!")
            return False

        elif user_input < 1 or user_input > 9:
            print("Invalide choice!!")
            return False

        else:
            self.used_index_list.append(user_input)
            self.used_index_list_actuals.append(self.position_dict[user_input])
            
            return self.position_dict[user_input]

    def players_move(self, i):
        """ask player to provide move"""
        if i == 0:
            new = list(board)
            self.updated_board_list.append((new))
        user_input = int(input())
        position = self.get_actual(user_input)
        self.player_places.append(position)
        if position:
            latest_board, new_list = self.get_latest_board(
                (self.updated_board_list)[-1], position, self.player[0])
            return new_list

        if not position:
            print("Please enter a valid choice !!!")
            self.players_move(i)

    def system_input(self, i):
        """
        system will provide input here
        x == 'system's inputs will only be available slots'
        """
        if i == 0:
            occupied_places = self.used_index_list
            available_places = [c for c in list(
                range(1, 10)) if c not in occupied_places]
        else:
            available_places = self.check_wining_places()
        x = random.choice(available_places)
        position = self.get_actual(x)

        if position:
            latest_board, new_list = self.get_latest_board(
                (self.updated_board_list)[-1], position, self.player[1])

    def get_latest_board(self, new, position, player):
        """get the latest board"""
        p = player
        if position:
            new_list = new[:position] + list(p) + new[(position+1):]
            latest_board = (
                n.format(*[i for i in new_list if i in ['0', 'X', 'Y']]))
            print(latest_board)
            self.updated_board_list.append(new_list)
            for val in self.winning_rows:
                u = (list(set(self.used_index_list_actuals) - set(self.player_places)))
                if (set(val).issubset(self.player_places)):
                    print("You Won")

                if (set(val).issubset(u)):
                    print("System Won")

            return latest_board, new_list

    def check_wining_places(self):
        """it will check all the possible places"""
        # print(self.winning_rows)
        players_index = self.player_places
        comb = list(itertools.combinations(players_index, 2))
        for x in self.winning_rows:
            for i in comb:
                if (set(i).issubset(x)):
                    self.possible_indexes.append(list(set(x) - set(i))[0])
        for item in self.possible_indexes:
            if item not in self.used_index_list_actuals:
                return [{v: k for k, v in self.position_dict.items()}[item]]

        for f in self.position_dict.items():
            if f[1] not in self.used_index_list_actuals:
                return [f[0]]



n = ('''
{} | {} | {} 
-----------
{} | {} | {}
-----------
{} | {} | {} 
        ''')

board = (n).format(*['0' for x in range(10)])

winning_rows = [
    [1, 5, 9], [24, 28, 32], [46, 50, 54],
    [1, 24, 46], [5, 28, 50], [9, 32, 54],
    [1, 28, 54], [9, 28, 46]
]


player = ['X', 'Y']

start_game = TictactoeAbstract(n, board, winning_rows, player)
start_game.ttt_board()


p1 = MainTictactoe(n, board, winning_rows, player)


def main():
    for i in range(4):
        print("Please provide your move - Player 1: \n")
        p1.players_move(i)

        print("Its System's turn !!!")
        time.sleep(3)
        p1.system_input(i)


if __name__ == '__main__':
    main()
