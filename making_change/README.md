# Making Change

## Description

This project is part of the **Holberton School interview preparation** track.
The goal is to determine the **fewest number of coins** needed to reach a given
amount, using a list of coin values where each value is available in unlimited
quantity.

The runtime of the solution is evaluated, so the algorithm must be efficient.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code follows the `PEP 8` style (version 1.7.x)
- All files are executable

## Task

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount `total`.

- **Prototype:** `def makeChange(coins, total)`
- **Return:** fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin is always an integer greater than `0`
- Each coin value can be used an unlimited number of times

## Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

$ ./0-main.py
7
-1
```

## Files

| File | Description |
|------|-------------|
| `0-making_change.py` | Function `makeChange` that returns the fewest number of coins needed to meet `total` |
| `README.md` | Project description |

## Repository

- **GitHub repository:** `holbertonschool-interview`
- **Directory:** `making_change`

## Author

**Thomas** — [Corbel99](https://github.com/Corbel99)
