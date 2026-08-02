# B3313 Manual Archipelago

This is a Manual APWorld for the Super Mario 64 ROM hack B3313.

**Important: Please do not discuss this APWorld in official Archipelago Discord servers or include this APWorld in games organized in those servers, as the core Archipelago staff wish to distance themselves from B3313.**

# What You Need to Play

- The "latest official release" 1.0.2 version of B3313 (not Unabandoned or any other version). You're on your own obtaining this.
- A compatible emulator, such as Project64 or Parallel Launcher.
- An up-to-date version of [Archipelago](https://archipelago.gg/) (version 0.6.7 at time of writing).
- This apworld (place it in custom_worlds inside your Archipelago folder)
- A player YAML for this apworld (can generate it using ArchipelagoLauncher's "Generate Template Options", or use the file in the release where you got the apworld)
- A save file with sufficient access to the game's locations. Truly accessing every location requires a 100% complete save file, but you can get by with the following:
  - 2 Red Stars (unlocks all moves and overworld)
    - You will eventually need all 13 Red Stars so that B3313 will let you access the final Bowser fight, but this can wait until you reach go mode.
  - 33 Power Stars (unlocks all areas besides final Bowser fight)
  - All Caps
- Optional: [PopTracker](https://poptracker.github.io/) and [Pack for B3313](https://github.com/zodastone/B3313-Manual-APWorld-PopTracker).
  - This has maps for where courses are in each overworld chunk.
  - This can function as a client, i.e. clicking off a location on the map will actually send the location.
    - Sending the victory condition is not currently supported via the tracker; you'll need to use manual client for this.

# What's Randomized

## Items

- Moves
  - Backflip, Side Flip, Wall Kick, Dive, Ground Pound, Ledge Grab: Self-explanatory.
  - Ceiling Hang
    - For hanging from various surfaces, owls, etc.
  - Kick
    - Also includes the "breakdance" kick performed via Z->B while stationary.
  - Long Jump
    - Also includes the B3313-added "flying somersault" performed via Z->B while running.
  - Pole Climb
    - For climbing poles, trees, etc.
  - Progressive Grab
    - This has 2 stages, Punch (can press B to strike objects with Mario's hand), and Grab (can pick up objects)
    - The stage 2 grab includes all types of grabs (punching grab, diving grab, swimming grab)
  - Progressive Triple Jump
    - This has 2 stages, Double Jump and Triple Jump. You always have access to the basic jump.
  - Shell
    - This is the ability to ride around on Koopa Shells.
  - Swim
    - This is the ability to move through water via Mario's swimming/grabbing animations.
    - If you have the Metal Cap, you can enter water and walk along the bottom without Swim.
  - Wall Climb
    - This is the B3313-added ability to climb up certain walls and jump off them.
    - If a wall is climbable, using Wall Kick on it instead is not in logic (for simplicity, since these walls are finicky about when you can do a true Wall Kick off them).
- Caps
- Green Comet: A made-up item that is required to obtain any Green Stars, because gating these behind 120 Stars would not be ideal. Power Stars are pure filler in this APWorld.
- Course Access: These grant you access to the courses inside a certain chunk of overworld. E.g. "Beta Lobby A Courses" grants you access to Snow Slider (B-Roll), Mountain (B-Roll), etc.
- Cannons: Includes the cannon for that course and its sub-areas.
- Red Stars: A configurable amount of these gate the final Bowser fight, and they do nothing else.
- Various filler items

## Locations
- Stars
- Switches
  - 2 of each of the 4 colors.
  - Switches of the same color are still separate checks.
  - You are expected to make a save state before pressing a Yellow Switch (playing the rest of the game without a hat would be painful).
- Yellow ? Boxes (optional)
  - Only includes yellow ? boxes containing coins, enemies, or nothing.
  - Does not include other types of boxes, or boxes containing stars, shells, caps, or which crash the game.
  - Location names for these will all start with "? Box".

# How Progression Works

## Objective
Your objective is to defeat the Bowser in the final Bowser area (Eternal Fort). To do this you will need to obtain:
- The "Bowser's Floor and Endgame Courses" item which gates Eternal Fort
- Enough Red Stars to unlock Eternal Fort (the amount is configurable in the YAML)
- Whatever moves/abilities you need to reach and defeat Bowser
  - Note: The "alternative" final Bowser fight (Eternal Fort (beta)), accessed only through a rare event, is not in logic.

## Overworld Access
You are free to traverse all areas of the overworld (using the moves/abilities you have unlocked).
- Using fast travel is always available.
- The world is always assumed to be in the "post introduction" state, which B3313 normally requires 1 Red Star to access.
  - Playing the game in the "introduction" state is not in logic (i.e. accessing Bowser in the Dark World (Shoshinkai) from Beta Lobby A/E is not in logic). 
- You are expected to place the world in its "ACT 1" state as needed, by waiting on the title screen for ~30 seconds.
- You are expected to reach Star Road without going through the final Bowser fight (ACT 1, Plexal Lobby, Boo cage to Crimson Hallway, die).
- You are expected to set your computer's time to day/night as needed to activate certain day/night-exclusive events.

## Course Access
The "Courses" items grant access to the courses within the corresponding chunk of overworld. These are grouped together in the client and tracker. E.g. "Beta Lobby A Courses" grants you access to Snow Slider (B-Roll), Mountain (B-Roll), etc.
- Some courses can be accessed from multiple places.
- Once inside a course, you are free to access any courses/sub-areas from within that course.

### Wait, What's "Overworld" and What's a "Course"?
Indeed, B3313 blurs the line between the two. The definitive answer is, whatever is in the "Overworld" group in the client/tracker is overworld, everything else is a course.
- Areas accessed from overworld via walking through a door, walking through a loading zone and walking out the other side, or entering a pipe and exiting another pipe are overworld.
- Notable examples: Toad's Hedge Maze, Floating Hotel, and Mr. I's Maze are overworld. Dream Castle and Peach's Cell are courses.

### RNG Course Access Logic
B3313 has some places where a course is accessed via a randomly-occurring event. A prime example is "wf.z64", the dark variant of Whomp's Fortress with a timer challenge.
**Courses are only logically accessible via consistent/high-probability entrances, unless using a low/mid-probabilty entrance is the only option.** Because being gated by RNG is annoying.
Examples:
- Uncanny Moat, Vanish Cap within the Plexus, and Unagi's Tunnel are the only courses that logically require a low/mid-probability entrance.
- The usual entrances to Whomp's Kingdom, Pleasant Pleasant Falls, and Frosty Highlands are in logic, despite them having a rare chance to cause a spooky event.
- wf.z64 is only logically accessible from the warp in the owl cage in Whomp's Kingdom or Flying Fortress.
- Eel Graveyard is only logically accessible from swimming beyond the edge of the moat in Castle Grounds.
- Snow Tunnels is only logically accessible from the consistent entrances in 4th Floor (beta) and Vanilla/Mirrored Upstairs.
- If you encounter an out-of-logic course by chance when attempting to enter an in-logic course, feel free to clear it if you want (you'll have to find it in its proper group in the client/tracker, though).

## Power Star Requirements
- **There are no Power Star requirements for anything.** Power Stars are pure filler.
- Playing on a save file with 33 Power Stars (to unlock 3rd Floor (beta)) should be sufficient to deal with B3313's Power Star requirements.
  - For locations that normally require more Power Stars (e.g. Toad's Rec Room, MIPS, the Whomp's Kingdom SMG2 warp), since it's a manual you can just walk to where the location is and clear the check.
  - Green Stars now require the Green Comet item, instead of the usual 120 Power Stars. Again, just walk to where the Green Stars would be and clear the check.

## Red Star Requirements
**Red Stars gate the final Bowser fight and nothing else.** The number of Red Stars for this is configurable in the YAML.
- The 13 Red Star requirement to access Randomized Realm (the long obstacle course before the final Bowser fight) has been removed, so that Randomized Realm has a reasonable chance to be in logic before go mode.
- Play on a save file with 2 Red Stars to unlock all moves and overworld areas.
  - For Randomized Realm, either swap in a save file with 13 Red Stars as needed, junk the locations there, or clear them without actually doing them in-game.
  - You'll eventually need a save file with 13 Red Stars to enter Eternal Fort to finish the game. If you don't have one, just grab the remaining Red Stars in-game once you reach go mode (or use vanilla Red Star placement for your first seed).

### Dynamic Difficulty
B3313 has a dynamic difficulty feature that kicks in after you get a few Red Stars, adding enemies and Purple Coins, making some bosses harder, and even slightly changing how tall/wide the levels are, depending on how well you play.
- You are expected to swap in a save file with lower dynamic difficulty if needed (looking at you, Prince Bob-omb).
- Taking multiple large amounts of damage is not in logic, even if it would be feasible without any Purple Coins present.
- Logic regarding the heights and distances of jumps considers some potential level scaling, consistent with what a veteran player could accumulate over a single playthrough if scale-increasing moves such as Long Jump are used early and often.
  - It's recommended to make a backup of your save file (from the emulator save folder) and revert to it for each seed, to prevent the boss difficulty and level scaling from stacking over the course of multiple playthroughs.

# Logic Difficulty
The logic with no tricks enabled is intended to have a difficulty level accessible to those already familiar with B3313 and/or SM64EX's movement rando.
- "Frame perfect" jumps are not required.
- Leniency is added in some places where missing a difficult jump would result in death or a lengthy backtrack.
- Maximize the height of basic jumps by getting a running start and holding forward/A throughout. Many pipes are just short enough to be accessible with no moves, even with level scaling active.
- Techniques expected by B3313, such as scaling a tall ledge with a same-side wall jump, are in logic.
- Using a Kick to extend the height or distance of a jump is in logic.
- Using a Shell to jump long distances or scale steep slopes is in logic.

# Options

## Red Stars
- You can choose the total number of Red Stars, and how many Red Stars are required to access Eternal Fort.
- You can choose whether Red Stars are placed in their vanilla locations, are local items, or are placed anywhere.
  - When using vanilla placement:
    - The total number of Red Stars is capped at 13.
    - If the total number of Red Stars is less than 13, a subset of the vanilla locations will be randomly selected. 

## Randomization of Moves
There's no dedicated option in the YAML to control which moves are randomized. If you want to start with all/some moves, then add them to your start_inventory_from_pool.
- E.g. \{"Progressive Triple Jump": 2, "Long Jump": 1, "Backflip": 1, "Side Flip": 1, "Wall Kick": 1, "Dive": 1, "Ground Pound": 1, "Kick": 1, "Pole Climb": 1, "Ledge Grab": 1, "Swim": 1, "Progressive Grab": 2, "Wall Climb": 1, "Ceiling Hang": 1, "Shell": 1\}

## Tricks
The YAML has options to enable various tricks, such as advanced movement techniques and interacting with invisible objects.
- Check the YAML for more details.

# Planned Updates
- Add glitched logic for disabled tricks (dependent on glitched logic being added to Manual for Archipelago)
- Add more of Mario's moves as items (swim, punch, etc.)
- Add more locations (yellow ? boxes)

# Credits
- This APWorld was built on top of [Manual for Archipelago](https://github.com/ManualForArchipelago/Manual), much thanks to Silasary and this project's other contributors.
- Much thanks to the Manual for Archipelago Discord community for the wealth of knowledge and already-answered questions there.

# FAQs
- What version of B3313 is this APWorld for?
  - 1.0.2 (latest "official" release), because it's the version I'm familiar with. Other versions will not have the same stars/locations.
- Why isn't this part of the more general SM64 Hacks APWorld project?
  - B3313 1.0.2 is derived from a decompilation of SM64, so is not compatible with that project's modifications to assembly code or assumptions on save memory layout.
- Are you planning to make a full (non-manual) APWorld of this?
  - Not likely, as my ROM hacking experience is minimal and I already have a large backlog of other projects I want to work on. If you are interested in taking the logic herein and making a non-manual APWorld from this, go for it.
- How do I reach (insert location here)?
  - In this repo, check manual_b3313_zodastone/data/locations.json and regions.json, and search for the relevant location or region. Some of the trickier locations and regions contain comments explaining the logic.
  - The PopTracker pack's maps can help if you aren't sure which course entrance in an overworld chunk leads to the course you're interested in. 
  - The B3313 wiki page on Fandom has a large amount of knowledge about the game, including all the ways each area can be entered. The overworld/course names in this APWorld match the names on the wiki.
  - 99% of the relevant overworld is reachable in Sphere 1. Some trickier cases:
    - Painting Museum: From the start of the game, take the far back door to Toad Hall, then the first pipe on the left and the door to Peach Upstairs, then the door on the left, and the door on the left again.
    - Polygonal Chaos: Follow the above to Peach Upstairs, then keep going forward through doors until you reach Polygonal Chaos. This puts you in an elevated spot near SGI Indy, where you can access all the courses here without needing to scale the big steps.
    - Vanilla Lobby Toad: Follow the above to Polygonal Chaos, then walk forward a long way to the set of double doors. This will put you right by the Toad, without needing to fly through the window.
    - Uncanny Courtyard Red Coins with hidden_stuff enabled: You don't have to jump over the wall if you approach from the back side. Start with Beta Lobby B and Plexal Upstairs, then take the upper door and the crescent moon door to Cryptic Hideout, then the door on the left to Funhouse, then the door hidden behind a texture with red hills on it.
    - Star Road: Set the game to ACT 1 by waiting on the title screen for ~30 seconds. Go to Plexal Lobby, then take the Boo cage to Crimson Hallway. Dying will then take you to a darkened version of the ending sequence which you can follow to Star Road. The pipes in Star Road (and most other places) are just short enough to enter with a basic jump.
    - Basement Maze Star Box without Swim: Go to Parallel Lobby, take the door that leads to the Hazy Memory Cave portal, take the opposite-side door, fall down the fountain on the opposite side of the hedge maze, and take the pipe.