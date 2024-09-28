import cases


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

    # I really liked my solution but could not get it to work :(
    def maxProfitByMe(self, prices: list[int]) -> int:
        if len(prices) == 0 or self.checkIfListIsDescending(prices):
            return 0

        max_number = max(prices)
        max_number_index = len(prices) - prices[::-1].index(max_number)

        min_number = min(prices)
        min_number_index = prices.index(min_number)

        if min_number_index < max_number_index:
            return max_number - min_number
        else:
            return max(
                self.maxProfit(prices[:max_number_index]),
                self.maxProfit(prices[max_number_index:]),
            )

    def checkIfListIsDescending(self, prices: list[int]) -> bool:
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                print(prices[i], prices[i + 1])
                return False

        return True


def main() -> None:
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))

    prices = [7, 6, 4, 3, 1]
    print(s.maxProfit(prices))

    prices = cases.prices
    print(s.maxProfit(prices))

    prices = cases.prices2
    print(s.checkIfListIsDescending(prices))
    print(s.checkIfListIsDescending([4, 3, 2, 1]))
    print(s.maxProfit(prices))


if __name__ == "__main__":
    main()
