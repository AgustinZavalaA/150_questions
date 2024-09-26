class Solution:
    def optimizedRemoveDuplicates(self, nums: list[int]) -> int:
        new_list = []

        for v in nums:
            if v not in new_list or new_list.count(v) == 1:
                new_list.append(v)

        nums[:] = new_list[:]
        return len(new_list)


def main():
    s = Solution()

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    unique_numbers2 = s.optimizedRemoveDuplicates(nums2)

    print(nums2, unique_numbers2)


if __name__ == "__main__":
    main()
