'''
Даны две строки s и t. Требуется вычислить расстояние Левенштейна между ними — минимальное количество операций вставки,
удаления или замены символа, необходимое для превращения строки s в строку t. 
Операции:
Вставка: добавить один символ в любую позицию строки.
Удаление: удалить один произвольный символ.
Замена: заменить один символ на другой.
Стоимость каждой операции принимается равной 1.
'''
def levenshtein_dp(s1: str, s2: str):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    return dp[m][n]

print(levenshtein_dp("cat", "cut"))      
print(levenshtein_dp("kitten", "sitting")) 
print(levenshtein_dp("hello", "world"))   
print(levenshtein_dp("book", "back"))   
print(levenshtein_dp("", "abc"))         
