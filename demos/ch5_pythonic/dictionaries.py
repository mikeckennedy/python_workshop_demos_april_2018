route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

merged = {}
for k, v in query.items():
    merged[k] = v
for k, v in post.items():
    merged[k] = v
for k, v in route.items():
    merged[k] = v

print(merged)

merged = {**query, **post, **route}
print(merged)

all_dicts = [query, post, route]

merged = {}
for d in all_dicts:
    merged.update(d)
print(merged)

