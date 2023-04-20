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
