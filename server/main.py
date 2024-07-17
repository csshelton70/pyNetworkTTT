def add(a: int, b: int) -> int:
    """Adds two integers together

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: sum of integers
    """
    return a + b




##  What should the server do?
"""
    Allow the connection of exactly two players
        if a 3rd connects, reject it nicely
    
    when two players are connected, it should start a game and notify players

    it should store the game state (3x3 grid), player ids, etc.

    it should detect winning or losing and notify players

    it should reject invalid moves

    
"""