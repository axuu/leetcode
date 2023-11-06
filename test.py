class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        if (len(strs) == 1):
            return strs[0]
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        result = ''
        for i in range(len(strs[0])):
            if (first[i] != last[i]):
                break
            result += first[i]
        return result
    
print(Solution.longestCommonPrefix(["",""]))