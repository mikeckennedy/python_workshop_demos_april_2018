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


print("---------------- DICTIONARY (AKA HASHMAP) -----")


