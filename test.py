class Solution:
    def isValid(s: str) -> bool:
        map = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack = []
        for i in range(len(s)):
            if (s[i] in [')', "]", "}"]):
                if (len(stack) == 0 or map[s[i]] != stack[-1]):
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0


    
print(Solution.isValid("[([]])"))