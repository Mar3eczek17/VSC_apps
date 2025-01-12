from typing import Optional

def display_cities(cities: list[str], preferences: Optional[str] = None):
    """Provides a list of cities vased on the user's search query and preferences.
    
    Args:
        preferences (str): The user's preferences for the search, like dkiing,
        beach, restaurants, bbq, etc.
        cities (list[str]): The list of cities being recommended to the user.
        
    Returns:
        list[str]: The list of cities being recommended to the user.
    """

    return cities