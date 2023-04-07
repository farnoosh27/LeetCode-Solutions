from collections import defaultdict


def groupAnagrams(strs):
    # a-z --> 26 unique characters 
    # for example: count[a-z] = 1e, 1a, 1t --> Hashmap
    # key is the 1e, 1a, 1t and our value is gonna be the list of anagrams
    # since we are using a hashmap and all we are doing is counting the characters of each
    # the overall time complexity would be O(m.n.26)--> the actual time complexity O(m.n)
    res = defaultdict(list) # mapping charCount to list of anagrams
    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            # for example: a = 80-> 0. 80-80
            # b = 81 -> 1, 81-80
            # then we count it by one to count how many of each character we have
            count[ord(c)-ord("a")] += 1 

        # we now want to group all the anagrams
        # but since the count may not have existed before, we change it to defaultdict
        res[tuple(count)].append(s)

    return res.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))