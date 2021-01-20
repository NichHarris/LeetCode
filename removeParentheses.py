class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Balance string

        stack = []
        result = []
        indexes = set()
        
        for i, char in enumerate(s):
            # Is the current character an index?
            if char not in "()":
                continue
            # Current char is a index open
            if char == "(":
                stack.append(i)
            elif not stack:
                indexes.add(i)
            else:
                stack.pop()
        
        indexes = indexes.union(set(stack))
        
        for i, char in enumerate(s):
            if i not in indexes:
                result.append(char)
        
        return "".join(result)