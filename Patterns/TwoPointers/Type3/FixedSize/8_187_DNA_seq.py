"""
LC 187: Repeated DNA Sequences

Question:
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

"""

def findRepeatedDnaSequences(s):
    # init 
    seen = set()
    result = set()

    # slide window
    for i in range(len(s) - 10 + 1):
        seq = s[i : i+10]

        # check if the sequence is already in the set
        if seq in seen:
            result.add(seq)
        else:
            seen.add(seq)
    return list(result)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))

"""

Goal:
Return all the 10-letter-long substring that occur more than once in s string

Thought Process:

	○ We can use a window of size 10 
	○ Init a set which stores all the substrings, lets call it "seen"
	(we don't have to store the count, because if the substring is more than once then it is part of result)
	○ Init a "result" set
	○ Iterate from 0 to len(s) - 10 + 1:
		○ Then we get the substring, seq = s[i:i+10]
		○ If the seq is already in the set:
			§ Then add to seq to the "result" set
		○ Else,
			§ Add the seq to seen set
Return "result" 

"""