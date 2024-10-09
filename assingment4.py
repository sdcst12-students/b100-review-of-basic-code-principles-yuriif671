"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

def main():
    while True:
        try:
            a = float((input("How much money you owe? $: ")))
            r = float((input("Gimme interest rate %: ")))
            m = float((input("How much you can pay per month $: ")))

            months = 0
            remaining_balance = a
            total_paid = 0

            while remaining_balance > 0:
                interest = remaining_balance * (r / 100)

                total_paid += interest

                remaining_balance += interest - m   

                months += 1

            print(f"It'll take you {months} months or {round(months / 12, 2)} years to repay the debt 🗿\nAnd you've paid this much interest: ${round(total_paid, 2)}\n😓😓😓")
            break
        
        except Exception as e:
            print("Bad input 🙄 duh", e)
    

if __name__ == '__main__':
    main()