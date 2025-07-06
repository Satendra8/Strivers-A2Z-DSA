"""
Q. You are an owner of lemonade island, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by given array bills[]). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

NOTE: At first, you do not have any bill to provide changes with. You can provide changes from the bills that you get from the previous customers.

Given an integer array bills of size N where bills [ i ] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:

Input:
N = 5
bills [ ] = {5, 5, 5, 10, 20}
Output: True
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change we return true.
 

Example 2:

Input:
N = 5
bills [ ] = {5, 5, 10, 10, 20}
Output: False
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
"""

def lemonadeChange(bills):
    """
    1. store count of all coins
    2. if coin is 10 (+10, -5), increase count of 10 by 1 and decrease count of 5 by 1
    3. if coin is 20 (-10, -5) or (-5, -5, -5)
    4. if either 5 or 10 becomes 0 before loop iteration return false
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    d = {5: 0, 10: 0, 20: 0}
    for coin in bills:
        if coin == 10:
            if d[5] == 0:
                return False
            d[5] -= 1
        elif coin == 20:
            if d[5] == 0:
                return False
            d[5] -= 1

            if d[10] > 0:
                d[10] -= 1
            elif d[5] > 1:
                d[5] -= 2
            else:
                return False
        d[coin] += 1

    return True


bills = [5,10, 20]
print(lemonadeChange(bills))