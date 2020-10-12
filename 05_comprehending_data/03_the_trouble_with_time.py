def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return time_string

  (mins, seconds) = time_string.split(splitter)
  return mins + '.' + seconds

def get_data_from_file(file_name):
  with open(file_name) as file:
    data = file.readline().strip().split(',')
  return [sanitize(time_string) for time_string in data]

james_data = get_data_from_file('james.txt')
print('james_data: ', sorted(james_data))

julie_data = get_data_from_file('julie.txt')
print('julie_data: ', sorted(julie_data))

mikey_data = get_data_from_file('mikey.txt')
print('mikey_data: ', sorted(mikey_data))

sarah_data = get_data_from_file('sarah.txt')
print('sarah_data: ', sorted(sarah_data))
