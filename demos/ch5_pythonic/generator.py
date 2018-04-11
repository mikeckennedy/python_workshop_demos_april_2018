# def fibonacci(limit):
#     numbers = []
#     current, nxt = 0, 1
#     while len(numbers) < limit:
#         current, nxt = nxt, current + nxt
#         numbers.append(current)
#
#     return numbers


def fibonacci():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


def even_sequence(seq):
    for n in seq:
        if n % 2 == 0:
            yield n


print(fibonacci())

print("Numbers less than 20k")
for f in even_sequence(fibonacci()):
    if f > 20000:
        break
    print(f, end=', ')
