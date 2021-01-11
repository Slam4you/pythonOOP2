# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"


s, t = (input() for _ in range(2))
cur = 0
count = 0
while cur < len (s):
    if s[cur] == t[0] and s[cur: cur + len(t)] == t:
        count += 1
    cur += 1
print(count)