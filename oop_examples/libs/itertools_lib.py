from itertools import combinations, combinations_with_replacement, count
# docs https://docs.python.org/3/library/itertools.html?highlight=itertools

nums = list(range(10))

print(nums)
print(list(combinations(nums, 3)))

print(list(combinations_with_replacement(nums, 2)))

odds = count(start=1, step=2)
print(list(next(odds) for _ in range(10))) # первые 10 нечетных цифр

