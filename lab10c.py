'''
Дан массив неотрицательных целых чисел nums, где nums[i] — сумма денег в i-м доме.
Грабитель не может брать деньги из двух соседних домов (сработает сигнализация).
Нужно найти максимальную сумму, которую можно украсть, не затронув два соседних дома.
'''
def rob_dp(nums: list[int]):
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


print(rob_dp([1, 2, 3, 1]))     
print(rob_dp([2, 7, 9, 3, 1]))     
print(rob_dp([5]))                
print(rob_dp([2, 1, 1, 2]))       
print(rob_dp([0, 0, 0]))         
