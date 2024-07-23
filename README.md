# AI Software Engineer Code Challenge

Welcome to the AI Software Engineer Code Challenge for Orbis Labs. This challenge is designed to assess your understanding of basic Python concepts, particularly focusing on custom class implementation and data handling.

# Setup Steps:
1. Navigate to [challenge](https://github.com/thefish18/AISoftwareEngineerExam)
2. Fork The Repository:
   - Click the "Fork" button at the top right of this page to create a copy of this repository under your own GitHub account.
3. Clone the Repository:
   - `git clone https://github.com/YOUR_USERNAME/AISoftwareEngineerExam.git`
4. Python Version:
   - This challenge was written in `python=3.10` but any similar version should work.
5. Dependencies:
   - This repository only uses packages in the standard library so no `pip installs` are necessary.

# Challenge:
Your task is to open dataset.py and implement the EvenDataset class. This class should subclass _IntDataset and correctly implement the `__len__` and `__getitem__` methods.

- EvenDataset initialization takes parameters `a` and `b`
- EvenDataset returns even numbers from interval [a, b)
- you can assume: `b` > `a` > 1

## Expected Functionality
```python
dset = EvenDataset(2, 10)
print(dset[0])  # Output: 2
print(dset[1])  # Output: 4

```
## Checklist:
- [ ] Your implementation must work for any values `b` > `a` > 1
- [ ] Your implementation should accept a slice (e.g. `dset[1: 3]`) in which case a list of ints is returned
- [ ] Your implementation does __not__ need to work with negative indexes or slices with negative values

## Timing
Once you have a solution you are happy with:
- run `python -m time_dataset` from your repo root in terminal/command line

If you want to try multiple implementations you can pass `--module_name` and/or `--class_name` to `python -m time_dataset`.
Run `pyton -m time_dataset --h` for help.

## Submission
When you have a solution you are happy with:
1. push your local repo to github
   - `git push origin main`
2. Navigate to [challenge](https://github.com/thefish18/AISoftwareEngineerExam) > Pull requests > New pull request > compare across forks
3. Your PR should attempt to merge into AISoftwareEngineerExam/submissions

# Explanation of Dunder Methods
Dunder methods, also known as "magic methods," are special methods in Python that begin and end with double underscores `(__)`. They allow instances of classes to interact with Python's built-in operators and functions, enabling custom behavior.
For example the `__len__` method allows the use of the `len()` function on an instance of your class.

```python
class MyClass:
    def __len__(self):
        return 42

obj = MyClass()
print(len(obj))  # Output: 42
```