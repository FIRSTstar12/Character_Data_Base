errorMessage = "There is a problem with your search. Please try again"
instructions = "This is the Marvel Data Base. It contains characters, locations, powers, comic information, movie information,and objects"
writer = ""
artist = ""
firstAppearance = ""
connections = [""]
powers = [""]
names  = [""]
searchableItems = []
userSearch = input("")
if userSearch not in searchableItems:
  print(errorMessage)