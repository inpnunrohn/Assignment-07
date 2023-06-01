# .............................
# Title : Pickling Data and Exception Handling
# Dev : Rohini N
# Date : 1st June,2023
# Changelog : (Who When What)
# Rohini N, 1st June,2023,Created Script
# .............................

# pickling an object
pickling = open("debuts.dat", "wb")  # open a binary file for writing
pickle.dump(debutAlbums, pickling)  # serialization i.e. pickling
# print(type(pickling))
pickling.close()  # close the file

# unpickling an object
unpickling = open("debuts.dat", "rb")  # open binary file for reading
debutAlbumsUP = pickle.load(unpickling)  # de-serialization i.e. unpickling
unpickling.close()  # close the file
#import pickle

debutAlbums = [{'band': 'Led Zeppelin', 'debut': 'Led Zeppelin'},
               {'band': 'U2', 'debut': 'Boy'}]

# pickling an object
with open("debuts.dat", "wb") as file:
    pickle.dump(debutAlbums, file)

# unpickling an object
with open("debuts.dat", "rb") as file:
    debutAlbumsUP = pickle.load(file)

print(debutAlbumsUP)
print(type(debutAlbumsUP))

try:
    strData = input("Give me a number: ")

    if not strData.isnumeric():
        raise ValueError('Give me a number, please.')

    intData = int(strData)

except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"There was an error: {e}")
else:
    print(f"The number you entered is {intData}")