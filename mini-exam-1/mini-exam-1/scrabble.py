"""
CIS 211 Spring 2021 Week 2 Exam 1

Author: Jacob Burke

Credits: N/A

Created a tile and tray class. Both are then used to tally up scores for
possible scrabble plays
"""

class Tile:
    """An object that has a letter and value identifier"""
    def __init__(self, letter: str, value: int):
        self.letter = letter
        self.value = value

    def __str__(self) -> str:
        """Looks like ('X', 8)"""
        return f"('{self.letter}',{self.value})"

    def __repr__(self) -> str:
        """Looks like Tile('X', 8)"""
        return f"Tile('{self.letter}', {self.value})"

class Tray:
    """List that contains tiles"""
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile: Tile):
        """Add tile to the collection of tiles in this tray"""
        self.tiles.append(tile)

    def __str__(self) -> str:
        """Looks like ('A', 1),('X', 8),('E', 1)"""
        return ",".join([str(t) for t in self.tiles])

    def __repr__(self):
        """Looks like Tray(('A', 1),('X', 8),('E', 1))"""
        return f"Tray({str(self)})"

    def has(self, letter: str) -> bool:
        """Does this tray hold a tile with the specified letter?"""
        if len(self.tiles) == 0:
            return False
        else:
            for tile in self.tiles:
                if tile.letter == letter:
                    return True
            print("False")
            return False

    def would_score(self, word: str):
        new_tray = self.tiles.copy()
        letter_dict = dict
        letter_list = []
        for letter in word: #Loops through each letter in word
            new_tray_index = 0
            letter_in = False
            for tile in new_tray: #Compares tiles in tray to letters in word
                if letter == tile.letter:
                    letter_list.append(new_tray.pop(new_tray_index))
                    letter_in = True
                    break
                else:
                    new_tray_index += 1
            if letter_in == False: #Used to check if letter was not in tray
                return 0
        score = 0 #score counter
        for tile in letter_list:
            score += tile.value #Tallies up score
        return score
