player_history= []
first_play = prev_player_move = 'S'
bot_list = [ False, False, False,False]
counter = [0]
counter_response = { 'P' : 'R', 'R' : 'S', 'S' : 'P'}
play_order = [{
    "RR" : 0, 
    "RP" : 0, 
    "RS" : 0, 
    "PR" : 0, 
    "PP" : 0, 
    "PS" : 0, 
    "SR" : 0, 
    "SP" : 0, 
    "SS" : 0, 
    }]

def player ( prev_opponent_play, opponent_history = []):
    global player_history, prev_player_move, bot_list, counter_response, play_order
    opponent_history.append(prev_opponent_play)
    player_history.append(prev_player_move)

    #quincy
    if(len(set(bot_list)) == 1 and opponent_history[-5:] == [ 'R', 'P', 'P', 'S', 'R']):
        bot_list[0] = True
    
    if(bot_list[0]):
        if(len(opponent_history) % 1000 == 0):
            bot_list = [False, False, False,False]
            opponent_history.clear()

        counter[0] += 1
        choices = ["P", "P", "S", "S", "R"]
        return choices[counter[0] % len(choices)]

    #abbey and mrugesh
    if(len(set(bot_list)) == 1  and opponent_history[-5:] == ['P', 'P','R','R','R']):
        bot_list[1]= True

    if(bot_list[1]):
        last_two = ''.join(player_history[-2:])
        if(len(last_two) == 2):
            play_order[0][last_two] += 1
        potential_plays = [
            prev_player_move + 'R', 
            prev_player_move + 'P',
            prev_player_move + 'S',
            ]
        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
            }
        prediction = max(sub_order, key=sub_order.get)[-1:]

        if(len(opponent_history) % 1000 == 0):
            bot_list = [False, False, False, False]
            opponent_history.clear()
            play_order = [{
              "RR" : 0, 
              "RP" : 0, 
              "RS" : 0, 
              "PR" : 0, 
              "PP" : 0, 
              "PS" : 0, 
              "SR" : 0, 
              "SP" : 0, 
              "SS" : 0, 
              }]
        prev_player_move = counter_response[prediction]
        return counter_response[prediction]

    #kris
    if(len(set(bot_list)) == 1  and opponent_history[-5:] == ['P', 'R','R','R','R']):
        bot_list[2]= True

    if(bot_list[2]):
        if prev_player_move == '':
            prev_player_move = "S"
        prev_player_move = counter_response[prev_player_move]
        return prev_player_move

    return prev_player_move

