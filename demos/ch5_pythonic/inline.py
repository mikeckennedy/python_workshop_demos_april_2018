numbers = [1, 2, 5, 7, 89, 90, 10, 20]

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n * n)

# list comprehension
evens = [
    n * n  # add value
    for n in numbers  # set to draw from
    if n % 2 == 0  # test for inclusion
]

print(evens)


results = [
    (1, 2, 70.1),
    (2, 2, 80.0),
    (4, 2, 20.0),
    (-4, 5, 100.0),
]

make_square = lambda n : n * n
# m = max(make_square(r[2]) for r in results)
m = max(r[2] for r in results)
print(m)


# Generator expression
evens = (
    n * n  # add value
    for n in numbers  # set to draw from
    if n % 2 == 0  # test for inclusion
)

for n in evens:
    print(n)



