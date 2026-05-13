from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
    
def HeightWallKickLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via wall kick + ledge grab."""
    """These should return requires strings, inside parenthesis if have outer and/or (for safety)"""
    return "(|Wall Kick| AND (|Ledge Grab| OR |Side Flip|))"
    
def HeightDoubleJumpWallKick(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via double jump + wall kick."""
    return "(|Wall Kick| AND (|Triple Jump| OR |Ledge Grab| OR |Side Flip|))"
    
def HeightSideFlipLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via side flip + ledge grab."""
    return "(|Triple Jump| OR (|Side Flip| AND |Ledge Grab|) OR (|Wall Kick| AND (|Ledge Grab| OR |Side Flip|)))"
    
def HeightWallKick(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via wall kick."""
    return "(|Triple Jump| OR (|Side Flip| AND |Ledge Grab|) OR |Wall Kick|)"
    
def HeightSideFlip(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via side flip."""
    return "(|Triple Jump| OR |Side Flip| OR |Wall Kick|)"
    
def HeightBackflip(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via backflip."""
    return "(|Triple Jump| OR |Side Flip| OR |Backflip| OR |Wall Kick|)"
    
def HeightLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via ledge grab."""
    return "(|Triple Jump| OR |Side Flip| OR |Backflip| OR |Ledge Grab| OR |Wall Kick|)"
    
def HeightKick(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump high enough to reach a platform reachable via jump + kick."""
    return "(|Triple Jump| OR |Side Flip| OR |Backflip| OR |Ledge Grab| OR |Kick| OR |Wall Kick|)"
    
def DistLongJumpWallKickLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via long jump + wall kick + ledge grab."""
    return "(|Triple Jump| OR (|Long Jump| AND |Ledge Grab| AND |Wall Kick|))"
    
def DistLongJumpLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via long jump + ledge grab."""
    return "(|Triple Jump| OR (|Long Jump| AND (|Ledge Grab| OR |Wall Kick|)))"
    
def DistLongJump(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via long jump."""
    return "(|Triple Jump| OR |Long Jump|)"
    
def DistDive(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via jump + dive."""
    return "(|Triple Jump| OR |Long Jump| OR |Dive|)"
    
def DistKick(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via jump + kick."""
    return "(|Triple Jump| OR |Long Jump| OR |Dive| OR |Kick|)"
    
def DistWallKickLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via jump + wall kick + ledge grab."""
    return "(|Triple Jump| OR |Long Jump| OR |Dive| OR |Kick| OR (|Wall Kick| AND |Ledge Grab|))"
    
def DistLedgeGrab(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Player can jump far enough to reach a platform reachable via jump + ledge grab."""
    return "(|Triple Jump| OR |Long Jump| OR |Dive| OR |Kick| OR |Ledge Grab|)"
