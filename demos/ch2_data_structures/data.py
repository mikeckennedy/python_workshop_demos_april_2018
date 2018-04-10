# List, Dictionary, Set, Tuple

print("---------------- LIST -----------------------")
throws = ['rock', 'paper', 'scissors', 7]

print(f"First item: {   throws[0]  }")
print(f"Second item: {   throws[1]  }")
print(f"Last item: {   throws[-1]  }")

throws[1] = 'PAPER'
throws.append("devil")
throws.append("human")
throws.append("sponge")

print(throws)
print()

print("---------------- DICTIONARY (AKA HASHMAP) -----")

lookup = {
    'jeff@gmail.com': "SOMETHING ABOUT JEFF",
    'sarah@gmail.com': "SOMETHING ABOUT SARAH",
    'joe@aol.com': "SOMETHING ABOUT JOE",
    'mary@aol.com': "SOMETHING ABOUT Mary"
}

if 'mary' in lookup:
    details = lookup['mary']
    print(details)
else:
    print("We don't know mary... who is this?")

details = lookup.get('mary', 'MISSING')
print(details)
details = lookup.get('mary@aol.com', 'MISSING')
print(details)
print()

print("---------------- Sets -----------------")
numbers = {1, 1, 2, 3, 5, 8, 13, 25, 25, 25, -1, 2, 2, 2, 2}
numbers.add(7)
numbers.add(1)
numbers.add(28)
print(numbers)

odd_numbers = set()
even_numbers = set()
for n in range(1, 100):
    if n % 2 == 1:
        odd_numbers.add(n)
    else:
        even_numbers.add(n)

print(odd_numbers)

print("Odd numbers")
print(numbers.intersection(odd_numbers))
print("Even numbers")
print(numbers.intersection(even_numbers))
print()

print("---------------- Tuples -----------------")
measurement = (4, 5, 70.1, .992)
print(f"x={   measurement[0]  }, y={  measurement[1]   }")

x, _, _, quality = measurement
print(x, quality)

x = 1
y = 2
print("Swap values")
temp = y
y = x
x = temp
print(x, y)

y, x = x, y
print(x, y)

print("All throws:")
# count = 0
# for t in throws:
#     count += 1
#     print(f"{count}. {t}")

for idx, t in enumerate(throws, start=1):
    print(f"{idx}. {t}")

# WHY? print(f"The value of the measurement is {measurement[1]}")

import collections

Measurement = collections.namedtuple('Measurement', 'x y value quality')

m = Measurement(x=4, y=5, quality=.992, value=70.1)
# m = Measurement(1, 2, 3, 4)
print(f"The value of the measurement is {m.value}")
print(m)


print("---------------- SLICING ----------------------")
n2 = list(numbers)
print(n2)

print(    n2[2:6]    )

# query = do_db_stuff()
# page3 = query[10*3:10*3+10]
