# Pascal's Triangle

## Description

This project contains an implementation of Pascal's Triangle in Python.

The goal is to create a function that generates Pascal's Triangle up to a given number of rows and returns it as a list of lists of integers.

## Task

### 0. Pascal's Triangle

Create a function:

```python
def pascal_triangle(n):
```

The function returns a list of lists of integers representing Pascal's Triangle of `n`.

### Requirements

* Return an empty list if `n <= 0`.
* `n` is always assumed to be an integer.
* Each row of the triangle must be represented as a list of integers.

For example:

```python
pascal_triangle(5)
```

returns:

```python
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Repository

* **GitHub repository:** `holbertonschool-interview`
* **Directory:** `pascal_triangle`
* **File:** `0-pascal_triangle.py`

## Example

```python
#!/usr/bin/python3

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

print(pascal_triangle(5))
```

Output:

```text
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```
