from art import logo, game
# global game
tic_tac_toe = {
    '1': 3,
    '2': 9,
    '3': 15,
    '4': 40,
    '5': 46,
    '6': 52,
    '7': 78,
    '8': 84,
    '9': 90
}
player1 = []
player2 = []
filled = []
win_ways = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [2, 5, 8], [1, 4, 7], [3, 6, 9]]


def game_done(player):
    if player == "player1":
        for way in win_ways:
            count = 0
            for i in way:
                if i in player1:
                    count += 1
                    if count == 3:
                        print(f"Congrats {player} won the game ")
                        return True
                else:
                    break

    elif player == "player2":
        for way in win_ways:
            count = 0
            for i in way:
                if i in player2:
                    count += 1
                    if count == 3:
                        print(f"Congrats {player} won the game ")
                        return True
                else:
                    break


def ask_and_fill(player, phase):
    if player == "player1":
        inputs = input(f"{player} Make Your Move. ")
        ttt = list(phase)
        if inputs in filled:
            print("Can't Make this Move. ")
            return ask_and_fill("player1", phase)
        elif inputs in tic_tac_toe:
            player1.append(int(inputs))
            filled.append(inputs)
            ttt[tic_tac_toe[inputs]] = 'X'
            phase = "".join(ttt)
            return phase
        else:
            print("Wrong Input Given!")
            return ask_and_fill("player1", phase)
    else:
        inputs = input(f"{player} Make Your Move. ")
        ttt = list(phase)
        if inputs in filled:
            print("Can't Make this Move. ")
            return ask_and_fill("player2", phase)
        elif inputs in tic_tac_toe:
            player2.append(int(inputs))
            filled.append(inputs)
            ttt[tic_tac_toe[inputs]] = 'O'
            phase = "".join(ttt)
            return phase
        else:
            print("Wrong Input Given!")
            return ask_and_fill("player2", phase)


def play_again():
    do = input("Do You want to play again 'y' or 'n'.  ").upper()
    if do == "Y":
        return True
    else:
        return False


def gameplay(blueprint):
    global player1
    global player2
    global filled
    player1_turn = True
    player2_turn = False
    game_is_on = True
    while game_is_on:
        play = blueprint
        if player1_turn:
            # print(player2)
            if game_done("player2"):
                game_is_on = False
                if play_again():
                    player1 = []
                    player2 = []
                    filled = []
                    print(game)
                    gameplay(game)
                else:
                    exit()
            else:
                if len(filled) == 9:
                    print(" Game Done. Draw ")
                    if play_again():
                        player1 = []
                        player2 = []
                        filled = []
                        print(game)
                        gameplay(game)
                    else:
                        exit()

                play = ask_and_fill("player1", play)
                print(play)
                player2_turn = True
                player1_turn = False
        else:
            # print(player1)
            if game_done("player1"):
                game_is_on = False
                if play_again():
                    player1 = []
                    player2 = []
                    filled = []
                    print(game)
                    gameplay(game)
                else:
                    exit()
            else:
                if len(filled) == 9:
                    print(" Game Done. Draw ")
                    if play_again():
                        player1 = []
                        player2 = []
                        filled = []
                        print(game)
                        gameplay(game)
                    else:
                        exit()

                play = ask_and_fill("player2", play)
                print(play)
                player1_turn = True
                player2_turn = False
        blueprint = play

#
# if "__name__" == "__main__":
#     print(logo)
#     # print(game)
#     # gameplay(game)


print(logo)
print(game)
gameplay(game)
