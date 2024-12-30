# Adventure Quest Worlds Character Page Extraction
- It will extract AQW character page, then automatically categorize them. It will extract badges and inventory.
- Main parameter is ccid. 
- Last Update: 31 Desember 2024

### Example usage
1. `get_inventory(10456604)`
2. `get_inventory(10456604, ["class", "armor"])`
3. `get_badges(10456604, categories=["support", "exclusive"])`
4. `get_inventory(10456604, categories=["InvalidCategory"])`
5. `get_character_id(pendekar muda)`