import requests
import urllib.parse

def generate_url(str_name):
    """Generates a URL from the item name by replacing special characters."""
    encoded_name = urllib.parse.quote(str_name.replace("'", "-").replace(" ", "-").replace(":", "-").replace(";", "-"))
    return f'http://aqwwiki.wikidot.com/{encoded_name}'

def get_inventory(ccid, categories=None):
    """
    Fetches inventory items for a character and categorizes them.
    Params:
        ccid (int): Character ID
        categories (list): Optional list of categories to filter items by (case-insensitive)
    """
    site = 'https://account.aq.com'
    inventory_url = f"{site}/CharPage/Inventory?ccid={ccid}"
    
    inventory_response = requests.get(inventory_url)
    inventory_data = inventory_response.json()

    itypes = ["Class", "Armor", "Helm", "Cape", "Sword", "Axe", "Gauntlet", "Dagger", "HandGun", "Rifle", "Gun", "Whip", "Bow",
              "Mace", "Polearm", "Staff", "Wand", "Pet", "Item", "Quest Item", "Resource", "Necklace", "Misc", "Ground", "House", 
              "Wall Item", "Floor Item"]

    # Dictionary to store the categorized items
    categorized_items = {category: [] for category in itypes}

    # Normalize categories (case-insensitive)
    if categories:
        categories = [category.capitalize() for category in categories]

    # Validate categories (check if they exist in the valid types)
    if categories:
        invalid_categories = [cat for cat in categories if cat not in itypes]
        if invalid_categories:
            print(f"Warning: Invalid categories provided: [{', '.join(invalid_categories)}]. These will be ignored.")
        categories = [cat for cat in categories if cat in itypes]  # Keep only valid categories
    
    # Process each inventory item
    for item in inventory_data:
        str_name = item['strName']
        str_type = item['strType']
        url = generate_url(str_name)
        
        # If the item type is in the valid types list or matches the provided categories (case-insensitive), add it
        if str_type in itypes and (categories is None or str_type.capitalize() in categories):
            categorized_items[str_type].append((str_name, url))

    # Print the categorized items
    for category, items in categorized_items.items():
        if items:  # Only print categories that have items
            print(f"\n{category}:")
            for item_name, item_url in items:
                print(f"  {item_name}: {item_url}")

# Function to fetch and print badge data
def get_badges(ccid, categories=None):
    """
    Fetches badges for a character and categorizes them.
    Params:
        ccid (int): Character ID
        categories (list): Optional list of categories to filter badges by (case-insensitive)
    """
    site = 'https://account.aq.com'
    badges_url = f"{site}/CharPage/Badges?ccid={ccid}"
    
    badges_response = requests.get(badges_url)
    badges_data = badges_response.json()  # Assuming the response is in JSON format

    badge_categories = ["Hidden", "Legendary", "Epic Hero", "Battle", "Support", 
                        "Exclusive", "Artix Entertainment", "HeroMart"]

    # Dictionary to store badges by category
    badges_by_category = {cat: [] for cat in badge_categories}

    # Normalize categories (case-insensitive)
    if categories:
        categories = [category.capitalize() for category in categories]

    # Validate categories (check if they exist in the valid categories)
    if categories:
        invalid_categories = [cat for cat in categories if cat not in badge_categories]
        if invalid_categories:
            print(f"Warning: Invalid categories provided: [{', '.join(invalid_categories)}]. These will be ignored.")
        categories = [cat for cat in categories if cat in badge_categories]  # Keep only valid categories

    # Process each badge
    for badge in badges_data:
        badge_category = badge['sCategory']
        badge_name = badge['sTitle']
        badge_description = badge['sDesc']
        
        # If the badge category is in the valid categories list or matches the provided categories (case-insensitive), add it
        if badge_category in badge_categories and (categories is None or badge_category.capitalize() in categories):
            badges_by_category[badge_category].append((badge_name, badge_description))

    # Print the badges by category
    for category, badges in badges_by_category.items():
        if badges:  # Only print categories that have badges
            print(f"\nCategory: {category}")
            for badge_name, badge_desc in badges:
                print(f"  {badge_name}: {badge_desc}")