import random
from metaheuristics import DGO, GBO, RTBGO, TWO

class Player:
    def init(self, id, num_tokens):
        self.bonus = 0
        self.id = id
        self.tokens = [{'position': 0, 'score': 0} for _ in range(num_tokens)]

    def play(self, num_tokens_to_update):
        print("[+] Throwing dice...")
        dice_roll = random.randint(1, 6)
        print("You rolled a ", dice_roll)
        num_tokens_to_update = len(self.tokens) // 6
        tokens_to_update = random.sample(self.tokens, num_tokens_to_update)

        for token in tokens_to_update:
            if dice_roll == 6:
                token['position'] += dice_roll
                token['score'] += 1
            else:
                token['position'] += dice_roll

        return dice_roll

class LudoGame:
    def init(self, num_tokens, num_of_players):
        self.players = [Player(i+1, num_tokens) for i in range(num_of_players)]

    def play_game(self):
        while not self.game_over():
            for player in self.players:
                dice_roll = player.play()
                if dice_roll == 6:
                    self.bonus = self.bonus + 1
                    continue
                    if self.bonus <= 2:
                        for i in range(self.bonus):
                            player.play()
                        break

    def game_over(self):
        for player in self.players:
            for token in player.tokens:
                if token['score'] >= 5:
                    return True
        return False

    def normalize(position):
        return np.sum(solution[0])