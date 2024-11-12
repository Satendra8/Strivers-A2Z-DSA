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