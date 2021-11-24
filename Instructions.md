# PS3
## Deadline: 05.12.2021 - 23:00

In this assignment, you will learn how to apply your knowledge of dictionaries and recursion to solve different problems. 
Note that this assignment, like any other assignment, will be graded via autograder with **additional different** test cases. We will check your code to make sure that your solution is recursive in Problem 2.

Implement all parts as functions, which takes necessary inputs and returns the expected outputs. Use of additional global variables are not allowed. You should not modify the main scope other than defining functions at dedicated `YOUR CODE HERE` sections and calling them at dedicated `None` lines.  

## Problem 1: Privacy: Encrypting Telefon Numbers

We are given a dictionary of people's names and their telephone numbers as strings. We want to store these numbers in a secure manner. To do so, we will encrypt the numbers with add & shift encryption. 

Suppose that our encryption formula is adding 2 and shifting by 1, and we have a telephone number as 
```
4875740312 
```
Then, our formula will iterate over this number digit by digit, and apply our formula. 

At iteration 1, we have 4+2=6 at index 1 (0+1).  
At iteration 2, we have 8+2=0 at index 2 (1+1).  
...  
At iteration 10, we have 2+2=4 at index 0 (9+1).

The resulting encrypted number should be:
```
46097962534
```
Notice that both the encryption and shifting positions work in a circular manner. That is, for encryption, if the result of addition by 2 is bigger or equal to 10, we simply take the last digit, which is 0. Similarly, for shifting, the number at the last index of input gets shifted by 1, so it ends up at the first index.    

**Hint:** Do not assume that add and scale parameters are always positive.

### Part 1: Encrypt

Given a dictionary of people's names and their telephone numbers, and add and shift scalars, return a dictionary of resulting encrypted numbers with corresponding names of people.  

### Part 2: Decrypt

Given a dictionary of people's names and their encrypted telephone numbers, with add and shift scalars used for encrypting them, undo the encryption. 

**Hint:** Notice that given the output of Part 1 with the same add and shift scalars, you must be able to return the original dictionary that was given as input to Part 1. You can use this testing as a sanity check.


## Problem 2: Recursive Word Game

We are given a list of unique letters. We want to find all possible permutations of any length using those letters to form meaningful single words. To check if the word is meaningful or not, we are also given a predefined dictionary with acceptable words as keys, and their scores as values that represent the word's uniqueness/rareness. 

For simplicity, let's divide the task into 2 steps.

### Part 1: Form all possible sequences

In this part, you are given a list of letters as input, and you should return all permutations of these letters that form sequences of any length.

**Example:** 

Given following letters as input
```
a b c
```
your function should return 
```
["a","b","c",
"aa","ab","ac","ba","bb","bc","ca","cb","cc",
"aaa","aab","aac","aba","abb","abc","aca","acb","acc","baa","bab","bac","bba","bbb","bbc","bca","bcb","bcc", "caa","cab","cac","cba","cbb","cbc","cca","ccb","ccc"].
```
**Note 1:** The order of the created sequences is not important. The one above is just an example.

**Note 2:** Note that repeating letters is allowed. 


### Part 2: Calculate the score given sequences

In this part, you are given a dictionary that has the accepted words as keys and their scores as values. After finding all sequences at Part 1, check if each sequence is a meaningful word using this dictionary, and if it is, update your score with the value of that word. 

**Example:** 

Suppose that the given set of letters are
```
d e f o g n u 
```
and the accepted_words dictionary is as follows
```
accepted_words = {"node":3, "sun":2, "gone":4, "fondue":6, "hit":1, "car":2, "god":3, "put":1, "fee":4, "due":3,"end":2, "go":1, "done":4, "odeon":5, "bb":1}
```
Then, it is straightforward to see that the following words should be in our list of generated sequences: "node", "gone", "fondue", "god", "fee", "due", "end", "go", "done", "odeon". Then, our function should return 35 which is the sum of values of these words.

**Note:** Do not iterate over the dictionary to see if we have the letters necessary and calculate score in that way. Instead, you should use your output from Part 1, and check if each generated word is in this dictionary or not. 


### Part 3: Combine Part 1 & Part 2 for efficiency

When you look at the output of Part 1, you can notice that we are returning all the generated sequences, including irrelevant ones. In other words, by storing all possible sequences, we are using more memory than we actually need. Instead, we can immediately check the score of a generated sequence at any recursion loop, and update our overall scores accordingly. 

**Note:** You can compare the output of this efficient version to the output of naive versions. Given the same inputs, the outputs should be the same.

**Example:** Using the same set of letters as in the example of Part 1, 
```
a b c
``` 
we can only generate the word `"bb"` in accepted_words dictionary. Then, your function should return the value of "bb" which is `1`. 


## Problem 3: Binary Palindromes

Palindromes are sequence of characters that are identical forward and backward.  
In this problem, you are given an integer `length` and you are expected to return all possible binary palindromes that have length `length`. You should use recursion. The order of your list is not important.

**Example:** 
Given `length=3`, your function should return 
```
["000", "010", "101", "111"]
```

