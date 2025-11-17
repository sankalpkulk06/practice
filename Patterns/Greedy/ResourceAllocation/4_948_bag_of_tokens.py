"""
leetcode 948: Bag of Tokens


Question:
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the maximum possible score you can achieve after playing any number of tokens.

Example 1:

Input: tokens = [100], power = 50
Output: 0
Explanation: You cannot play the only token face up, because you do not have any power.
"""
def bagOfTokens(tokens, power):
    
    # sort tokens in ascending order
    tokens.sort()
    print(tokens)

    # init score
    score = 0
    left = 0
    right = len(tokens) - 1
    maxScore = 0

    # play while left <= right
    while left <= right:
        print(f'left: {tokens[left]}, right: {tokens[right]}, power: {power}, score: {score}, maxScore: {maxScore}')
        # if we have enough power to play the token face up
        if power >= tokens[0]:
            power -= tokens[0]
            score += 1
            left += 1
            maxScore = max(maxScore, score)
        # if we have enough score to play the token face down
        elif score >= 1:
            power += tokens[right]
            score -= 1
            right -= 1
            maxScore = max(maxScore, score)
        else:
            break

print(bagOfTokens([100], 50))
print(bagOfTokens([100,200], 150))
print(bagOfTokens([100,200,300], 200))
print(bagOfTokens([100,200,300,400], 200))
print(bagOfTokens([100,200,300,400,500], 200))
print(bagOfTokens([100,200,300,400,500,600], 200))
print(bagOfTokens([100,200,300,400,500,600,700], 200))
print(bagOfTokens([100,200,300,400,500,600,700,800], 200))
print(bagOfTokens([100,200,300,400,500,600,700,800,900], 200))
print(bagOfTokens([100,200,300,400,500,600,700,800,900,1000], 200))