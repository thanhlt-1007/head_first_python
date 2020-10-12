def print_list(item_list, indent=False, level=0):
  for item in item_list:
    if (isinstance(item, list)):
      print_list(item, indent, level + 1)
    else:
      if indent:
        for tab in range(level - 1):
          print("| ", end = "")
        print("|_", end = "")
      print(item)
