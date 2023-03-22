class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0
        self.game_level = 1
        self.is_playing = False
    
    def start_game(self):
        self.is_playing = True
        print(f"The game has started. Good luck, {self.player_name}!")
    
    def end_game(self):
        self.is_playing = False
        print(f"The game has ended. Your final score is {self.player_score}.")
    
    def update_score(self, score):
        self.player_score += score
    
    def update_level(self, level):
        self.game_level = level
        print(f"Congratulations! You have reached level {self.game_level}.")
    
    def print_info(self):
        print(f"Player: {self.player_name}")
        print(f"Score: {self.player_score}")
        print(f"Level: {self.game_level}")