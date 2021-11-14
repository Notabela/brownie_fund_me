from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpers import (
    get_accounts,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVS,
    FORKED_LOCAL_ENVS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_accounts()

    if network.show_active() not in (LOCAL_BLOCKCHAIN_ENVS | FORKED_LOCAL_ENVS):
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        price_feed_address = deploy_mocks()

    should_publish = config["networks"][network.show_active()].get("verify")
    fund_me = FundMe.deploy(
        price_feed_address, {"from": account}, publish_source=should_publish
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
