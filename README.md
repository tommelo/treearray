# treearray
Minimum path sum of an integer triangle

## About
This is a helper class to find the minimum path sum of a given "integer triangle" represented as an array.

E.g.:

The array ```[1,2,3,4,5,6]``` would represent the triangle:
```
  1
 2 3
4 5 6
```

and the minimum path sum(shortest path) would be **7**(1 + 2 + 4).

## How to use

```python
from treearray import TreeArray

"""
E.g.:

The array [9, 1, 2, 9, 10, 4, 10, 9, 10, 6, 10, 1, 3, 3, 1] would represent the triangle:

      9
     1  2
   9  10  4
 10  9  10  6
10  1  3  3  1

"""

tree = TreeArray.make_tree([9, 1, 2, 9, 10, 4, 10, 9, 10, 6, 10, 1, 3, 3, 1])
print tree.shortest_path_sum() # 22
```
## Credits
All the credits of the algorithm goes to **John Kurlak** that shared a modified Java version of the Dijkstra's algorithm to solve this challenge.

You can find the Java version on Quora: https://www.quora.com/Given-a-triangle-find-the-minimum-path-sum-from-top-to-bottom-Each-step-you-may-move-to-adjacent-numbers-on-the-row-below

## License
This is an open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
