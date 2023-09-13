"""
  File: spiral.py
  Description: Function to create a number spiral according to the input dimension and a function to sum the numbers
  surrounding a given number

  Student Name: Quentin Schuelke
  Student UT EID: qcs86 

  Partner Name: Daniela Cordon
  Partner UT EID: dc47324

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09/04/23
  Date Last Modified: 09/04/23

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys


def merge_tuples (tuples_list):
    """Merge the tuples"""
    merged_intervals = set()
    # merge intervals
    for interval in tuples_list:
        lower = interval[0]
        upper = interval[1]
        for comp in tuples_list:
            if (comp[0] < upper) and comp[1] > lower:
                upper = max([comp[1], upper])
                lower = min([comp[0], lower])
            if (comp[1] > lower) and (comp[1] < upper):
                upper = max([comp[1], upper])
                lower = min([comp[0], lower])
        merged_intervals.add((lower, upper))

    merged_intervals = list(merged_intervals)
    merged_intervals.sort()

    return merged_intervals



def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    size_list = [0] * len(tuples_list)
    index = 0
    # create list of interval sizes
    for tuple in tuples_list:
        interval_size = tuple[1] - tuple[0]
        size_list[index] = interval_size
        index += 1

    # bubble sort the intervals and perform the same operation on the tuples list
    for size in size_list:
        for i in range(len(size_list)-1):
            if size_list[i] > size_list[i+1]:
                size_list[i], size_list[i+1] = size_list[i+1], size_list[i]
                tuples_list[i], tuples_list[i+1] = tuples_list[i+1], tuples_list[i]


    


    return tuples_list



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
