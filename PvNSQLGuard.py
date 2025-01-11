import time
import pyfiglet
import requests
from urllib.parse import urlparse, parse_qs
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Function to display the splash screen
def display_splash_screen():
    ascii_art = pyfiglet.figlet_format("PvNSQLGuard", font="slant")
    print(Fore.CYAN + ascii_art)
    print(Fore.YELLOW + "Developer: Pavan Kamthane")
    print(Fore.GREEN + "LinkedIn: https://www.linkedin.com/in/pavankamthane/")
    print(Fore.GREEN + "GitHub: https://github.com/PavanBoss")
    print(Fore.GREEN + "\nInitializing SQL Injection scanner...\n")
    
    # Basic definition of PvNSQLGuard
    print(Fore.WHITE + "\nPvNSQLGuard is a tool designed to detect SQL injection vulnerabilities in web applications.")
    print(Fore.WHITE + "It scans a given URL for query parameters and tests them with common SQL injection payloads.")
    print(Fore.WHITE + "The tool provides quick feedback on whether the URL is vulnerable to SQL injection.")
    
    time.sleep(3)

# Function to read payloads from a file
def load_payloads(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file.readlines()]
    return payloads

# Function to test SQL injection vulnerability on all parameters
def test_sql_injection(url, payloads):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # If there are no query parameters, exit
    if not query_params:
        print(Fore.YELLOW + "No query parameters found in the URL.")
        return
    
    # Test each parameter
    for param in query_params:
        for payload in payloads:
            test_url = f"{url}&{param}={payload}"
            response = requests.get(test_url)

            # Check for common error responses (you can extend this based on your testing)
            if "error" in response.text or "syntax" in response.text:
                print(Fore.RED + f"[Vulnerable] SQL Injection detected on {url} with parameter: {param}")
                return
    print(Fore.GREEN + f"[Safe] No SQL injection detected on {url}.")

# Main function
def main():
    display_splash_screen()

    # Path to the payloads file
    payloads_file = "payloads.txt"

    # Load payloads from the file
    payloads = load_payloads(payloads_file)

    # Display example URL
    print(Fore.YELLOW + "\nExample URL to test (with query parameters):")
    print(Fore.CYAN + "http://testphp.vulnweb.com/search.php?test=query\n")

    # Colorized input prompt
    url = input(Fore.YELLOW + "Enter target URL: ")

    # Colorized input for query parameters check
    has_params = input(Fore.YELLOW + "Does this URL have query parameters? (yes/no) or 'IDK': ").strip().lower()

    if has_params in ["yes", "y"]:  # If the user knows the URL has parameters
        # Test for SQL injection on all parameters
        test_sql_injection(url, payloads)
    elif has_params in ["no", "n", "idk"]:  # If the user is unsure or says no
        # Automatically detect query parameters
        print(Fore.YELLOW + "Scanning URL for query parameters...")

        # Detect query parameters
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        if not query_params:
            print(Fore.YELLOW + "No query parameters found in the URL.")
        else:
            print(Fore.GREEN + "Detected query parameters. Starting SQL injection test...")
            # Test for SQL injection on all detected parameters
            test_sql_injection(url, payloads)
    else:
        print(Fore.RED + "Invalid input. Please enter 'yes', 'no', or 'IDK'.")

if __name__ == "__main__":
    main()
