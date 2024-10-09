"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

def main():
    while True:
        try:
            p = float((input("Gimme principal $: ")))
            r = float((input("Gimme interest rate %: ")))
            time_unit = input("Gimme whether time is in years, months or days (y/m/d): ")
            t = float((input("Enter length of time: ")))

            #dictionary mapping cuz fancy and no if-else-if-else-if-else 🤓
            i = p * r/100 * (t / {'y': 1, 'm': 12, 'd': 365}[time_unit])

            print(f"\n\n💹💲🤑💸🤑💲🤓\nWith your invesment of ${p:.2f} with a {r}% rate for {t}{time_unit} — you'll make:\n${i:.2f}\n💹💲🤑💸🤑💲🤓")
            break
        
        except Exception as e:
            print("Bad input 🙄 duh", e)
    

if __name__ == '__main__':
    main()