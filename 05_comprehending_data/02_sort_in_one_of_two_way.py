def get_data_from_file(file_name):
  with open(file_name) as file:
    data = file.readline().strip().split(',')
  return data

james_data = get_data_from_file('james.txt')
print('james_data: ', sorted(james_data))

julie_data = get_data_from_file('julie.txt')
print('julie_data: ', sorted(julie_data))

mikey_data = get_data_from_file('mikey.txt')
print('mikey_data: ', sorted(mikey_data))

sarah_data = get_data_from_file('sarah.txt')
print('sarah_data: ', sorted(sarah_data))
