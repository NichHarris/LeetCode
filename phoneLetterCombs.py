class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numbers = { "2": ["a", "b", "c"],
                    "3": ["d","e","f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        
        if digits == "":
            return None
        current = [""]
        
        for digit in digits:
            nextVals = []
            for val in current:
                for char in numbers[digit]:
                    nextVals.append(val + char)
                    
            current = nextVals
        return current