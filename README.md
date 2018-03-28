# Discriminant Ordering

## Intro

The Discriminant Ordering (DO) metric is an alternative method of measuring the "similarity" between 2 functions which aren't necessarily 1-to-1 mappings between one another. Rather than compute the correlation between two functions (f(x) vs g(x)), DO iteratively compares the ordering any all points in a space (i.e. x and x') after being mapped with the compared functions f(x) and g(x).

## Calculation Details

The DO metric considers the way two separate functions, f(x) and g(x), map the same dataset. For any pair of inputs from the space, x and x', we compare the "ordering" between f(x) and f(x') with that of g(x) and g(x'). The Heavi-side step function is then used to determine whether function f and function g map those two inputs with the same relative ordering. So the DO is can be written as

<p align="center"><img src="images/DO_equation.png" alt="DO" width="300px"/></p>

This can be thought of graphically by the diagram below

<p align="center"><img src="images/DO_calc_example.png" alt="DO_calc_example" width="600px"/></p>

When the two mappings are perfectly similiar or perfectly dissimilar (i.e. opposit ordering), summing all DO and normalizing to 1 yields the result 0 and 1, respectively. When the mappings are not at all related (i.e. the ordering is 50% similar and 50% dissimilar), summing over all DO-> 0.5. We can then map this to a more convenient scale by taking

<p align="center"><img src="images/DO_norm.pdf" alt="DO_norm" width="170px"/></p>

so, in the end,

<p align="center"><img src="images/DO_legend.pdf" alt="DO_legend" width="250px"/></p>

## Installing the discriminant ordering package

### From pip

The discriminant ordering calculation is available on pypi. To install,

```python
pip install discriminant_ordering
```

the discriminant ordering is designed to depend on numpy.

### Manual installation

Download the package from github

```
git clone https://github.com/tfaucett/discriminant_ordering.git
cd discriminant_ordering
```

and run the setup script

```python
python setup.py install
```

## Using discriminant_ordering

### General Usage

Import the package

```python
from discriminant_ordering import DO
'''

the function requires 4 inputs:
-fx = The mapping for your first function (e.g. f_signal)
-

```python
DO(fx=x, gx=y, target=targets, n_data=)
'''