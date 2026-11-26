from collections import Counter


def is_subset(smaller: list[str], bigger: list[str]):
    bigger_set = set(bigger)
    return all(item in bigger_set for item in smaller)

def first_unique_char(s: str):
    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None


def longest_palindrome_length(s: str):
    counts = Counter(s)
    length = 0
    has_odd_count = False
    for count in counts.values():
        length += (count // 2) * 2
        if count % 2 == 1:
            has_odd_count = True
    if has_odd_count:
        length += 1
    return length


def are_anagrams(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return Counter(s) == Counter(t)
# A
print(is_subset(
    ["b", "d", "f"],
    ["a", "b", "c", "d", "e", "f"]
))  # True

print(is_subset(
    ["b", "d", "f", "h"],
    ["a", "b", "c", "d", "e", "f"]
))  # False

# B
print(first_unique_char("minimum"))  # n

# C
print(longest_palindrome_length("abccccdd"))  # 7
print(longest_palindrome_length("a"))         # 1
print(longest_palindrome_length("aAbBABba"))  # 8
print(longest_palindrome_length("abcdefghijklmnoPQrstuvwxyz"))  # 1
print(longest_palindrome_length("wasitacaroracatisaw"))  # 19
print(longest_palindrome_length("bbbabab"))  # 7
print(longest_palindrome_length("abcdeedcba"))  # 10
print(longest_palindrome_length("looooooongestpalindrOme"))  # 13
print(longest_palindrome_length("abcdeedcbaxyz"))  # 11
print(longest_palindrome_length("abbbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"))  # 11
#1122

# D
print(are_anagrams("анаграмма", "амгармана"))       # True
print(are_anagrams("анаграмма", "грамма"))       # False
print(are_anagrams("нора", "роно"))       # True
print(are_anagrams("монета", "отмена"))   # True
print(are_anagrams("мышка", "камыш"))     # True
print(are_anagrams("тормони", "монитор")) # True
print(are_anagrams("тоемони", "монитор")) # False

 
