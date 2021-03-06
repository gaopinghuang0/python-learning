import unittest
import collections, re

# beats 99.08%
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # optimize by Submission
        ban_set = set(banned)
        paragraph = re.sub(r'[^a-z ]', '', paragraph.lower())
        counter = collections.Counter()
        for word in paragraph.strip().split(' '):
            if word not in ban_set:
                counter[word] += 1
        return counter.most_common(1)[0][0]


# beats 8.65%
class Solution_V1(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # idea: use a counter
        counter = collections.Counter()
        for word in paragraph.split(' '):
            word = re.sub(r'[^a-z]', '', word.lower())
            counter[word] += 1

        for word, count in counter.most_common():
            if word not in banned:
                return word

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        self.assertEqual(self.s.mostCommonWord(paragraph, banned), 'ball')


if __name__ == "__main__":
    unittest.main()
