## 49 group anagrams
### medium 
### string
## Questions:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

example 1: 

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


example 2: 

Input: strs = [""]

Output: [[""]]

example 3: 

Input: strs = ["a"]

Output: [["a"]]

## Solutions:
The NeetCode solution for this is provided: https://www.youtube.com/watch?v=vzdNOK2oB2E

There are two solutions for this:
1) using regular hashmap for eachone, and then sorting them. --> time complexity: m (nlong(n))
2) (more optimized) each character would be from lower case "a" to lower case "z" so overall 26 characters, so using a data structre like hashmaps with keys as values.

The time complexity of the provided code is O(nmlog(m)), where n is the number of words in the input list and m is the length of the longest word.

The reason for this time complexity is that the code first iterates over each word in the input list and sorts its characters alphabetically using the sorted() function, which has a time complexity of O(m*log(m)) for a word of length m. Then, the code uses the sorted string as a key to a dictionary, which takes constant time on average to insert or retrieve an element.

Therefore, the overall time complexity of the algorithm is the product of the time complexity of sorting a word, the number of words in the input list, and the average time complexity of inserting/retrieving an element from the dictionary, which is also constant on average. 
