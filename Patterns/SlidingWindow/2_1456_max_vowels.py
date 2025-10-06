"""
Traced sliding window for LeetCode 1456 (Maximum Number of Vowels in a Substring of Given Length)

Question:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Example:
Input: s = "abciiidef", k = 3
Output: 3

"""

def maxVowels(  s: str, k: int) -> int:
        
        vowels = 'aeiouAEIOU'
        # init count in first window of size k
        count = sum(ch in vowels for ch in s[:k])
        # print (count)
        max_count = count

        for i in range(k, len(s)):
            # slide the window
            count += (s[i] in vowels) - (s[i-k] in vowels)
            if count > max_count:
                max_count = count

        return max_count

s = "abciiidef"
res = maxVowels(s, 3)
print(res)

s2 = "aeiou"
res2 = maxVowels(s2, 2)
print(res2)

s3 = "rhythm"
res3 = maxVowels(s3, 3)
print(res3)


"""
Question:
1. Why is this a fixed-size window problem and not variable-size?
Answer:
    - We are looking for the maximum number of vowels in a substring of length k.
    - K is fixed, so we can use a fixed-size window.

2. What if the entire string has no vowels?
Answer:
    - The function will return 0.

3. Whats the time and space complexity?
Answer:
    - Time complexity: O(n)
    - Space complexity: O(1)

4. Could we make it faster than O(n)?
Answer:
    - Yes, we can use a hash table to store the vowels and check if the character is a vowel in constant time.



"""
