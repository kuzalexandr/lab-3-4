class Unique(object):
  def __init__(self, items, **kwargs):
    self.items = iter(items)
    self.seen = set()
    self.ignore_case = kwargs.get('ignore_case', False)

  def __next__(self):
    while True:
      try:
        item = next(self.items)
        if self.ignore_case:
          item = item.lower()
        if item not in self.seen:
          self.seen.add(item)
          return item
      except StopIteration:
        raise StopIteration

  def __iter__(self):
    return self