"""
This module defines a function to create a Certificate of Deposit (CD) account,
calculate interest earned, and update the account balance.

Functions:
    create_cd_account(balance, interest_rate, months):
        Creates a CD account instance with the given initial balance and interest rate.
        Calculates the interest earned over the specified number of months and updates
        the account balance accordingly.

        Args:
            balance (float): The initial CD account balance.
            interest_rate (float): The annual percentage rate (APR) interest rate for the CD account.
            months (int): The length of time in months for the CD.

        Returns:
            - float: The updated CD account balance after adding the interest earned.
            - float: The interest earned over the specified period.
"""
"""Import the Account class from the Account.py file."""
import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    CDAccount = Account.Account(balance, interest_rate)

    # Calculate interest earned
    Interest_Earned = balance * (interest_rate/100 * months / 12)

    # Update the CD account balance by adding the interest earned
    Account_Balance = balance + Interest_Earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    CDAccount.set_balance = Account_Balance

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    CDAccount.set_interest = Interest_Earned

    # Return the updated balance and interest earned.
    return  Account_Balance, Interest_Earned
