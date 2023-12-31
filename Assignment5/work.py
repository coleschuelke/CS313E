"""
  File: work.py
  Description: A comparison between linear and binary search

  Student Name: Quentin Schuelke
  Student UT EID: qcs86 

  Partner Name: Daniela Cordon
  Partner UT EID: dc47324

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09/11/23
  Date Last Modified: 09//23
"""

import sys
import time
# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    term = v
    power = 1
    series_sum = term
    while term > 0:
        term = v//(k**power)
        series_sum += term
        power += 1

    return series_sum






# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    v = 0
    series_sum = 0

    while series_sum < n:
        series_sum = sum_series(v, k)
        v += 1

    return v - 1




# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    lo = 0
    hi = n

    while lo < hi - 1:
        mid = (lo + hi) // 2

        if sum_series(mid, k) < n:
            lo = mid
        else:
            hi = mid
    return hi



def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for i in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
