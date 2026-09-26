# ai-tools-lab
# AI Tools Lab

A Python project containing sorting algorithms and utility functions, built as part of an AI Tools and Applications Lab exercise exploring AI-assisted software development workflows (code generation, documentation, and debugging).

## Features

- **Sorting algorithms** — implementations of classic sorting techniques (e.g. bubble sort).
- **Utility functions** — small, reusable helper functions:
  - `is_palindrome(s)` — check whether a string is a palindrome.
  - `count_words(text)` — count the number of words in a text.
  - `celsius_to_fahrenheit(c)` — convert a temperature from Celsius to Fahrenheit.

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/Loveleen-kaur19/ai-tools-lab.git
   cd ai-tools-lab
   
2. Make sure you have Python 3 installed:
   bash
   python --version
3. No external dependencies are required — the project uses only the Python standard library.

## Usage

### Sorting

python
from sorting import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
# Output: [11, 12, 22, 25, 34, 64, 90]

### Utilities

python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

print(is_palindrome("madam"))                 # True
print(count_words("Hello brave new world"))   # 4
print(celsius_to_fahrenheit(100))             # 212.0


## Running Tests

Docstring examples can be verified with:
bash
python -m doctest utils.py


## Contributors

Loveleen Kaur-Loveleen-Kaur19
## License

This project is licensed under the [MIT License](LICENSE).

