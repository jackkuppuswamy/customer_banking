"""
This script allows users to calculate and display interest earned on both savings and CD accounts.

Functions:
    main():
        Prompts the user to enter balances, interest rates, and months for both a savings account
        and a CD (Certificate of Deposit) account. It then calls the respective functions
        (`create_savings_account` and `create_cd_account`) to calculate interest earned and
        update account balances. Finally, it prints out the interest earned and updated balances
        for both accounts.
"""
# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    try:
        savings_balance = float(input("Enter the savings account balance: "))        
    except ValueError:
        print("Please enter a valid account balance.")
        return
    
    try:
        savings_interest = float(input("Enter the savings account interest rate: "))        
    except ValueError:
        print("Please enter a valid interest rate.")
        return
    
    try:
        savings_maturity = int(input("Enter the number of months: "))
    except ValueError:
        print("Please enter a valid number of months.")
        return

    # Call the create_savings_account function and pass the variables from the user.
    savings_account = create_savings_account(savings_balance, savings_interest, savings_maturity)
    updated_savings_balance, interest_earned = savings_account #, savings_account.get_interest()

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The interest earned on the savings account is: ${interest_earned:,.2f}")
    print(f"The updated savings account balance with interest earned for {savings_maturity} months is: ${updated_savings_balance:,.2f}")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    try:
        cd_balance= float(input("Enter the CD account balance: "))
    except ValueError:
        print("Please enter a valid account balance.")
        return
    
    try:
        cd_interest = float(input("Enter the CD account interest rate: "))
    except ValueError:
        print("Please enter a valid interest rate.")
        return

    try:
        cd_maturity = int(input("Enter the number of months: "))
    except ValueError:
        print("Please enter a valid number of months.")
        return

    # Call the create_cd_account function and pass the variables from the user.
    cd_account = create_cd_account(cd_balance, cd_interest, cd_maturity)
    updated_cd_balance, interest_earned = cd_account

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The interest earned on the CD account is: ${interest_earned:,.2f}")
    print(f"The updated CD account balance with interest earned for {cd_maturity} months is: ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
