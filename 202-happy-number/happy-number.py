class Solution:
    def isHappy(self, n: int) -> bool:
        
        def fun(n):
            total = 0
            while n > 0:
                d = n % 10
                total += d * d
                n //= 10
            return total
        
        slow = n
        fast = n 

        while True:
            slow = fun(slow)
            fast = fun(fun(fast))
            
            if slow == fast:
                break

        return slow == 1


