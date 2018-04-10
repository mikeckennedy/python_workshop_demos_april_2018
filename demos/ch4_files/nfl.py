import csv
from collections import defaultdict

with open('nfl.csv', 'r', encoding='utf-8') as fin:
    reader = csv.DictReader(fin)

    # counts = defaultdict(list)
    # for r in reader:
    #     team = r.get('team')
    #     player = r.get('name')
    #     counts[team].append(player)
    counts = dict()
    straight_teams = []
    for r in reader:
        team = r.get('team')
        straight_teams.append(team)
        player = r.get('name')

        if team not in counts:
            counts[team] = []

        counts[team].append(player)

# for k, v in counts.items():
#     print("Team: {}, Offenders: {}".format(k, v))


offenders = list(counts.items())
offenders.sort(key=lambda t: len(t[1]), reverse=True)
# print(offenders)
for o in offenders:
    print(f"{o[0]} with {len(o[1])} offenses.")


from collections import Counter
results = Counter(straight_teams)
print(results)

