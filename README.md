# NYTSpellingBee
A Python program designed to assist players in finding all possible words based on a set of letters from the New York Times [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) puzzle. The program reads a list of valid words and filters them according to the rules of the game, ensuring that each word meets the criteria for length and letter usage.

## NYT Puzzles and codes
| Puzzles        | Code       |
|----------------|----------------|
| [Wordle](https://www.nytimes.com/games/wordle/index.html)    | [NYTWordle](https://github.com/FarnoodID/NYTWordle)           |
| [Letter Boxed](https://www.nytimes.com/puzzles/letter-boxed) | [NYTLetterBoxed](https://github.com/FarnoodID/NYTLetterBoxed) |
| [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) | NYTSpellingBee |
| [Sudoku](https://www.nytimes.com/puzzles/sudoku)             | [NYTSudoku](https://github.com/FarnoodID/NYTSudoku)           |
| [Pixletters](https://pixletters.com/)                        | [Pixletters](https://github.com/FarnoodID/Pixletters)         |

## Features
- **Word Selection**: The program uses a predefined list of words stored in `words.txt`.
- **User Input**: Players enter a string of letters with the center letter at the beginning, allowing the program to identify valid words.
- **Word Filtering**: The program filters words based on the following criteria:
  - Words must include the specified center letter.
  - Words must be at least four letters long.
  - Words can only contain the letters provided by the user.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/FarnoodID/NYTSpellingBee.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NYTSpellingBee
   ```
### Usage
1. Run the program:
   ```bash
   python NYTSpellingBee.py
   ```
2. The program will prompt you to enter the letters, starting with the center letter followed by other letters. For example, enter:
   ```text
   bozinrg
   ```
3. The program will then display all available words that can be formed with those letters.
## Example Interaction
If you enter ``bozinrg``, the program will filter through words.txt and return all valid words that include ``b``, ``o``, ``z``, ``i``, ``n``, ``r``, and ``g`` while ensuring that at least one instance of ``b`` (the center letter) is included in each word.
