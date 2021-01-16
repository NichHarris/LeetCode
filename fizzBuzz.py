class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,n+1):
            if i%5 == 0 and i%3 == 0:
                ans.append("FizzBuzz")
            elif i%5 == 0:
                ans.append("Buzz")
            elif i%3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans

# Hash Table

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        hashTable = {3: "Fizz", 5: "Buzz"}
        for i in range(1,n+1):
            numStr = ""
            for key in hashTable.keys():
                if i%key == 0:
                    numStr += hashTable[key]
            if not numStr:
                numStr = str(i)
                
            ans.append(numStr)        
        return ans