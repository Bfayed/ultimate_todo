# <Bavly Fayed>             <9-28-2023>
# <Assignment 3>
# <spinner winner>

import random
def printTitleMaterial():
    """ This function prints the 'title material' that prints out when the program starts.
    """
    print("Spinner Winner!")
    print()

    
    print("By: <Bavly Fayed>")
    print("[COM S 127 <J>]")
    print()

def initialChoice():
    """ This function allows the player to make various choices when starting the game. This is an 
    example of the 'do-while' pattern.

    :return String: The choice the player has made when starting the program to [p]lay the game, view the
    [i]nstructions, or [q]uit the program..
    """
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    """ This function allows the player to choose whether they will play against another
    human, or play against the computer.

    :return Integer: The number of players in the game.
    """
    numPlayers = 0
    choice = int(input("Enter the number of players [1] or [2]: "))
    while choice != 1 and choice != 2:
        print("ERROR: Please enter '1' or '2'")
        choice = int(input("Enter the number of players [1] or [2]: "))
    
    return numPlayers

def wait():
    """ This function has the computer 'wait' until the [Enter] key is pressed. This allows 
    for better 'readability' in the final output.
    """
    input("Press [Enter] To Continue...")
    print()

def printBanner():
    """ Prints the 'banner' between each round of the game so that the output text does not 
    get too 'messy.'
    """
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def printPoints(numPlayers, points):
    """ This function prints the number of points a certain player currently has.

    :param Integer playerNum: The player whose points are being displayed.
    :param Integer points: The number of points to be displayed
    """
    print("* Player {0} Has {1} Points!".format(numPlayers, points))
    print()

def wagerPointsHuman( playerNum , points):
    """ This function uses the 'do-while' pattern to take in input for the number of points to be wagered. It checks to
    make sure that the player has entered a valid amount of points. Meaning, the player cannot wager more points than
    they have, nor zero points, nor a negative number of points. The function then returns the wager.

    As there could potentially be two human players, this function requires the playerNum to know which player to include
    in any printouts.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer points: The number of points the specified player currently has.
    :return Integer: The number of points to be wagered.
    """
    wager = 0
    while True:
        try: 
            choice = int(input(f"Player {playerNum}, you have {points} points. How many points would you like to wager? "))
            print(" *keep in mind* it is not possible to wager a negative number or a zero or a higher number than what you have!! ") 
            if choice <= 0: 
                print(" *keep in mind* it is not possible to wager a negative number or a zero or a higher number than what you have!! ")
            # elif choice > points: 
            #     print(" *keep in mind* it is not possible to wager a negative number or a zero or a higher number than what you have!!")
            else: 
                return choice
        except ValueError: 
            print("  *keep in mind* it is not possible to wager a negative number or a zero or a higher number than what you have!! ")

        return wager 

def wagerPointsAI( numPlayers, points):
    """ This function should choose a random number between 1 and the number of points the AI has (inclusive). For example,
    if the computer has 5 points, it can wager either 1, 2, 3, 4, or 5. This function should include a printout similar to 
    what is printed when the human wagers points.

    :param Integer playerNum: The player to include in any printouts. While this will usually be 2, including this value allows 
                              for a future version of the game with 2 computer players.
    :param Integer points: The number of points the specified player currently has.
    :return Integer: The number of points to be wagered.
    """
    
    if points <= 1:    
        return min(1, points)
    wager = random.randint(1, points)
    print(f"Player {numPlayers} or (AI) wagers {wager} points.")
    return wager 


def generateTargetValue(numSpinners, spinnerLow, spinnerHigh):
    """ This function generates the 'target value' that the players try to match. This number is generated by summing together
    random values between 'spinnerLow' and 'spinnerHigh' (inclusive), produced by a random number of spinners, between 1 and 
    numSpinners (inclusive). For example, if there are 3 spinners, and a spinner can have values between 1 - 3, then the target 
    value would be the summation of 1-3 random values between 1 and 3
    (inclusive).

    :param Integer numSpinners: The number of spinners used in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The target value generated by summing together 'numSpinners' number of random numbers between 'spinnerLow' and
                     'spinnerHigh' (inclusive).
    """
    target = 0
    num_selected_spinners = random.randint(1, numSpinners + 1)
    for i in range(num_selected_spinners): 
        random_value = random.randint(spinnerLow , spinnerHigh + 1)
        target += random_value 
    return target

def getSpinnerChoiceHuman(numPlayers, target, numSpinners, spinnerLow, spinnerHigh):
    """ This function gets the number of spinners that the human wants to spin. It should print out the 'target value' that the player
    is trying to match, as well as the values that a spinner can produce (ex: 1 - 3), and the number of spinners that can be spun. The
    player cannot pick more spinners than are in the game, nor can they pick zero spinners, nor can they pick a negative number of spinners.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer target: The 'target value' the player is trying to match.
    :param Integer numSpinners: The total number of spinners in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The number of spinners the player chooses to spin.
    """
    spinnerChoice = 0
    print(f"Player {numPlayers}, your target is {target}.")
    print(f"Each spinner can produce values between {spinnerLow} and {spinnerHigh}.")
    print(f"There are {numSpinners} spinners available.")
    
    while True: 
        user_input = input(f"Player {numPlayers}, how many spinners would you like to spin (between 1 and {numSpinners})? ")
        if user_input.isdigit():
            spinnerChoice = int(user_input)
            if 1 <= spinnerChoice <= numSpinners:
                return spinnerChoice
            else:
                print(f"Please enter a number between 1 and {numSpinners}.")
        else:
            print("Invalid input. Please enter a valid number.")
        return getSpinnerChoiceHuman

def getSpinnerChoiceAI(numPlayers, target, numSpinners, spinnerLow, spinnerHigh):
    """ This function gets the number of spinners that the computer wants to spin. This number should be a randomly generated value
    between 1 and numSpinners (inclusive). It should print out text similar to what the 'getSpinnerChoiceHuman()' function produces.

    :param Integer playerNum: The player to include in any printouts. While this will usually be 2, including this value allows 
                              for a future version of the game with 2 computer players.
    :param Integer target: The 'target value' the computer is trying to match. The computer does not take this value into account when
                           choosing the number of spinners - it should be used for printouts, however.
    :param Integer numSpinners: The total number of spinners in the game.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The number of spinners the computer chooses to spin.
    """
    spinnerChoice = 0
    spinnerChoice = random.randint(numSpinners + 1)
    
    print(f"Player {numPlayers}, your target is {target}.")
    print(f"Each spinner can produce values between {spinnerLow} and {spinnerHigh}.")
    print(f"There are {numSpinners} spinners available.")
    print(f"Computer (Player {numPlayers}) chooses to spin {spinnerChoice} spinner(s).")
    
    return spinnerChoice



def spinSpinners(numPlayers, spinnerChoice, target, spinnerLow, spinnerHigh):
    """ This function can be used for either human or computer players, and it calculates the summed values of the number of
    spinner spins. For example, if the player chooses to spin 3 spinners, and these spinners can have values between 1 and 3,
    the player could spin values of 2, 3, and 1 for a total of 6. This is the value the function would return.

    This function should print out the results of each spin as each spin is spun. The function should then print the sum of 
    all the spins and the target value once all the spins are complete.

    Please note - the winner of the round is *not* calculated here - only the spinner totals.

    :param Integer playerNum: The player to include in any printouts. Can be 1 or 2.
    :param Integer spinnerChoice: The number of spinners the player wishes to spin.
    :param Integer target: Use this value in the printout so the user can compare what they spun compared to the target.
    :param Integer spinnerLow: The smallest value a spinner can generate.
    :param Integer spinnerHigh: The highest value a spinner can generate.
    :return Integer: The sum of all the spinner spins.
    """
    spinTotal = 0
    print(f"Player {numPlayers} is spinning {spinnerChoice} spinner(s).")

    for i in range(spinnerChoice):
        spinVal = random.randint(spinnerLow, spinnerHigh)
        print(f"Spinner {i + 1} result: {spinVal}")
        spinTotal += spinVal

    print(f"Player {numPlayers} spun a total of {spinTotal}. Target value: {target}")

    return spinTotal
 
def updatePoints(player1Points, player2Points, winner, player1Wager, player2Wager):
    """
    Update the points of both players based on the outcome of the round.

    Args:
    player1Points (int): Points of player 1.
    player2Points (int): Points of player 2.
    winner (str): The winner of the round ("Player 1", "Player 2", or "Draw").
    player1Wager (int): Wager made by player 1 in the round.
    player2Wager (int): Wager made by player 2 in the round.

    Returns:
    tuple: Updated points for player 1 and player 2.
    """
    if winner == "Player 1":
        player1Points += player1Wager
        player2Points -= player2Wager
    elif winner == "Player 2":
        player1Points -= player1Wager
        player2Points += player2Wager

    player1Points = max(player1Points, 0)
    player2Points = max(player2Points, 0)

    return player1Points, player2Points


def calculateRoundWinner(player1SpinTotal, player2SpinTotal, target):

    if abs(player1SpinTotal - target) < abs(player2SpinTotal - target):
        return "Player 1"
    elif abs(player2SpinTotal - target) < abs(player1SpinTotal - target):
        return "Player 2"
    else:
        return "Draw"


def gameIsOver(player1Points, player2Points):
    return player1Points <= 0 or player2Points <= 0

def main():
    """ This is the main function that executes when the game is started from the terminal. It contains all of the logic/states
    necessary to play the game.
    """
    running = True
    while running:
        SPINNER_LOW = 1
        SPINNER_HIGH = 3
        NUM_SPINNERS = 3
        INITIAL_POINTS = 10
        player1Points = INITIAL_POINTS
        player2Points = INITIAL_POINTS
        printTitleMaterial()

        while running:
            choice = initialChoice()
            if choice == "p":

                numPlayers = chooseNumPlayers()
                

                while True:
                    printBanner()
                    target = generateTargetValue(NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    print("Expected values between 3-9 Actual value: {0}".format(target))

                    chooseNumPlayers()
                    initialChoice()
                    chooseNumPlayers()
                    wait()
                    printBanner()
                    printPoints(numPlayers, player1Points)

                    human_points = wagerPointsHuman(1, player1Points)
                    wagerPointsAI(numPlayers )
                    generateTargetValue(NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    getSpinnerChoiceHuman(target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                   
                    getSpinnerChoiceAI(numPlayers, target, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    spinSpinners(numPlayers, NUM_SPINNERS, target, SPINNER_LOW, SPINNER_HIGH) 
                    calculateRoundWinner(player1SpinTotal, player2SpinTotal , target)



                    if player1Points <= 0 or player2Points <= 0:
                        print("Game Over!")
                        printPoints(player1Points, player2Points)
                        break
                    else:
                        print("End of the round.")

            elif choice == "i":
                print("The user selects a game between one or two players. A one player game has the user play against the computer. A two player game has two users play against one another. The players start the game with a certain number of 'points.' The game is divided into 'rounds.' At the start of the 'round,' the computer generates a 'target value.' This is the value that the players try to match. At the start of the 'round,' each player 'wagers' a certain number of 'points.' Players cannot 'wager' more 'points' than they have. Nor can they 'wager' zero (0) 'points.' Nor can they 'wager' a negative number of 'points.' Then each player decides how many 'spinners' to spin. Each spin adds its value to a final 'spin value' for the round. Players can not spin more spinners than are available to be spun. Nor can the spin zero (0) spinners. Nor can they spin a negative number of spinners. After each player spins their 'spinners,' their 'spin value' is compared against the 'target value.' The player who gets their 'spin value' closest to the 'target value' is the winner of the round. If both players 'spin value' are equally distant from the 'target value' the round is a 'draw.' Once the winner is decided, 'points' are added and subtracted from each player's score. The winning player gets their wager amount added to their score. The losing player gets their wager amount subtracted from their score. The game continues until one player is completely out of 'points.")
            
            elif choice == "q":
                print("why? just try a round please I wokred really hard on it!")
                running = False
                print("Goodbye!")
            else:
                print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
                quit()

if __name__ == "__main__":
    main()
