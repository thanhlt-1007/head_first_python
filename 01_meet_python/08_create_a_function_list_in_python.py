movies = [
  "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    ["Graham Chapman",
      ["Micheal Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
    ]
]

def print_list(item_list):
  for item in item_list:
    if (isinstance(item, list)):
      print_list(item)
    else:
      print(item)

print_list(movies)
