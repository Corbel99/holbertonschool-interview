# Lockboxes

## Description

The **Lockboxes** project is an algorithmic problem where we have a collection of locked boxes. Each box can contain keys that allow us to open other boxes.

The goal is to determine whether **all boxes can be opened**, starting with the first box (`boxes[0]`), which is already unlocked.

A key containing the same number as a box allows that box to be opened.

## Requirements

* Python 3
* Ubuntu 14.04 LTS
* PEP 8 style
* All Python files must start with:

  ```python
  #!/usr/bin/python3
  ```

## Function

The project contains the following function:

```python
def canUnlockAll(boxes):
```

### Parameters

* `boxes`: a list of lists of integers.
* Each list represents the keys contained in a box.
* The index of a box represents its number.

### Return value

* `True` if all boxes can be opened.
* `False` if at least one box cannot be opened.

## Example

```python
boxes = [[1], [2], [3], [4], []]

print(canUnlockAll(boxes))
```

Output:

```text
True
```

In this example:

* Box `0` is already unlocked.
* Box `0` contains key `1`, so box `1` can be opened.
* Box `1` contains key `2`, so box `2` can be opened.
* Box `2` contains key `3`, so box `3` can be opened.
* Box `3` contains key `4`, so box `4` can be opened.

Therefore, all boxes can be opened.

### Another example

```python
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

print(canUnlockAll(boxes))
```

Output:

```text
False
```

Some boxes cannot be reached from the first box, so the function returns `False`.

## Repository

* **GitHub repository:** `holbertonschool-interview`
* **Directory:** `lockboxes`
* **File:** `0-lockboxes.py`
