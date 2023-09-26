# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Quentin Cole Schuelke

# Student UT EID: qcs86

# Course Name: CS 313E

# Unique Number: 52590

# Output: True or False
def are_anagrams(str1, str2):
    sorted_1 = sorted(str1)
    sorted_2 = sorted(str2)

    if sorted_1 == sorted_2:
        return True
    else:
        return False



# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    families = [lst[0]]
    for word in lst:
        not_count = 0
        for fam in families:
            if not are_anagrams(word, fam):
                not_count += 1
        if not_count == len(families):
            families.append(word)

    return len(families)



def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
