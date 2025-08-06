# TASK 3 - PARALLEL PRS & DEPENDENCIES

## What I Did:
Added two mathematical functions (`square` and `cube`) on separate branches where the cube function needed the square function to work properly. Had to figure out how to manage the PRs so they could be merged in the right order.

## Work Phases:

### 1. Add `square()` function
* **Created branch:** `feature/add-square-function`
* **Implemented:** Basic square function with input validation
```python
@staticmethod
def square(a: float) -> float:
    """Calculate the square of a number."""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    return float(a) ** 2
```
* **Added tests:** Covered positive, negative, zero, decimal, and type validation cases
* **Quality checks:** Ran `pytest tests/` and `flake8 src/ tests/` - everything passed
* **Created PR:** Left it open without merging (like the exercise said to do)

### 2. Add `cube()` function - depends on `square()`
* **Created branch:** `feature/add-cube-function` (from main, not from the square branch)
* **Initial implementation:** Had to use `a ** 3` because the square function wasn't available yet
```python
@staticmethod
def cube(a: float) -> float:
    """Calculate the cube of a number."""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    # TODO: Will be refactored to use square() function after PR merge
    return float(a) ** 3
```
* **Added tests:** Similar test pattern to square function
* **PR documentation:** Made sure to note the dependency and that I'd change it later
* **Status:** Now had two open PRs at the same time

### 3. Managing the merge sequence
* **First:** Merged the square function PR
* **Updated cube branch:** `git checkout feature/add-cube-function` then `git pull origin main`
* **Refactored cube:** Now changed the implementation to use the square function:
```python
@staticmethod
def cube(a: float) -> float:
    """Calculate the cube of a number using square function."""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    square_result = Calculator.square(a)
    return square_result * float(a)
```
* **Verification:** Ran tests to make sure the cube function worked with the square function
* **Updated PR:** Added a note about what I changed
* **Second merge:** Got the cube function PR merged too

### 4. Branch cleanup
* Deleted both feature branches after successful merges
* Kept main branch clean and up-to-date

## Technical Implementation:

### Square Function:
```python
def test_square():
    assert Calculator.square(2) == 4.0
    assert Calculator.square(-3) == 9.0
    assert Calculator.square(0) == 0.0
    assert Calculator.square(2.5) == 6.25
```

### Cube Function (using square):
```python
@staticmethod
def cube(a: float) -> float:
    """Calculate the cube of a number using square function."""
    if not isinstance(a, (int, float)):
        raise TypeError("Argument must be a number")
    square_result = Calculator.square(a)
    return square_result * float(a)
```

## Challenges I Encountered:

### 1. Choosing functions that made sense
Wasn't sure at first what functions to implement that would actually depend on each other. Asked AI for suggestions and it recommended square/cube because it's obvious that cube could use square (a³ = a² × a).

### 2. Getting the branch management right
Had to remember to create the cube branch from main (not from the square branch) so it would actually create the dependency problem the exercise wanted. This meant the cube function couldn't use square at first.

### 3. Writing clear PR descriptions
Needed to make sure anyone looking at the cube function PR would understand it needed the square function merged first. Used AI to help write more professional descriptions after I wrote the basic explanation of what I did.

## What I Figured Out:

### Git Workflow:
* How to handle multiple PRs when one depends on the other
* How merge order actually matters when there are dependencies

### Working with others:
* How to write PR descriptions that explain what depends on what
* How to update your branch after someone else's code gets merged

### Code stuff:
* Going from `a ** 3` to `Calculator.square(a) * a` after the dependency was available showed me how this works in practice
* Sometimes you write a temporary solution first, then improve it later

## What I Accomplished:
Got both functions working - square and cube operations are now part of the calculator. Created 2 PRs total and managed to get them merged in the right order. All the tests are still passing and I cleaned up the branches afterward.

The whole thing showed me how parallel development works when multiple people might be working on related features at the same time.