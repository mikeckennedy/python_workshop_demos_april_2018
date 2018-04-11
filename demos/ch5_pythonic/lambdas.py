def even_numbers(nums, predicate):
    selected = []
    for n in nums:
        if predicate(n):
            selected.append(n)

    return selected


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


print(even_numbers([1, 1, 2, 8, 10, 9, 100, 5], is_even))
print(even_numbers([1, 1, 2, 8, 10, 9, 100, 5], lambda n: n % 3 == 0))


nums = [1, 1, 2, 8, 10, 9, 100, 5, -1, -7, -100]

nums.sort(key=lambda m: abs(m), reverse=True)
print(nums)
