from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counter = 0

        # starting at m in nums1 because from that index the values are 0 and have to be replaced with values from nums2

        for i in range(m, len(nums1)):
            nums1[i] = nums2[counter]
            counter += 1

        # finally sort the nums1 array.
        nums1.sort()


# Running the test cases
test_cases = [
    {
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6],
    },
    {"nums1": [1], "m": 1, "nums2": [], "n": 0, "expected": [1]},
    {"nums1": [0], "m": 0, "nums2": [1], "n": 1, "expected": [1]},
]


obj = Solution()
for test_case in test_cases:
    obj.merge(test_case["nums1"], test_case["m"], test_case["nums2"], test_case["n"])
    if test_case["nums1"] == test_case["expected"]:
        print(True)
    else:
        print("Failed for test case", test_case)
