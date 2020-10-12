movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)

cast.remove("Chapman")
print(cast)
case.insert(0, "Chapman")
print(cast)
