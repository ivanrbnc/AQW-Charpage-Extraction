import requests
import re

def get_character_id(character_name):
    """
    Fetch the character ID (ccid) by character name.
    Params:
        character_name (str): The name of the character (spaces allowed).
    Returns:
        int: Character ID (ccid) if found, None if not.
    """

    # Format the character name for the URL
    formatted_name = character_name.replace(" ", "+")
    site = 'https://account.aq.com'
    ccid_url = f"{site}/CharPage?id={formatted_name}"
    
    # Fetch the page source
    response = requests.get(ccid_url)
    
    if response.status_code != 200:
        print("Failed to fetch character page.")
        return None
    
    # Extract the ccid using regex
    match = re.search(r"var ccid = (\d+);", response.text)
    
    if match:
        ccid = int(match.group(1))
        print(f"Character ID (ccid) for '{character_name}': {ccid}")
        return ccid
    else:
        print(f"Character ID not found for '{character_name}'.")
        return None