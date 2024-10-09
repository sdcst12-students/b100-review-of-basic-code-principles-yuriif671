"""
### Assignment 3
#### Calculation of an investment with a recurring depositS
This will be the same as assignment 2 except you must use a while loop to iterate through your years.
The simple interest formula only works if the principal or initial investment is not touched.  If an amount is added to the principal every year, then the interest must be calculated and added along with the future deposit to determine the starting balance at the beginning of the next year.

For example, suppose you invest $100 every year, and earn 5% interest per year.
At the start of the first year, you will have your $100 that you invested.  At the start of the second year, you will have the initial $100, $5 interest as well as an additional $100 that is invested in the second year, for a total of $205 dollars.  Write a program that uses a while loop to determine the amount of money in an account after a certain number of years.

Criteria:
Your program should ask the user for
* the annual investment
* the annual interest rate (as a percentage)
* the number of years
* calculate the amount of money at the end of each year until the specified number of years has been reached.
* appropriate formatting and variable names will be important
* use a *while* loop to iterate through the years.

Sample data
annual investment: 100
rate: 5%
10 years
final balance: 1320.68
"""

def main():
    while True:
        try:
            a = float((input("Gimme annual investment $: ")))
            r = float((input("Gimme interest rate %: ")))
            t = int((input("Enter how many years: ")))

            #dictionary mapping cuz fancy and no if-else-if-else-if-else 🤓
            money = 0

            while t != 0:
                money += a
                i = money * (r / 100)
                money += i

                print(f"Year {t}: Balance = ${money:.2f} 💵🤑")
                t-= 1
            
            print(f"\n\n💹💲🤑💸🤑💲🤓\nAfter {t} years with a {r}%, you get:\n${money:.2f}\n💹💲🤑💸🤑💲🤓")
            break
        
        except Exception as e:
            print("Bad input 🙄 duh", e)
    

if __name__ == '__main__':
    main()