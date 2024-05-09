import time


def calcBalances(age, retirementAge, initial401kBalance, employerContribution,
                 salary, individualContribution, rothBalance, rothReturn,
                 rothContributions, brokerageBalance, brokerageReturn, brokerageContributions):
    """Calculation logic for future account balance. Takes inputs as parameters for calculation."""

    # Brokerage logic
    futureBrokerageBalance = brokerageBalance
    curAge = age
    while curAge < retirementAge:
        futureBrokerageBalance *= (1 + brokerageReturn / 100) 
        futureBrokerageBalance += brokerageContributions
        curAge += 1

    # Roth logic
    futureRothBalance = rothBalance
    curAge = age
    while curAge < retirementAge:
        futureRothBalance *= (1 + rothReturn / 100) 
        futureRothBalance += rothContributions
        curAge += 1

    # 401k logic
    future401kBalance = initial401kBalance
    curAge = age
    while curAge < retirementAge:
        future401kBalance += ((1 + individualContribution / 100) * salary) + ((1 + employerContribution / 100) * salary)
        curAge += 1

    totalAccounts = future401kBalance + futureBrokerageBalance + futureRothBalance

    print("\n  You have entered all necessary information! ")
    print("\n  Calculating future account balances... ")
    print("\n\n")
    time.sleep(3)

    print("\n  Here are you projected balances at retirement age: ")
    print("\n\n")
    print(f"   401(k) Balance: ${future401kBalance:,.2f}")
    print(f"   Roth IRA Balance: ${futureRothBalance:,.2f}")
    print(f"   Brokerage Account Balance: ${futureBrokerageBalance:,.2f}")
    print(f"   In total you will have: ${totalAccounts:,.2f} when you retire.")  
    print("\n\n")

    return

# Input validation functions:


def validateAge(current_age, retirement_age):
    """Validates that retirement age is greater than current age."""
    return retirement_age >= current_age


def validateRoth(rothContribution):
    """Validates that Roth IRA contribution input by the user is less than the federal limit."""
    return rothContribution <= 7000


def validate401k(salary, contributionPercentage):
    """Validates that 401k contribution input by the user is a portion of their salary that amounts
     to less than the federal limit."""
    return (contributionPercentage / 100) * salary <= 23000


def main():
    print("\nWelcome to the Retirement Planner\n")

    header = '''
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$┌────────────────────────────────────────────────────────────────────────┐$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│ /$$$$$$                                           /$$     /$$          │$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│|_  $$_/                                          | $$    | $$          │$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│  | $$   /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$$ /$$$$$$  | $$ /$$   /$$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│  | $$  | $$__  $$|  $$  /$$//$$__  $$ /$$_____/|_  $$_/  | $$| $$  | $$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│  | $$  | $$  \ $$ \  $$/$$/| $$$$$$$$|  $$$$$$   | $$    | $$| $$  | $$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│  | $$  | $$  | $$  \  $$$/ | $$_____/ \____  $$  | $$ /$$| $$| $$  | $$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│ /$$$$$$| $$  | $$   \  $/  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$|  $$$$$$$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│|______/|__/  |__/    \_/    \_______/|_______/    \___/  |__/ \____  $$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│                                                               /$$  | $$│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│                                                              |  $$$$$$/│$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$│                                                               \______/ │$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$└────────────────────────────────────────────────────────────────────────┘$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    '''
 
    print(header)
    print("                                            Welcome to the Investly Investment Calculator!")
    print("                 Check out our options below to try the Investment Calculator! You can enter '1' to start the Investment Calculator, ")
    print("                 which will calculate and display what your Roth IRA, 401k and Brokerage accounts will be worth when you retire. ")
    print("                 Need more information about the Investly Calculator or account types? Enter '2' to go to the FAQ page. When prompted, you ")
    print("                 can stop this application by entering '3'. Happy investing! ")
    print("\n\n")
    time.sleep(4)

    while True:
        print("      Please choose an option below to continue:")
        print("\n\n")
        print("      1. Use the Investment Calculator")
        print("      2. Learn more about these account types!")
        print("      3. Quit")
        print("\n\n")

        choice = input("      Choose an option: ")
        print("\n\n")

        if choice == "1":
            print("   When prompted, please enter the appropriate information. If any of the prompts do not apply to your current financial situation,")
            print("   please enter '0'. We will never sell your information. Our calculator keeps your information secure and private!")
            print("\n\n")
            time.sleep(2)

            invalid = "   Invalid entry. Try again."
            prompts = [("   Enter you current age. This must be an integer value: "), ("   Enter you projected retirement age. This must be an integer value: "), ("   Enter your current 401(k) balance. This must be a numerical value: $"),
                       ("   Enter your employer's contribution percentage to your 401(k). This must be a numerical value. Do not include the '%' sign: "), ("   Please enter your current salary. This must be a numerical value: $"), 
                       ("   Please enter your individual contribution percentage to your 401(k). This must be a numerical value. Do not include the '%' sign: "), ("   Please enter your current Roth IRA balance. This must be a numerical value: $ "),
                       ("   Please enter your projected Roth IRA rate of return. This must be a numerical value. Do not include the '%' sign:: "), ("   Please enter your yearly contribution to your Roth IRA. This must be a numerical value: $ "),
                       ("   Please enter current brokerage account balance. This must be a numerical value: $ "), ("   Please enter your projected Brokerage account rate of return. This must be a numerical value. Do not include the '%' sign:: "),
                       ("   Please enter your yearly contribution to your Brokerage account. This must be a numerical value: $ ")]

            categories = [None] * 12

            i = 0
            while i < 12 and type(categories[i]) != float:

                categories[i] = (input(prompts[i]))

                if i == 1:
                    try:
                        curAge = float(categories[0])
                        retirementAge = float(categories[i])
                        if not validateAge(curAge, retirementAge):
                            print("   Retirement age must be greater than or equal to the current age.")
                            continue
                    except ValueError:
                        print("   Invalid input")
                        continue

                if i == 8:
                    try:
                        rothContribution = float(categories[i])
                        if not validateRoth(rothContribution):
                            print("   As per the 2024 federal limit: Roth IRA yearly contribution cannot exceed $7,000.")
                            continue
                    except ValueError:
                        print("   Invalid input.")
                        continue

                if i == 5:
                    try:
                        salary = float(categories[4])
                        individualContribution = float(categories[i])
                        if not validate401k(salary, individualContribution):
                            print("   As per the 2024 federal limit: Individual 401(k) contribution cannot exceed $23,000.")
                            continue 
                    except ValueError:
                        print("   Invalid input")
                        continue

                try:
                    categories[i] = float(categories[i])
                    i += 1
                except ValueError:
                    print(invalid)

            calcBalances(
                categories[0], categories[1], categories[2], categories[3],
                categories[4], categories[5], categories[6], categories[7],
                categories[8], categories[9], categories[10], categories[11])

        elif choice == "2":
            about()
            time.sleep(10)
        elif choice == "3":
            print("Thank you for using Investly. We hope to see you soon!")
            print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

            return
        else:
            print("You entered an invalid option. Please enter 1, 2, or 3.")


def about():
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Welcome to the FAQ! $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    print("\n What is Investly?\n")
    print("\n Investly is a compound interest calculator that takes your current and projected account details for 401ks, Roth IRAs, and brokerage acounts.\n")
    print("\n Investly then calculates your future projected account balances at your projected retirement age so that you can visualize your financial health.\n")
    print("\n --------------------------------------------------------------------------------------------------------------------\n")
    time.sleep(1)
    print("\n What is a 401k?\n")
    print("\n A 401k is a tax advantage account that reduces your taxable income as contributions are taken out of your paycheck pre-tax.\n")
    print("\n The 2024 federal limit for 401k contributions is $23,000. You can withdraw TAX FREE from this account at age 59.5! \n")
    print("\n --------------------------------------------------------------------------------------------------------------------\n")
    time.sleep(1)
    print("\n What is a Roth IRA? \n")
    print("\n A Roth IRA is another tax advantage account, but it doesn't reduce your taxable income. As of 2024 the federal limit is $7,000 a year. \n")
    print("\n There is no tax deduction for contributions to a Roth IRA, but contributions and earnings can be withdrawn tax free in retirement. \n")
    print("\n Any contribution made can be taken out at any time without penalty. \n")
    print("\n --------------------------------------------------------------------------------------------------------------------\n")
    time.sleep(1)
    print("\n What is a Brokerage account?.\n")
    print("\n This is an investment account that allows you to buy and sell stocks, mutual funds, ETFs, cryptocurrency, and other securities!\n")
    print("\n Unfortunately, these accounts are not tax advantage, so you will be subject to capital gains tax based on your tax bracket.\n")
    print("\n This account can still be very powerful with the advantage of compound interest! \n")
    print("\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")


if __name__ == "__main__":
    main()
