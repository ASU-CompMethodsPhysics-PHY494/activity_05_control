# Activity 05: Control structures
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2021/02/02/04_Python_2/ for help.

## Processing data in a loop: batch temperature conversion

In `temperatures.py` you are given the list
```python
temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0]
 ```

The conversion from a temperature θ in Fahrenheit to *T* in Kelvin is


          5
      T = - (θ - 32) + 273.15
          9


1. Edit `temperatures.py` so that each temperature in Fahrenheit in the list
   is converted to Kelvin and stored in a new list `temp_Kelvin`.

2. Add code to `temperature.py` to print a table of the temperature in
   F and in K side by side by iterating through the lists temperatures
   and temp_Kelvin simultaneously.

   Hints:

   * You can use `len()` and `range()`

   * Assign individual values to variables `T_K` and `theta_F` and
     print each line with the format `print("{0:6.1f} F {1:6.1f}
     K".format(theta_F, T_K))`.

## Generate values from -10 to 10 in steps of 0.25

We often need a range of values at arbitrary step size, e.g., for
plotting a function on a grid. *The `range()` function only provides
integer numbers.* Find a way to generate a list of numbers from
`start=-10` to `stop=10` (exclusive) with `step=0.25`, i.e., `[-10.,
-9.75, -9.5, ..., 9.5, 9.75]`.

Put your code into file `grid.py` and store your list in the variable `x_grid`.

Hints:
* You can use a list comprehension for improved readability or an explicit loop with appending to a list.

* Think about how to use `range()` and how to use the resulting
  integers `i` to generate the floating point numbers: `x = i * step +
  start`


## Reading input

Write a program `alternatesum.py` that

1. reads numbers from input until an empty line is encountered
2. stores the numbers in a list `numbers`
3. calculates the "alternating sum" `numbers[0] - numbers[1] +
   numbers[2] - numbers[3] + ...` and stores it in a variable `asum`. (You can
   also print `asum`.)

## Guessing game

Write a program `guessinggame.py` that takes a single number `guess`
as input and compares it to a preset integer number
`secret_number`. Tell the player if their guess was "too low", "too
high", or that they "guessed the number".

