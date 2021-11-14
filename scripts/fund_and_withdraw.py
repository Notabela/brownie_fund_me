from brownie import FundMe
from scripts.helpers import get_accounts


def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    entrance_fee = fund_me.getEntranceFee()
    print(f"the current entrance fee is {entrance_fee}")

    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
