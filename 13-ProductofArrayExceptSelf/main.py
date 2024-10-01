class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums_copy = nums.copy()
        has_one_cero = False
        if 0 in nums_copy:
            has_one_cero = True
            # remove 0
            nums_copy.remove(0)
            if 0 in nums_copy:
                return [0] * len(nums)

        cum_product = 1
        for n in nums:
            if n == 0:
                continue
            cum_product *= n

        p = []
        for n in nums:
            if n == 0:
                p.append(cum_product)
            elif has_one_cero:
                p.append(0)
            else:
                # leetcode challenges to not use division so this way it is less efficient at least in python, uncomment following code for more efficient 23:05:22
                # p.append(cum_product/n)
                p.append(self._division(cum_product, n))

        return p

    # I got the implementation from https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
    def _division(self, a: int, b: int) -> int:
        # The sign will be negative only if sign of
        # divisor and dividend are different
        sign = -1 if (a < 0) ^ (b < 0) else 1

        # remove sign of operands
        a = abs(a)
        b = abs(b)

        # Initialize the quotient
        quotient = 0

        # Iterate from most significant bit to
        # least significant bit
        for i in range(31, -1, -1):
            # Check if (divisor << i) <= dividend
            if (b << i) <= a:
                a -= b << i
                quotient |= 1 << i

        return sign * quotient

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        product = []

        for i in range(len(nums)):
            p = 1
            for j, x in enumerate(nums):
                if i != j:
                    p *= x
            product.append(p)

        return product


def main() -> None:
    s = Solution()

    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))

    nums = [-1, 1, 0, -3, 3]
    print(s.productExceptSelf(nums))


if __name__ == "__main__":
    main()
