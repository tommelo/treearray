# MIT License
#
# Copyright (c) 2018 tommelo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# pylint: disable=C0103,C0301,W1202,W0212

class TreeArray(object):
    """
    The TreeArray class.

    This is a helper class to find the minimum path sum of a
    given 'integer triangle' represented as an array.

    E.g.:

    The array [1,2,3,4,5,6] would represent the triangle

      1
     2 3
    4 5 6

    and the minimum path sum(shortest path) would be 7(1 + 2 + 4).

    All the credits of the algorithm goes to John Kurlak that shared
    a modified Java version of the Dijkstra's algorithm to solve this
    challenge.
    You can find the Java version on Quora:
    https://www.quora.com/Given-a-triangle-find-the-minimum-path-sum-from-top-to-bottom-Each-step-you-may-move-to-adjacent-numbers-on-the-row-below
    """

    __key = object()

    def __init__(self, key, tree):
        assert(key == TreeArray.__key), \
            "TreeArray objects must be created using TreeArray.make_tree([])"
        self.tree = tree

    def __sum_to_n(self, n):
        if n < 0:
            return 0        
        return n * (n + 1) / 2

    def __index_from_row_col(self, row, col):
        return self.__sum_to_n(row) + col

    def __shortest_path_tree(self, tree, min_costs, row, col):
        if row == 0:
            min_costs[0] = tree[row][col]
            return min_costs[0]
            
        min_value = -1
        if col - 1 >= 0:
            min_value = min_costs[self.__index_from_row_col(row - 1, col - 1)]
            
        if col < len(tree[row - 1]):
            cost = min_costs[self.__index_from_row_col(row - 1, col)]
            if min_value == -1:
                min_value = cost
            
            min_value = min(min_value, cost)
        
        min_cost = tree[row][col] + min_value
        min_costs[self.__index_from_row_col(row, col)] = min_cost

        return min_cost
    
    def shortest_path(self):
        if not self.tree:
            return 0
            
        rows = len(self.tree)
        nodes = self.__sum_to_n(rows)
        min_costs = [None] * nodes

        for row in range(rows):
            cols = len(self.tree[row])
            for col in range(cols):
                self.__shortest_path_tree(self.tree, min_costs, row, col)
                    
        row = rows - 1
        cols = len(self.tree[row])
        min = -1

        for col in range(cols):
            cost = min_costs[self.__index_from_row_col(row, col)]
            if cost < min or min == -1:
                min = cost
                        
        return max(0, min)

    @classmethod
    def make_tree(cls, array):
        assert array, \
            "The array cannot be empty"

        tree = []
        count = 1

        array.reverse()

        while len(array) > 0:                
            aux = []
            for _ in range(count):
                aux.append(array.pop())

            tree.append(aux)
            count += 1
        
        return TreeArray(cls.__key, tree)
