from web3 import Web3
import time
import colorama
from colorama import Fore, Style
import shutil

# Initialize colorama for colored console output
colorama.init()

# --- SETUP ---
RPC_URL = "https://testnet-rpc.monad.xyz"
ROUTER_ADDRESS = Web3.to_checksum_address("0x00000000009726632680FB07Ddc7c4D5793BfE4F")
MON_TOKEN = Web3.to_checksum_address("0x0000000000000000000000000000000000000000")
TOKENS = {
    "WSOL": Web3.to_checksum_address("0x5387C85A4965769f6B0Df430638a1388493486F1"),
    "DAK": Web3.to_checksum_address("0x0F0BDEbF0F83cD1EE3974779Bcb7315f9808c714"),
    "ETH": Web3.to_checksum_address("0x836047a99e11F376522B447bffb6e3495Dd0637c"),
    "YAKI": Web3.to_checksum_address("0xfe140e1dCe99Be9F4F15d657CD9b7BF622270C50"),
    "CHOG": Web3.to_checksum_address("0xE0590015A873bF326bd645c3E1266d4db41C4E6B"),
    "NAP": Web3.to_checksum_address("0x93E9CaE50424C7a4E3c5eCEb7855B6dab74Bc803"),
    "WMON": Web3.to_checksum_address("0x760AfE86e5de5fa0Ee542fc7B7B713e1c5425701"),
    "USDT": Web3.to_checksum_address("0x88b8E2161DEDC77EF4ab7585569D2415a1C1055D"),
    "USDC": Web3.to_checksum_address("0xf817257fed379853cDe0fa4F97AB987181B1E5Ea"),
    "shMON": Web3.to_checksum_address("0x3a98250F98Dd388C211206983453837C8365BDc1"),
    "aprMON": Web3.to_checksum_address("0xb2f82D0f38dc453D596Ad40A37799446Cc89274A"),
    "WBTC": Web3.to_checksum_address("0xcf5a6076cfa32686c0Df13aBaDa2b40dec133F1d"),
    "Ango": Web3.to_checksum_address("0xE60c974ed6d3B19b97cA3097aD85181a814c888c"),
    "MIST": Web3.to_checksum_address("0xb38bb873cca844b20A9eE448a87Af3626a6e1EF5"),
}

# Version and Credits
VERSION = "v1.3"
CREDITS = "Created by Akbar | Powered by DZAP TESTNET"

# Utility Functions
def center_text(text):
    console_width = 80  # Default console width
    try:
        console_width = shutil.get_terminal_size().columns
    except:
        pass
    lines = text.split('\n')
    return '\n'.join(' ' * max(0, (console_width - len(line)) // 2) + line for line in lines)

def format_amount(amount, decimals=18):
    return f"{float(amount) / 10**decimals:.6f}"

# Retry Utility
def retry(fn, max_retries=3, delay_ms=5000):
    for attempt in range(1, max_retries + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == max_retries:
                raise e
            print(center_text(Fore.YELLOW + f"Retry {attempt}/{max_retries} failed: {e}. Retrying..." + Style.RESET_ALL))
            time.sleep(delay_ms / 1000)

# Display Banner
def display_banner():
    banner = f"""
{'='*50}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣿⡏⠉⠉⠉⠉⢹⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣽⣿⣯⣿⣿⣶⣴⣤⠸⣏⠁⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣾⣿⣿⢿⣿⣿⣿⣿⣯⡄⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣆⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣿⣿⣿⢿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣟⣿⣿⡷⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡟⠳⡻⢿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠐⠱⠌⠢⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⡄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⢳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠇⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠃⠉⠉⠓⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠀⠀⠀⠀⠉⠉⠛⠿⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⡀⠀⠀⠀⢀⣀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣯⣶⣢⡭⣀⣤⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡐⢛⡿⣿⡟⣋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿
⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢣⡜⣱⠯⣜⡄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡏
⡷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣊⠼⣎⡳⢎⡷⣿⢾⣼⡣⡖⠠⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢂
⡷⣹⣆⢀⢠⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠮⣬⣛⣾⡽⢯⣻⣿⣿⣾⣗⡯⣇⡯⡀⢤⡐⢪⣜⣠⡄⠀⠀⠀⠀⠀⠀⡠⣡⢃
⣟⡵⣾⢮⡾⣟⡼⡔⠀⠀⠀⠀⠀⠀⡄⣐⢖⡱⣮⠶⣕⣦⡒⣄⡄⢄⡀⢄⡴⣪⣷⣶⡻⣯⣟⣯⣿⣿⣿⣿⣿⣿⡽⣧⣝⢦⣻⡷⣳⡜⣜⡱⢂⠀⠀⠀⡴⡑⢆⢣
⣾⣹⣞⣯⢿⣿⣷⣞⡣⡄⢄⠂⡴⣰⡱⣎⣾⡿⣿⣿⣿⣷⣿⣿⣿⣶⣿⣾⣿⣷⣿⣶⣟⣷⣾⣻⣿⣿⣿⣿⣿⣿⣿⣷⣯⡟⢢⠙⣳⡽⢶⡩⣇⢮⣐⢾⡱⣙⢎⡖
⣷⢻⣼⣯⣿⣽⣿⣿⣷⣯⣯⢻⣵⣿⢻⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣧⡄⣮⣽⢳⣿⡜⣧⠛⣮⢳⡝⢺⡜
⣯⣟⣷⣻⣞⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣱⢮⣱⢻⣮⢿⣽⣛⣮⢷⣫⠷⣽
⣿⣞⣷⡿⣽⡿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢧⣇⣿⣟⡿⣾⡽⣞⣯⣟⣿⣳
⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⣿⣷⡿⣿⣽⣾⡷⣿
{'='*50}
LETS FUCK THIS TESTNET  {VERSION}
{CREDITS}
{'='*50}
"""
    print(center_text(Fore.BLUE + banner + Style.RESET_ALL))

# Display Menu
def display_menu():
    menu = f"""
{'='*50}
DZAP TESTNET X MONAD BOT - MAIN MENU
{'='*50}
Select a token to swap with MON:
{'-'*50}
"""
    for i, token in enumerate(TOKENS.keys(), 1):
        menu += f"[{i}] Swap MON <-> {token}\n"
    menu += f"""
{'-'*50}
[{len(TOKENS) + 1}] Auto All (Swaps for all tokens)
[{len(TOKENS) + 2}] Exit
{'='*50}
"""
    print(center_text(Fore.BLUE + menu + Style.RESET_ALL))

# Read Wallets
def load_wallets():
    try:
        with open("pv.txt", "r") as f:
            private_keys = [line.strip() for line in f if line.strip()]
        if not private_keys:
            print(center_text(Fore.RED + "Warning: No private keys found in kz.txt." + Style.RESET_ALL))
            exit(1)
        return private_keys
    except FileNotFoundError:
        print(center_text(Fore.RED + "Warning: kz.txt not found." + Style.RESET_ALL))
        exit(1)

# Build Transaction Data
def build_data(method_id, from_token, to_token, amount_in_wei, min_out, deadline, user_address, fee=0):
    try:
        from_token = Web3.to_checksum_address(from_token)
        to_token = Web3.to_checksum_address(to_token)
        user_address = Web3.to_checksum_address(user_address)
        return (
            method_id +
            bytes.fromhex(from_token[2:]).rjust(32, b'\x00').hex() +
            bytes.fromhex(to_token[2:]).rjust(32, b'\x00').hex() +
            int(amount_in_wei).to_bytes(32, "big").hex() +
            int(min_out).to_bytes(32, "big").hex() +
            int(deadline).to_bytes(32, "big").hex() +
            bytes.fromhex(user_address[2:]).rjust(32, b'\x00').hex() +
            int(fee).to_bytes(32, "big").hex()
        )
    except ValueError as e:
        print(center_text(Fore.RED + f"Error building data: {e}" + Style.RESET_ALL))
        raise

# Send Swap Transaction
def send_swap(w3, account, from_token, to_token, amount_in_wei, is_mon_in=False):
    sender = Web3.to_checksum_address(account.address)
    nonce = w3.eth.get_transaction_count(sender, "pending")
    deadline = int(time.time()) + 1800  # 30 minutes
    method_id = "0x2e4586c4"
    tx_value = amount_in_wei if is_mon_in else 0

    tx = {
        "from": sender,
        "to": ROUTER_ADDRESS,
        "value": tx_value,
        "gas": 500_000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce,
        "chainId": w3.eth.chain_id,
        "data": build_data(method_id, from_token, to_token, amount_in_wei, 0, deadline, sender),
    }

    signed_tx = w3.eth.account.sign_transaction(tx, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(center_text(Fore.GREEN + f"Transaction sent: https://testnet.monadexplorer.com/tx/{w3.to_hex(tx_hash)}" + Style.RESET_ALL))

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=300, poll_latency=5)
    print(center_text(Fore.GREEN + f"Confirmed in block {receipt.blockNumber}" + Style.RESET_ALL))

# Execute Swaps for a Single Token
def execute_for_token(w3, account, token_name, token_address, amount_mon, rounds):
    sender = Web3.to_checksum_address(account.address)
    print(center_text(Fore.CYAN + f"--- Processing Account: {sender} | Token: {token_name} ---" + Style.RESET_ALL))
    amount_in_wei = w3.to_wei(amount_mon, "ether")
    half_in_wei = int(amount_in_wei // 2)

    for i in range(rounds):
        print(center_text(Fore.CYAN + f"Round {i+1}/{rounds}" + Style.RESET_ALL))
        try:
            balance = w3.from_wei(w3.eth.get_balance(sender), "ether")
            if balance < amount_mon:
                print(center_text(Fore.YELLOW + f"Warning: Insufficient balance: {balance:.6f} MON < {amount_mon:.6f} MON" + Style.RESET_ALL))
                continue

            print(center_text(Fore.YELLOW + f"Swap MON -> {token_name} ({format_amount(amount_in_wei)} MON)" + Style.RESET_ALL))
            retry(lambda: send_swap(w3, account, MON_TOKEN, token_address, amount_in_wei, is_mon_in=True))
            time.sleep(2)
            
            print(center_text(Fore.YELLOW + f"Swap {token_name} -> MON (50% = {format_amount(half_in_wei)} {token_name})" + Style.RESET_ALL))
            retry(lambda: send_swap(w3, account, token_address, MON_TOKEN, half_in_wei, is_mon_in=False))
            if i < rounds - 1:
                time.sleep(2)
        except Exception as e:
            print(center_text(Fore.YELLOW + f"Warning: Skipping round {i+1} for {token_name} due to error: {e}" + Style.RESET_ALL))
            continue

# Execute All Swaps
def execute_all_swaps(w3, account, amount_mon, rounds):
    sender = Web3.to_checksum_address(account.address)
    print(center_text(Fore.CYAN + f"--- Processing All Swaps for Account: {sender} ---" + Style.RESET_ALL))
    for idx, (token_name, token_address) in enumerate(TOKENS.items(), 1):
        print(center_text(Fore.CYAN + f"[{idx}/{len(TOKENS)}] Executing swaps for {token_name}" + Style.RESET_ALL))
        try:
            execute_for_token(w3, account, token_name, token_address, amount_mon, rounds)
            time.sleep(2)
        except Exception as e:
            print(center_text(Fore.YELLOW + f"Warning: Skipping {token_name} due to error: {e}" + Style.RESET_ALL))
            continue

# Main Execution
def main():
    display_banner()
    private_keys = load_wallets()
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print(center_text(Fore.RED + "Warning: Failed to connect to RPC." + Style.RESET_ALL))
        exit(1)

    while True:
        display_menu()
        try:
            choice = input(center_text(Fore.GREEN + f"> Select an option (1-{len(TOKENS) + 2}): " + Style.RESET_ALL)).strip()
            if choice == str(len(TOKENS) + 2):
                print(center_text(Fore.GREEN + "Exiting..." + Style.RESET_ALL))
                exit(0)

            if choice == str(len(TOKENS) + 1):
                mode = "all"
                amount_mon = float(input(center_text(Fore.GREEN + "Amount of MON per token (in MON): " + Style.RESET_ALL)))
                rounds = int(input(center_text(Fore.GREEN + "Enter number of swap rounds: " + Style.RESET_ALL)))
            elif 1 <= int(choice) <= len(TOKENS):
                mode = "single"
                token_name = list(TOKENS.keys())[int(choice) - 1]
                token_address = TOKENS[token_name]
                amount_mon = float(input(center_text(Fore.GREEN + f"Amount of MON for {token_name} (in MON): " + Style.RESET_ALL)))
                rounds = int(input(center_text(Fore.GREEN + f"Enter number of swap rounds for {token_name}: " + Style.RESET_ALL)))
            else:
                print(center_text(Fore.RED + f"Invalid option. Please select 1-{len(TOKENS) + 2}." + Style.RESET_ALL))
                continue

            print(center_text(Fore.CYAN + f"Executing {'All Swaps' if mode == 'all' else f'Swaps for {token_name}'} for {len(private_keys)} account(s)..." + Style.RESET_ALL))
            for idx, pk in enumerate(private_keys, 1):
                try:
                    account = w3.eth.account.from_key(pk)
                    sender = Web3.to_checksum_address(account.address)
                    balance = w3.from_wei(w3.eth.get_balance(sender), "ether")
                    print(center_text(Fore.CYAN + f"[{idx}/{len(private_keys)}] Wallet: {sender} | Balance: {balance:.6f} MON" + Style.RESET_ALL))
                    
                    if mode == "all":
                        execute_all_swaps(w3, account, amount_mon, rounds)
                    else:
                        execute_for_token(w3, account, token_name, token_address, amount_mon, rounds)
                    
                    if idx < len(private_keys):
                        time.sleep(2)
                except Exception as e:
                    print(center_text(Fore.RED + f"Error processing wallet {sender}: {e}" + Style.RESET_ALL))
                    continue

            print(center_text(Fore.GREEN + "Completed processing for all accounts." + Style.RESET_ALL))
            input(center_text(Fore.GREEN + "Press Enter to return to menu, or Ctrl+C to exit..." + Style.RESET_ALL))
        except ValueError:
            print(center_text(Fore.RED + "Warning: Invalid input. Please enter valid numbers." + Style.RESET_ALL))
        except KeyboardInterrupt:
            print(center_text(Fore.GREEN + "Stopped by user." + Style.RESET_ALL))
            exit(0)
        except Exception as e:
            print(center_text(Fore.RED + f"Error: {e}" + Style.RESET_ALL))
            time.sleep(10)

if __name__ == "__main__":
    main()
