"""
================================================================================
Proxy List Generator
================================================================================
Author      : Breno Farias da Silva
Created     : 2026-02-05
Description :
    This script generates a list of proxies by scraping from various online sources.
    It collects proxy IP addresses and ports from spys.me and free-proxy-list.net,
    and saves them to a text file for use in proxy-related applications.

    Key features include:
        - Scraping proxies from spys.me using regex pattern matching
        - Scraping proxies from free-proxy-list.net using HTML parsing
        - Saving all collected proxies to a single output file
        - Logging output to both terminal and file
        - Execution time calculation and reporting
        - Optional sound notification upon completion

Usage:
    1. Ensure all dependencies are installed (see Dependencies section).
    2. Run the script via Python:
            $ python main.py
    3. The script will scrape proxies and save them to separate files in the Proxies_List directory.

Outputs:
    - Proxies_List/spys_me_proxies.txt: Proxies from spys.me
    - Proxies_List/free_proxy_list_proxies.txt: Proxies from free-proxy-list.net

TODOs:
    - Add support for additional proxy sources
    - Implement proxy validation and filtering
    - Add command-line arguments for customization
    - Improve error handling for network requests

Dependencies:
    - Python >= 3.6
    - beautifulsoup4
    - colorama
    - Logger (custom module)
    - requests

Assumptions & Notes:
    - Internet connection is required for scraping
    - The script assumes the target websites maintain their current structure
    - Proxies are saved in IP:PORT format, one per line, in separate files per source
    - Sound notification is disabled on Windows
"""

import atexit  # For playing a sound when the program finishes
import datetime  # For getting the current date and time
import os  # For running a command in the terminal
import platform  # For getting the operating system name
import re  # For regular expressions
import requests  # For making HTTP requests
import sys  # For system-specific parameters and functions
from bs4 import BeautifulSoup  # For HTML parsing
from colorama import Style  # For coloring the terminal
from Logger import Logger  # For logging output to both terminal and file
from pathlib import Path  # For handling file paths


# Macros:
class BackgroundColors:  # Colors for the terminal
    CYAN = "\033[96m"  # Cyan
    GREEN = "\033[92m"  # Green
    YELLOW = "\033[93m"  # Yellow
    RED = "\033[91m"  # Red
    BOLD = "\033[1m"  # Bold
    UNDERLINE = "\033[4m"  # Underline
    CLEAR_TERMINAL = "\033[H\033[J"  # Clear the terminal


# Execution Constants:
VERBOSE = False  # Set to True to output verbose messages

# Proxy Constants:
PROXY_SOURCES = {
    "spys_me": "https://spys.me/proxy.txt",
    "free_proxy_list": "https://free-proxy-list.net/",
}
PROXY_REGEX = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"  # Regex pattern to match IP:PORT format
OUTPUT_DIR = "Proxies_List"  # Output directory for proxy files
OUTPUT_FILE_SUFFIX = "proxies.txt"  # Suffix for proxy output files

# Logger Setup:
logger = Logger(f"./Logs/{Path(__file__).stem}.log", clean=True)  # Create a Logger instance
sys.stdout = logger  # Redirect stdout to the logger
sys.stderr = logger  # Redirect stderr to the logger

# Sound Constants:
SOUND_COMMANDS = {
    "Darwin": "afplay",
    "Linux": "aplay",
    "Windows": "start",
}  # The commands to play a sound for each operating system
SOUND_FILE = "./.assets/Sounds/NotificationSound.wav"  # The path to the sound file

# RUN_FUNCTIONS:
RUN_FUNCTIONS = {
    "Play Sound": True,  # Set to True to play a sound when the program finishes
}

# Functions Definitions:


def verbose_output(true_string="", false_string=""):
    """
    Outputs a message if the VERBOSE constant is set to True.

    :param true_string: The string to be outputted if the VERBOSE constant is set to True.
    :param false_string: The string to be outputted if the VERBOSE constant is set to False.
    :return: None
    """

    if VERBOSE and true_string != "":  # If VERBOSE is True and a true_string was provided
        print(true_string)  # Output the true statement string
    elif false_string != "":  # If a false_string was provided
        print(false_string)  # Output the false statement string


def verify_filepath_exists(filepath):
    """
    Verify if a file or folder exists at the specified path.

    :param filepath: Path to the file or folder
    :return: True if the file or folder exists, False otherwise
    """

    verbose_output(
        f"{BackgroundColors.GREEN}Verifying if the file or folder exists at the path: {BackgroundColors.CYAN}{filepath}{Style.RESET_ALL}"
    )  # Output the verbose message

    return os.path.exists(filepath)  # Return True if the file or folder exists, False otherwise


def scrape_proxies_from_spys_me():
    """
    Scrapes proxy IP addresses and ports from spys.me using regex pattern matching
    and returns a list of proxy strings.

    :return: List of proxy strings in IP:PORT format
    """

    verbose_output(
        f"{BackgroundColors.GREEN}Scraping proxies from spys.me...{Style.RESET_ALL}"
    )  # Output the scraping message
    
    c = requests.get(PROXY_SOURCES["spys_me"])  # Make HTTP request to spys.me
    
    test_str = c.text  # Get the response text
    
    a = re.finditer(PROXY_REGEX, test_str, re.MULTILINE)  # Find all matches of IP:PORT pattern
    
    proxies = [i.group() for i in a]  # Collect all proxy strings
    
    verbose_output(
        f"{BackgroundColors.GREEN}Scraped {len(proxies)} proxies from spys.me{Style.RESET_ALL}"
    )  # Output the scraping result
    
    return proxies  # Return the list of proxies


def scrape_proxies_from_free_proxy_list():
    """
    Scrapes proxy IP addresses and ports from free-proxy-list.net using HTML parsing
    and returns a list of proxy strings.

    :return: List of proxy strings in IP:PORT format
    """

    verbose_output(
        f"{BackgroundColors.GREEN}Scraping proxies from free-proxy-list.net...{Style.RESET_ALL}"
    )  # Output the scraping message
    
    d = requests.get(PROXY_SOURCES["free_proxy_list"])  # Make HTTP request to free-proxy-list.net
    
    soup = BeautifulSoup(d.content, "html.parser")  # Parse the HTML content
    
    td_elements = soup.select(".fpl-list .table tbody tr td")  # Select table data elements
    
    ips = []  # List to store IP addresses
    ports = []  # List to store ports
    
    for j in range(0, len(td_elements), 8):  # Iterate over elements in steps of 8
        ips.append(td_elements[j].text.strip())  # Extract and store IP
        ports.append(td_elements[j + 1].text.strip())  # Extract and store port
    
    proxies = [f"{ip}:{port}" for ip, port in zip(ips, ports)]  # Format proxy strings
    
    verbose_output(
        f"{BackgroundColors.GREEN}Scraped {len(proxies)} proxies from free-proxy-list.net{Style.RESET_ALL}"
    )  # Output the scraping result
    
    return proxies  # Return the list of proxies


def to_seconds(obj):
    """
    Converts various time-like objects to seconds.
    
    :param obj: The object to convert (can be int, float, timedelta, datetime, etc.)
    :return: The equivalent time in seconds as a float, or None if conversion fails
    """
    
    if obj is None:  # None can't be converted
        return None  # Signal failure to convert
    if isinstance(obj, (int, float)):  # Already numeric (seconds or timestamp)
        return float(obj)  # Return as float seconds
    if hasattr(obj, "total_seconds"):  # Timedelta-like objects
        try:  # Attempt to call total_seconds()
            return float(obj.total_seconds())  # Use the total_seconds() method
        except Exception:
            pass  # Fallthrough on error
    if hasattr(obj, "timestamp"):  # Datetime-like objects
        try:  # Attempt to call timestamp()
            return float(obj.timestamp())  # Use timestamp() to get seconds since epoch
        except Exception:
            pass  # Fallthrough on error
    return None  # Couldn't convert


def calculate_execution_time(start_time, finish_time=None):
    """
    Calculates the execution time and returns a human-readable string.

    Accepts either:
    - Two datetimes/timedeltas: `calculate_execution_time(start, finish)`
    - A single timedelta or numeric seconds: `calculate_execution_time(delta)`
    - Two numeric timestamps (seconds): `calculate_execution_time(start_s, finish_s)`

    Returns a string like "1h 2m 3s".
    """

    if finish_time is None:  # Single-argument mode: start_time already represents duration or seconds
        total_seconds = to_seconds(start_time)  # Try to convert provided value to seconds
        if total_seconds is None:  # Conversion failed
            try:  # Attempt numeric coercion
                total_seconds = float(start_time)  # Attempt numeric coercion
            except Exception:
                total_seconds = 0.0  # Fallback to zero
    else:  # Two-argument mode: Compute difference finish_time - start_time
        st = to_seconds(start_time)  # Convert start to seconds if possible
        ft = to_seconds(finish_time)  # Convert finish to seconds if possible
        if st is not None and ft is not None:  # Both converted successfully
            total_seconds = ft - st  # Direct numeric subtraction
        else:  # Fallback to other methods
            try:  # Attempt to subtract (works for datetimes/timedeltas)
                delta = finish_time - start_time  # Try subtracting (works for datetimes/timedeltas)
                total_seconds = float(delta.total_seconds())  # Get seconds from the resulting timedelta
            except Exception:  # Subtraction failed
                try:  # Final attempt: Numeric coercion
                    total_seconds = float(finish_time) - float(start_time)  # Final numeric coercion attempt
                except Exception:  # Numeric coercion failed
                    total_seconds = 0.0  # Fallback to zero on failure

    if total_seconds is None:  # Ensure a numeric value
        total_seconds = 0.0  # Default to zero
    if total_seconds < 0:  # Normalize negative durations
        total_seconds = abs(total_seconds)  # Use absolute value

    days = int(total_seconds // 86400)  # Compute full days
    hours = int((total_seconds % 86400) // 3600)  # Compute remaining hours
    minutes = int((total_seconds % 3600) // 60)  # Compute remaining minutes
    seconds = int(total_seconds % 60)  # Compute remaining seconds

    if days > 0:  # Include days when present
        return f"{days}d {hours}h {minutes}m {seconds}s"  # Return formatted days+hours+minutes+seconds
    if hours > 0:  # Include hours when present
        return f"{hours}h {minutes}m {seconds}s"  # Return formatted hours+minutes+seconds
    if minutes > 0:  # Include minutes when present
        return f"{minutes}m {seconds}s"  # Return formatted minutes+seconds
    return f"{seconds}s"  # Fallback: only seconds


def play_sound():
    """
    Plays a sound when the program finishes and skips if the operating system is Windows.

    :param: None
    :return: None
    """

    current_os = platform.system()  # Get the current operating system
    if current_os == "Windows":  # If the current operating system is Windows
        return  # Do nothing

    if verify_filepath_exists(SOUND_FILE):  # If the sound file exists
        if current_os in SOUND_COMMANDS:  # If the platform.system() is in the SOUND_COMMANDS dictionary
            os.system(f"{SOUND_COMMANDS[current_os]} {SOUND_FILE}")  # Play the sound
        else:  # If the platform.system() is not in the SOUND_COMMANDS dictionary
            print(
                f"{BackgroundColors.RED}The {BackgroundColors.CYAN}{current_os}{BackgroundColors.RED} is not in the {BackgroundColors.CYAN}SOUND_COMMANDS dictionary{BackgroundColors.RED}. Please add it!{Style.RESET_ALL}"
            )
    else:  # If the sound file does not exist
        print(
            f"{BackgroundColors.RED}Sound file {BackgroundColors.CYAN}{SOUND_FILE}{BackgroundColors.RED} not found. Make sure the file exists.{Style.RESET_ALL}"
        )


def main():
    """
    Main function.

    :param: None
    :return: None
    """

    print(
        f"{BackgroundColors.CLEAR_TERMINAL}{BackgroundColors.BOLD}{BackgroundColors.GREEN}Welcome to the {BackgroundColors.CYAN}Proxy List Generator{BackgroundColors.GREEN} program!{Style.RESET_ALL}",
        end="\n\n",
    )  # Output the welcome message
    start_time = datetime.datetime.now()  # Get the start time of the program
    
    # Implement logic here

    finish_time = datetime.datetime.now()  # Get the finish time of the program
    print(
        f"{BackgroundColors.GREEN}Start time: {BackgroundColors.CYAN}{start_time.strftime('%d/%m/%Y - %H:%M:%S')}\n{BackgroundColors.GREEN}Finish time: {BackgroundColors.CYAN}{finish_time.strftime('%d/%m/%Y - %H:%M:%S')}\n{BackgroundColors.GREEN}Execution time: {BackgroundColors.CYAN}{calculate_execution_time(start_time, finish_time)}{Style.RESET_ALL}"
    )  # Output the start and finish times
    print(
        f"\n{BackgroundColors.BOLD}{BackgroundColors.GREEN}Program finished.{Style.RESET_ALL}"
    )  # Output the end of the program message
    (
        atexit.register(play_sound) if RUN_FUNCTIONS["Play Sound"] else None
    )  # Register the play_sound function to be called when the program finishes


if __name__ == "__main__":
    """
    This is the standard boilerplate that calls the main() function.

    :return: None
    """

    main()  # Call the main function
