# HOWTO mini-exam 5 (finals week)

There are two separate problems on this mini-exam,
worth 10 points each.  

## Problem 1: grid (positive sums of columns)

`grid.py` has a class `Grid` that holds a
rectangular grid of integers.  Your job is to
complete the method `some_column_sum_positive`, 
which should return `True` if there is at least
one column in the grid whose sum is positive.


## Problem 2: Refactoring a scrunchy grid

`scrunchy.py` also contains a class that
represents grids of integers, but you have
a rather different task.  `scrunchy.py`
already passes its test cases, but the code
is redundant ... each of the `scrunch`
methods in the concrete subclasses of 
`Scrunchy` contain some redundant logic for
replacing each row in the grid.  Your task is
to *refactor* the `scrunch` method.  You will
need to do three things: 

* Implement a concrete method `scrunch_row` in
  each concrete subclass.
* Replace the abstract `scrunch` method in
  class `Scrunchy` with a concrete method that
  can be inherited by each concrete subclass. 
  This concrete method will call the abstract
  method `scrunch_row`.
* Remove the `scrunch` method from the concrete
  subclasses, so that you use the inherited
  `scrunch` method instead. 
  
When you are finished, your code should still pass
the same test cases, but it will be shorter and
cleaner.  You must complete all three of the steps
above to earn full credit.  Do not change the
header of `scrunch` or `scrunch_row`.  Do not
change the constructor of any class. 
  
