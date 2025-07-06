from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # creating a new variable to store the new array.
        final_nums = []

        for i in nums:
            # if the value in nums equals val, skip it and dont add in final nums
            if i == val:
                continue
            final_nums.append(i)

        # now replace the entire nums array with final_nums.
        # Note: we cannot do nums=final_nums, because that would just change the pointer of nums to now point to final nums, but the original nums array remains unchanged. and the question asks to replace nums in place. so we need to modify the nums original array itself.
        nums[:] = final_nums
        return len(final_nums)


# Running test cases
test_cases = [
    {"nums": [3, 2, 2, 3], "val": 3, "expected_k": 2, "expected_nums_prefix": [2, 2]},
    {
        "nums": [0, 1, 2, 2, 3, 0, 4, 2],
        "val": 2,
        "expected_k": 5,
        "expected_nums_prefix": [0, 1, 3, 0, 4],
    },
    {"nums": [], "val": 1, "expected_k": 0, "expected_nums_prefix": []},
    {"nums": [1, 1, 1], "val": 1, "expected_k": 0, "expected_nums_prefix": []},
    {"nums": [4, 5, 6], "val": 7, "expected_k": 3, "expected_nums_prefix": [4, 5, 6]},
]

solution = Solution()

for idx, case in enumerate(test_cases, 1):
    nums = case["nums"]
    val = case["val"]
    expected_k = case["expected_k"]
    expected_prefix = case["expected_nums_prefix"]

    k = solution.removeElement(nums, val)
    if k != expected_k or nums != expected_prefix:
        print("Failed for test case - ", case)
        print("k received", k)
        print("nums output", nums)
    else:
        print(True)
