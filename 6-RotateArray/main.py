class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k if len(nums) > k else k % len(nums)
        new_list = nums[-k:]
        new_list.extend(nums[:-k])

        nums[:] = new_list[:]


def main() -> None:
    s = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [1, 2]
    k = 3

    s.rotate(nums, k)
    s.rotate(nums2, k)

    print(nums)
    print(nums2)


if __name__ == "__main__":
    main()
