# UTF-8 Validation

## Description

This project focuses on validating whether a given sequence of integers represents a valid UTF-8 encoding.

Each integer in the input list represents one byte of data. The validation is based on the UTF-8 encoding rules, where a character can be represented using between 1 and 4 bytes.

The goal is to understand how UTF-8 represents characters using binary patterns and how to determine whether a sequence of bytes follows the expected structure.

## Learning Objectives

Through this project, we learn how to:

- Understand the basic principles of UTF-8 encoding.
- Work with binary representations of integers.
- Identify the different types of UTF-8 bytes.
- Determine whether a sequence of bytes represents valid UTF-8 data.
- Manipulate bits using Python.
- Apply algorithmic reasoning to validate a sequence of data.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)
- All files must:
  - Start with `#!/usr/bin/python3`
  - End with a new line
  - Be executable

## Project Structure

```text
utf8_validation/
├── 0-validate_utf8.py
├── 0-main.py
└── README.md
```

## Task

### 0. UTF-8 Validation

Implement:

```python
def validUTF8(data)
```

The function must return:

- `True` if the given data represents a valid UTF-8 encoding.
- `False` otherwise.

The input is a list of integers, with each integer representing one byte of data. Only the 8 least significant bits of each integer need to be considered.

A UTF-8 character can contain between 1 and 4 bytes, and the data may contain multiple characters.

## UTF-8 Encoding Patterns