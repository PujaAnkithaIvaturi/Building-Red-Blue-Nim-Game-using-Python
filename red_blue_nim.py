import sys

def evaluate_score(red, blue, maxi):
    score = 2 * red + 3 * blue
    if maxi:
        return -score
    return score

def updated_piles(color_0_red_1_blue, red_m, blue_m):
    piles = [red_m - 1 if color_0_red_1_blue == 0 else red_m, blue_m - 1 if color_0_red_1_blue != 0 else blue_m]
    return piles[0], piles[1]

def minmax_by_depth_limit(red_pile, blue_pile, depth, alpha, beta, maxi):
    if depth == 0 or red_pile == 0 or blue_pile == 0:
        return evaluate_score(red_pile, blue_pile, maxi)
    depth = depth - 1
    if maxi:
        opti_score = -sys.maxsize
        for color_0_red_1_blue, number_of_marbles_left in [(0, red_pile), (1, blue_pile)]:
            if number_of_marbles_left > 0:
                red, blue = updated_piles(color_0_red_1_blue, red_pile, blue_pile)
                updated_score = minmax_by_depth_limit(red, blue, depth, alpha, beta, False)
                opti_score = max(opti_score, updated_score)
                alpha = max(alpha, opti_score)
                if beta <= alpha:
                    break
        return opti_score
    else:
        opti_score = sys.maxsize
        for color_0_red_1_blue, number_of_marbles_left in [(0, red_pile), (1, blue_pile)]:
            if number_of_marbles_left > 0:
                red, blue = updated_piles(color_0_red_1_blue, red_pile, blue_pile)
                updated_score = minmax_by_depth_limit(red, blue, depth, alpha, beta, True)
                opti_score = min(opti_score, updated_score)
                beta = min(beta, opti_score)
                if beta <= alpha:
                    break
        return opti_score

def red_blue_nim(red_marbles, blue_marbles, curr_player, depth):
    while red_marbles > 0 and blue_marbles > 0:
        print("Available marbles =====)  Red:Blue = {0}:{1}".format(red_marbles, blue_marbles))
        if curr_player.lower() == 'computer':
            opti_score = -sys.maxsize
            optimal_move = None
            for color_0_red_1_blue, number_of_marbles_left in [(0, red_marbles), (1, blue_marbles)]:
                if number_of_marbles_left > 0:
                    red, blue = updated_piles(color_0_red_1_blue, red_marbles, blue_marbles)
                    updated_score = minmax_by_depth_limit(red, blue, depth, -sys.maxsize, sys.maxsize, True)
                    if updated_score > opti_score:
                        opti_score = updated_score
                        optimal_move = (color_0_red_1_blue, 1)
            if optimal_move[0] == 0:
                print("Computer removed a red marble...")
                red_marbles = red_marbles - 1
            else:
                print("Computer removed a blue marble...")
                blue_marbles = blue_marbles - 1
            curr_player = "Human"
        else:
            humans_input = str(input("Now it is your turn... So, pick a colored marble of your choice (red/blue): "))
            if humans_input.lower() == "red":
                red_marbles = red_marbles - 1
                print("You picked out a red marble...")
                curr_player = "Computer"
            elif humans_input.lower() == "blue":
                blue_marbles = blue_marbles - 1
                print("You picked out a blue marble...")
                curr_player = "Computer"
            else:
                print("Invalid choice. Please select a color between blue and red. Make sure you typed the spellings correct.")
    print("{0} wins the Red Blue Nim game with a grand score of {1} points!!".format(curr_player, 2 * red_marbles + 3 * blue_marbles))
    print("Thank you for playing!")

if len(sys.argv)>2 and int(sys.argv[1])>0 and int(sys.argv[2])>0:
    red_marbles = int(sys.argv[1])
    blue_marbles = int(sys.argv[2])
    if len(sys.argv)>=4:
        start_player = sys.argv[3]
    else:
        start_player = "computer"
    if len(sys.argv)>=5:
        depth_limit = int(sys.argv[4])
    else:
        depth_limit = 20
    red_blue_nim(red_marbles, blue_marbles, start_player, depth_limit)
else:
    print("The input format is : red_blue_nim.py <num-red> <num-blue> <first-player> <depth>")
    print("Contraints: num-red and num-blue should be integers and are greater than 0. first-player: computer/human. depth>1")