import numpy as np
import random as rand

count = 1000
start = 3000
pocket = 3000
least_pocket = 3000
init_wager = 10

def menu():
    print("""
        \nWelcome to the Table! Please select from the menu below:
          1. Instructions
          2. Beginner
          3. Intermediate
          4. Run simulations - beginner
          5. Run simulations - intermediate
          6. Exit          
           """)

def selection_check():
    while True:
        user_input = int(input("Selection: "))
        if(user_input <= 6 and user_input >= 0):
            return user_input
        else:
            print("Invalid input. Please enter a value between 0 and 6.\n")

def selection_action(selection):
    log = 0
    while True:
        if selection == 1:
            print_instructions()
        elif selection == 2:
            first_wager, max_bet, max_spins = beginner_variables()
            log_choice = input("Print Logs of each spin? (Y/N): ")
            if log_choice == 'Y':
                log = 1
            walk, profit, total_spins, win_per, max_wager, least_pocket, pos_prof = simulation(first_wager, max_bet,max_spins, logs=log, level=selection)
            win = win_per*total_spins
            lose = (1-win_per)*total_spins
            print("\n\n---------------------\nStatistics:\n---------------------")
            print("Wins: ", win)
            print("Losses: ", lose)
            print("Total: ", win+lose)
            print("Win Percentage = %", (win/(win+lose))*100)
            print("Lose Percentage = %", (lose/(win+lose))*100)
            print("Profit = $", profit)
            print("Final Pocket: $", profit+max_bet)
            print("Largest Wager of the simulation: $", max_wager)
            print("Least amount of $$ in your pocket through out the simulation: $", least_pocket)

        elif selection == 3:
            first_wager, max_bet, max_spins = beginner_variables()
            bankroll_amt, pocket_amt, walkaway = intermediate_variables()
            log_choice = input("Print Logs of each spin? (Y/N): ")
            if log_choice == 'Y':
                log = 1
            walk, profit, total_spins, win_per, max_wager, least_pocket, pos_prof = simulation(first_wager, max_bet, max_spins, log, walkaway, bankroll_amt, pocket_amt, level=selection)
            win = win_per*total_spins
            lose = (1-win_per)*total_spins
            print("\n\n---------------------\nStatistics:\n---------------------")
            print("Wins: ", win)
            print("Losses: ", lose)
            print("Total: ", win+lose)
            print("Win Percentage = %", (win/(win+lose))*100)
            print("Lose Percentage = %", (lose/(win+lose))*100)
            print("Profit = $", profit)
            print("Final Pocket: $", profit+max_bet)
            print("Largest Wager of the simulation: $", max_wager)
            print("Least amount of $$ in your pocket through out the simulation: $", least_pocket)

        elif selection == 4:
            first_wager, max_bet, max_spins = beginner_variables()
            experiment(first_wager, max_bet,max_spins, logs=0, level=2)
        elif selection == 5:
            first_wager, max_bet, max_spins = beginner_variables()
            bankroll_amt, pocket_amt, walkaway = intermediate_variables()
            log = 0
            experiment(first_wager, max_bet, max_spins, log, walkaway, bankroll_amt, pocket_amt, level=3)

        elif selection == 6:
            print("Thanks for playing!")
        if selection != 1 and selection != 6:
            play_again = input("Play again? (Y/N): ")
            play_again = play_again.upper()
            if play_again == 'Y' or play_again == 'YES':
                return 1
            elif play_again == 'N' or play_again == 'NO':
                return 6  
            else:
                print("Invalid format. Playing again:")
                return 1
            return 1
        elif selection == 6:
            return 6
        else: 
            choice = input("See menu again? (Y/N): ")  
            choice = choice.upper()
            if choice == 'Y' or choice == 'YES':
                return 1
            elif choice == 'N' or choice == 'NO':
                return 0  
            else:
                print("Invalid format. Printing menu:")
                return 1       
        
def print_instructions():
    print("""
          \n------------------------------------------------------------------------------------
                  This program tests the gambling theory of:  
          "You can't lose, if you just double your wager after each loss"
          
          To keep it simple - we are assuming you are playing roulette - and are assuming 
          you are betting on RED every spin. Their are 18 of both colors (red + black), plus 
          (2) greens, so your odds of winning each hand are 18/38 = 47.3%.
          
          By selecting (2) at the menu - Beginner - you will be able to set (3) variables:
              1. How much your first wager is at the table
              2. The maximum you are willing to lose
              3. The maximum amount of roulette spins you'd like to play.
          
          By selecting (3) at the menu - Intermediate - you will be able to set those same (3) 
          variables, as well as three additional:
              1. If your current profits get to a certain amount (X)
              2. How much of your current profits would you like to pocket?
                    This will take it out of your pile of $$ that you are willing to gamble.
              3.  How much profit would you want to have pocketed, before you walk away 
                  from the table victorous?    
          
          
          The output to both Beginner and Intermediate will tell you:
              1. How many spins you won
              2. How many spins you lost
              3. How many spins total you played
              4. Win/Loss percentage
              5. Profits/losses at the end of the simulation
              6. How much you are walking away with (profit + initial max_bet)
              7. What the least amount that was in your pocket at any given time during 
                 the simulation
          
          By selecting (4) or (5) at the menu - you will get asked the same questions above, 
          but you will pick how many simulations you would like to run  of that scenario - 
          meaning - how many times you'd like to virtually "sit at the wheel". This will allow 
          you to see the stats on if you stuck to your strategy - how often would it be successful. 
          
          We will provide the stats on:

              1. What percentage of your simulations would you have walked away profitable.
              2. What percentage would you have at least broken even
              3. Your avg winnings when you at least broke even
              4. Your avg losses when you did not break even
              5. The avg amount of hands you played per simulation.
              6. The average amount of profit/loss - across all simulations - regardless 
                 of if you broke even or not.

          The last statistic I think is the most revealing. Because it shows you - how the house 
          always wins. Personally - I have been able to create scenarios where I have an 80prcnt chance 
          of walking away with $100, and a 20prcnt chance of losing $600. When you look at your odds 
          across all simulations though - regardless of whether or not you walk away profitable 80/100 
          simulations - I haven't yet found a recipe that results in at least an avg of "break even". 

          Logically - you can increase the percent likelihood of breaking even - by increasing your 
          risk appetite while decreasing the amount of profit required for you to walk away. 
          But - when my recipe was:
                    $10 wager
                    $100000 risk appetite
                    $50 walk away from the table
          I found that despite walking away profitable 99.6/100 simulations - the amount of money lost 
          on the .4/100 simulations that were not successful still left the house "winning" across all 
          simulations combined.

          Try and find a recipe that works - and happy gambling!\n
              """) 

def beginner_variables():
    first_wager = int(input("How much is your wager per spin?: "))
    max_bet = int(input("What is the maximum amount you are willing to lose?: "))
    max_spins = int(input("What is the maximum amount of roulette spins you want to do?: "))
    return first_wager, max_bet, max_spins

def intermediate_variables():
    bankroll_amt = 0
    pocket_amt = 0
    bankroll_amt = int(input("How much profit before you take some off the table?: $"))
    while True:
        pocket_amt = int(input("How much do you want to take off table?: $"))
        if pocket_amt > bankroll_amt:
            print("You cannot pocket more than your profits.")
        else:
            break
    walkaway = int(input("How much profit, before you walk away from the table?: $")) 
    return bankroll_amt, pocket_amt, walkaway


def simulation(first_wager, max_bet, max_spins, logs, walkaway = 0, bankroll_amt =0 ,pocket_amt = 0, level=0):
    #print("FIRST WAGER:  ", first_wager, "  MAX_BET: ", max_bet,   "MAX_SPINS: ", max_spins, "  LOGS: ", logs, "  WALKAWAY = ", walkaway, "BNKRLLAMT = ", bankroll_amt, "  PCKTAMT = ", pocket_amt, " LEVEL: ", level)
    pos_prof = False
    pocket = max_bet
    total_spins = 0
    walk = False
    off_table = 0
    spin = "orange"
    least_pocket = max_bet
    max_pocket = max_bet
    bet = first_wager
    max_wager = first_wager
    current_L_streak = 0
    max_L_streak = 0
    lose =0
    win = 0
    for i in range(max_spins):
        total_spins = i+1
        roll = rand.randrange(1,39)
        if roll > 18:
            lose = lose+1
            pocket = pocket - bet
            if current_L_streak > max_L_streak:
                max_L_streak = current_L_streak
            if pocket < least_pocket:
                least_pocket = pocket
            current_L_streak = current_L_streak+1
            if pocket < max_bet:
                bet = bet*2
            if bet > max_wager:
                max_wager = bet
        else:
            win = win+1
            if pocket < least_pocket:
                least_pocket = pocket
            pocket = pocket + bet
            if level == 2: 
                if max_pocket < pocket:
                    max_pocket = pocket
            elif level == 3:
                if pocket + off_table - max_bet == walkaway:
                    off_table = walkaway
                    pocket = max_bet
                    walk = True
                elif max_pocket < pocket + off_table:
                    max_pocket = pocket + off_table
                
            if bet > max_wager:
                max_wager = bet
            bet = first_wager
            if current_L_streak > max_L_streak:
                max_L_streak = current_L_streak
            current_L_streak = 0
            if level == 3 and walk == False:
                if pocket >= max_bet+bankroll_amt:
                    off_table = off_table + pocket_amt
                    pocket = pocket - pocket_amt
        if logs == 1:
            if roll <= 18:
                spin = 'red'
            elif roll <=36:
                spin = 'black'
            else:
                spin = 'green'
            if level==2:
                print("\nSpin Count: ", i+1, "\nSpin Result: ", spin, "\nNew amount in pocket: $", pocket, "\nNext bet: $", bet, "\nLeast Amount in Pocket thus far: $", least_pocket, "\nMost amount in pocket thus far: $", max_pocket)
            elif level==3:
                print("\nSpin Count: ", i+1, "\nSpin Result: ", spin, "\nNew amount in pocket: $", pocket, "\nNext bet: $", bet, "\nLeast Amount in Pocket thus far: $", least_pocket, "\nMost amount in pocket thus far: $", max_pocket, "\nAmount off table: $", off_table)

        if pocket < bet:
            break  
        elif walk == True:
            break   
    profit = pocket + off_table -  max_bet
    win_per = win/(win+lose)
    if profit >= 0:
        pos_prof = True
    return walk, profit, total_spins, win_per, max_wager, least_pocket, pos_prof

def experiment(first_wager, max_bet, max_spins, logs, walkaway = 0, bankroll_amt =0 ,pocket_amt = 0, level=0):
    total_runs = int(input("How many simulations would you like to run, with the variables you just selected?: "))
    walked_cnt = 0
    profit_ttl = 0
    pos_prof_ttl = 0
    total_pos_runs = 0
    total_neg_runs = 0
    neg_prof_ttl = 0
    total_spins_ttl = 0
    win_per_ttl = 0
    max_wager_ttl = 0
    least_pocket_ttl = 0
    for i in range(total_runs):
        walked, profit, total_spins, win_per, max_wager, least_pocket, pos_prof = simulation(first_wager, max_bet, max_spins, logs, walkaway, bankroll_amt, pocket_amt, level)
        if walked == True:
            walked_cnt = walked_cnt + 1
        if pos_prof == True:
            pos_prof_ttl = pos_prof_ttl + profit
            total_pos_runs = total_pos_runs + 1
        else:
            neg_prof_ttl = neg_prof_ttl + profit
            total_neg_runs = total_neg_runs + 1
        profit_ttl = profit_ttl + profit
        total_spins_ttl = total_spins_ttl + total_spins
        win_per_ttl = win_per_ttl + win_per
        max_wager_ttl = max_wager_ttl + max_wager
        least_pocket_ttl = least_pocket_ttl + least_pocket
    print("\n\n---------------------\nStatistics:\n---------------------")
    print("You hit your goal and walked from table early  %", (walked_cnt/total_runs)*100, " of the time. ")
    print("You left the table at least breaking even %", (total_pos_runs/total_runs)*100, " of the time")
    print("When you left even or positive, your average profit was: $", pos_prof_ttl/total_pos_runs)
    print("When you lost as much as you were comfortable with, your average losses were: $", neg_prof_ttl/total_neg_runs)
    print("Across all simulations - on average, your profit/loss at the end of the night was:    $", profit_ttl/total_runs)
    print("On average, you sat for ", total_spins_ttl/total_runs, " before you walked away (win or lose).")
    print("Your average win percentage across all simulations was: %", (win_per_ttl/total_runs)*100)
    print("You had to endure an average max wager of $", max_wager_ttl/total_runs, " at least once per simulation.")
    print("You on average had your pocket drop to $", least_pocket_ttl/total_runs, " at some point during the simulation.")



if __name__ == "__main__":
    user_input = 0
    print_menu = 1
    while print_menu != 6:
        if print_menu == 1:
            menu()
        user_input = selection_check()
        print_menu = selection_action(user_input)