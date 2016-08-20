import hit_blow_logic

game = hit_blow_logic.Game()
game.generate_answer_list()

while game.player_victory is False:
    try:
        input_txt = input("> Guess Number:  ")
        game.game_logic(input_txt)
    except AssertionError:
        print("Try again, your guess was invalid.")
