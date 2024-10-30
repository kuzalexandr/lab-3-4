
goods = [
  {'title': 'Ковер', 'price': 2000, 'color': 'green'},
  {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
  assert len(args) > 0
  if len(args) == 1:
    for item in items:
      yield item[args[0]]
  else:
    for item in items:
      yield {arg: item[arg] for arg in args}


for title in field(goods, 'title'):
  print(title, end=", ")

for item in field(goods, 'title', 'price'):
  print(item, end= ", ")