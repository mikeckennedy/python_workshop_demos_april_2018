import json

with open('movies.json', 'r', encoding='utf-8') as fin:
    data = json.load(fin)

hits = data.get('hits')
for idx, movie in enumerate(hits, 1):
    if 'comedy' in movie.get('genres'):
        print("{}. {}".format(idx, movie.get('title', 'MISSING')))

data['hits'][0]['title'] = 'The Rundown 2, the revenge!'

with open('movies_edited.json', 'w', encoding='utf-8') as fout:
    data = json.dump(data, fout, indent=True)
