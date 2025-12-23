# Roulette
                  This program tests the gambling theory of:  
          "You can't lose, if you just double your wager after each loss"
          
### To keep it simple -  
          We are assuming you are playing roulette - and are assuming 
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
