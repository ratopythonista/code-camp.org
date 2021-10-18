from scripts.helpful_script import get_account, get_contract
from brownie import Lottery


def deploy_lottery():
    account = get_account(id="ratopythonista")
    lottery = Lottery.deploy(get_contract())


def main():
    deploy_lottery()
