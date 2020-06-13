import pygame

class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = True
        self.ready = False
        self.id = id
        self.winningPattern = ["Green", "Red", "Blue", "Yellow"]
        self.tryingPattern = []
        self.board = [boardInput(0), boardInput(1), boardInput(2), boardInput(3), boardInput(4), boardInput(5)]
        self.wins = [0,0]
        self.ties = 0
        self.turnNumber = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, attempt):
        self.tryingPattern = []

        if player == 0:
            self.p1Went = True
            self.p2Went = False
        else:
            self.p2Went = True
            self.p1Went = False

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        winner = -1
        if self.tryingPattern == self.winningPattern and self.p1Went == True:
            winner = 0
        elif self.tryingPattern == self.winningPattern and self.p2Went == True:
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

class boardInput:
    def __init__(self, number):
        self.colors = []
        self.number = number

