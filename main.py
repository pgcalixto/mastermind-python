from mastermind import Player

def main():
    '''Main function.'''

    # instantiates the player, gets the first guess and play
    game_player = Player()
    guess = game_player.get_first_guess()

    print(guess)
    answer = input()

    while answer != '40':
        # parses the answer and gets the next guess
        answer = (int(answer[0]), int(answer[1]))
        guess = game_player.get_next_guess(answer)
        print(guess)
        answer = input()

    print('ganhei')

if __name__ == '__main__':
    main()
