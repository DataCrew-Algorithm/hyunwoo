# # 실패(banned가 비어있을 경우가 있을 수 있음)
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        max = 0
        max_str = ""
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(",", "")
        paragraph = paragraph.replace(".", "")
        if banned[0] in paragraph:
            paragraph = paragraph.replace(banned[0], "")
        lst = paragraph.split()
        for i in lst:
            if lst.count(i) > max:
                max = lst.count(i)
                max_str = i

        return max_str

# ===============================================================================================

# # 실패(예외 생김)
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        max = 0
        max_str = "a"
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(",", "")
        paragraph = paragraph.replace(".", "")
        for j in banned:
            if j in paragraph:
                paragraph = paragraph.replace(j, "")
        lst = paragraph.split()
        for i in lst:
            if lst.count(i) > max:
                max = lst.count(i)
                max_str = i

        return max_str


# ===============================================================================================

# 실패 (예외존재)
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        max = 0
        max_str = "a"
        paragraph = paragraph.lower()
        paragraph = re.sub("[^\w]", "", paragraph)
        for j in banned:
            if j in paragraph:
                paragraph = paragraph.replace(j, "")
        lst = paragraph.split()
        for i in lst:
            if lst.count(i) > max:
                max = lst.count(i)
                max_str = i

        return max_str

# ===============================================================================================
# 실패 (예외 존재)
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        max = 0
        max_str = ""
        paragraph = paragraph.lower()
        paragraph = re.sub("[^\w]", " ", paragraph)
        lst = paragraph.split()
        for j in lst:
            if j in banned:
                lst.remove(j)
        for i in lst:
            if lst.count(i) > max:
                max = lst.count(i)
                max_str = i

        return max_str


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
ban = ["hit"]


sol = Solution()
print(sol.mostCommonWord(paragraph, ban))
