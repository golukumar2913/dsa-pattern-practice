class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums) 
        pos = []
        neg = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)  

        if len(neg) == 0:
            return [x * x for x in pos ]    

        if len(pos) == 0:
            res = [x* x for x in neg]  
            res.reverse()
            return res       
        
        neg = [x * x for x in neg] [:: -1]
        pos = [x * x for x in pos]
        n = len(neg)
        p = len(pos)
        result = []

        i = j = 0

        while i < n and j < p :
            if neg[i] <= pos[j]:
                result.append(neg[i])
                i += 1
            else:
                result.append(pos[j]) 
                j+=1   
         
        while i < n :
            result.append(neg[i])
            i += 1

        while j < p:
            result.append(pos[j]) 
            j +=1   

        return result     


