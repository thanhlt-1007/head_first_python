# cleese = {}
# palin = dict()

# print(type(cleese))
# print(type(palin))

# cleese['Name']= 'John Cleese'
# cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
# palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}

# print(palin['Name'])
# print(cleese['Occupations'][-1])

# palin['Birthplace'] = 'Broomhill, Sheffield, England'
# cleese['Birthplace'] = 'Weston-super-Mare, North Somerset, England'

# print(palin)
# print(cleese)

def sanitize(time_string):
  if '-' in time_string:
    splitter = '-'
  elif ':' in time_string:
    splitter = ':'
  else:
    return(time_string)

  (mins, seconds) = time_string.split(splitter)
  return(mins + '.' + seconds)

def get_coach_data(file_name):
  try:
    with open(file_name) as file:
      file_data = file.readline().strip().split(',')

      data = {}
      data['Name'] = file_data.pop(0)
      data['DOB'] = file_data.pop(0)
      sanitize_data = [sanitize(time_string) for time_string in file_data]
      unique_data = set(sanitize_data)
      fasted_data = sorted(unique_data)[0:3]
      data['Times'] = fasted_data

      return(data)
    return(data.strip().split(','))
  except IOError as io_err:
    print('File error: ' + str(io_err))
    return(None)

sarah = get_coach_data('sarah.txt')
print(str(sarah['Times']))
