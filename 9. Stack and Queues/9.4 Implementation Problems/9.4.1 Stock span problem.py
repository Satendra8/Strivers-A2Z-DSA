"""
Q. Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
"""

class StockSpannerBrute():
    """
    Brute Force Approach
    1. store all elements in array
    2. keep checking and count till previous is smaller or equal to
    4. push new price and return smaller count
    """

    def __init__(self):
        self.stack = []
        

    def next(self, price):

        count = 1
        n = len(self.stack)

        for i in range(n-1, -1, -1):
            if self.stack[i] <= price:
                count += 1
            else:
                break
        self.stack.append(price)
        print(count)


class StockSpanner():
    """
    Optimal Approach
    1. store prev greater element along with its index
    2. calculate the ans by subtracting the current and prev index
    Time Complexity: O(N), for overall operations
    Space Complexity: O(N)
    """

    def __init__(self):
        self.stack = []
        self.size = 0
        

    def next(self, price):
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.size += 1
        ans = self.size - 0
        if self.stack:
            ans = self.size - self.stack[-1][1]
        self.stack.append((price, self.size))
        print(ans)

stockSpanner = StockSpanner()
stockSpanner.next(100);# return 1
stockSpanner.next(80); # return 1
stockSpanner.next(60); # return 1
stockSpanner.next(70); # return 2
stockSpanner.next(60); # return 1
stockSpanner.next(75); # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85); # return 6