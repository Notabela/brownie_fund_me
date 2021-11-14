from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVS = {"mainnet-fork", "mainnet-fork-dev"}
LOCAL_BLOCKCHAIN_ENVS = {"development", "ganache-local"}


def get_accounts():
    if network.show_active() in (LOCAL_BLOCKCHAIN_ENVS | FORKED_LOCAL_ENVS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, Web3.toWei(2000, "ether"), {"from": get_accounts()})

    print("Mocks Deployed")

    return MockV3Aggregator[-1].address
