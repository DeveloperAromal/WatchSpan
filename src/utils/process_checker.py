from colorama import Fore
from src.utils.log import log
import requests
import os

def check_info():
    try:
        ip_info = requests.get("https://api.ipify.org?format=json").json()
        log(f"Initialized new machine in {ip_info.get('ip')}", Fore.CYAN)
    except Exception as e:
        log(f"Failed to fetch IP: {e}", Fore.RED, "[!]")

    log("Checking Training dataset...", Fore.YELLOW)
    if os.path.isfile("src/data/retail_store_inventory_train.csv"):
        log("Training dataset exists", Fore.GREEN, "[*]")
    else:
        log("Training dataset does NOT exist", Fore.RED, "[!]")

    log("Checking Testing dataset...", Fore.YELLOW)
    if os.path.isfile("src/data/retail_store_inventory_test.csv"):
        log("Testing dataset exists", Fore.GREEN, "[*]")
    else:
        log("Testing dataset does NOT exist", Fore.RED, "[!]")

    print("-" * 74 + "\n")
