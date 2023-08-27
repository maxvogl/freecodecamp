# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

"""
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
"""

def player(prev_play, opponent_history=[], n_last_games=5, play_order={}):
    ideal_response = {"R" : "P", "P" : "S", "S" : "R"}
    prediction = "S"  # initial choice "Scissor First"!

    if not prev_play:
        prev_play = prediction
    opponent_history.append(prev_play)

    if len(opponent_history) > (n_last_games - 1):
        last_games = "".join(opponent_history[-n_last_games:])
        play_order[last_games] = play_order.get(last_games, 0) + 1
        potential_plays = ["".join([*opponent_history[-(n_last_games-1):], move])
                           for move in list(ideal_response.keys())]
        
        sub_order = {k : play_order[k]
                     for k in potential_plays
                     if k in play_order
                    }
        
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    return ideal_response[prediction]