# Chase Game

This is a simple game called **Chase** implemented in Python using the Turtle graphics library.

## Description

***Chase*** is a game where the player controls an arrow-shaped character (chaser) using the arrow keys on the keyboard. The objective is to chase and capture moving targets represented by circles on the screen while avoiding obstacles represented by squares. The player earns points for capturing targets and loses the game if the chaser collides with the borders of the game zone or any obstacles.

## Features

- Two game modes: Normal and Hard Mode.
- Random generation of targets and obstacles.
- Score tracking and display.
- Leaderboard to track high scores.
- Basic GUI using Tkinter for the main menu and leaderboard view.
- Background music and sound effects for an immersive experience.

## Prerequisites

- Python 3.x
- `tkinter` (for GUI)
- `turtle` (for graphics)
- `pygame` (for music)

To install the dependencies, run:

```bash
make dependencies
```

## Usage

1. Run the main script to start the game:

    ```bash
    make runGame
    ```

2. Use the arrow keys to control the chaser and capture targets.

3. Select ***Play*** or ***Play Hard Mode*** to start the game.

4. Enter your name when prompted to save your score to the leaderboard.

5. Select ***View Leaderboard*** to see the high scores.

## Build

To build the package and create a distribution wheel, run:

```bash
make build
```

## Versioning

To view the current version (based on git tags), run:

```bash
make version
```

## Clean Up

To clean up build files, run:

```bash
make clean
```

## Credits

- Music by [Toby Smith](https://pixabay.com/users/tobylane-15168815/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=115826) from [Pixabay](https://pixabay.com/music/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=115826)
- Music by [Lesiakower](https://pixabay.com/users/lesiakower-25701529/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=173553) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=173553)
- Music by [Maksym Dudchyk](https://pixabay.com/users/white_records-32584949/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=223905) from [Pixabay](https://pixabay.com/music/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=223905)
- Music by [Oleksii Holubiev](https://pixabay.com/users/loksii-40853646/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=211881) from [Pixabay](https://pixabay.com/music/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=211881)
- Sound Effect from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=38511)

## License
This project is licensed under the MIT License. See the [LICENCE](LICENSE) file for details.
