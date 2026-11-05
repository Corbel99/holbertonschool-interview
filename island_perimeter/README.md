# Island Perimeter

## Description

This project is part of the **Holberton School Interview Preparation** track.
The goal is to write a Python function that computes the perimeter of a single
island described in a grid of integers.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code follows the `PEP 8` style (version 1.7)
- Importing modules is not allowed
- All modules and functions must be documented
- All files must be executable

## Task

### 0. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of
the island described in `grid`.

- `grid` is a list of lists of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the
  water surrounding the island)

**File:** `0-island_perimeter.py`

## Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

$ ./0-main.py
12
```

## Files

| File | Description |
|------|-------------|
| `0-island_perimeter.py` | Function `island_perimeter(grid)` returning the perimeter of the island |
| `README.md` | Project description |

## Repository

- GitHub repository: `holbertonschool-interview`
- Directory: `island_perimeter`

## Author

**Thomas** — [Corbel99](https://github.com/Corbel99)
