"""
leetcode 860: Lemonade Change

Question:
You are working at a lemonade stand where each lemonade costs $5. 
Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Return true if you can provide every customer with the correct change, or false otherwise.

Example 1:
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
"""


def lemonadeChange(bills) -> bool:
    
    count = {
        5:0,
        10:0,
        20:0
    }

    for bill in bills:

        # if bill is $5
        if bill == 5:
            count[5] += 1
        
        elif bill == 10:
            # if we have to change of $5
            if count[5] == 0:
                return False
            
            count[5] -= 1   # give change of $5
            count[10] += 1  # take $10 bill

        elif bill == 20:
            # we haev change one $10 and one $5
            if count[10] > 0 and count[5] > 0:
                count[10] -= 1
                count[5] -= 1
            
            # give 3 $5 bills back
            elif count[5] >= 3:
                count[5] -= 3
            
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([10,10]))
print(lemonadeChange([5,5,10,10,20]))
print(lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,5,5,5]))
print(lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,5,5,5]))