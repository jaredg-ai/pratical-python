#in python, to make a list you simply use the []

names = ["Jared", "Alex"]
#in the list, "Jared" is equal to "0" and "Alex" is equal to "1" in the index.
names.append("Indy")
#this will add the name Indy to the list.
names.remove("Alex")
#the remove will remove that name form the list.
del names[1]
#this will also remove the name "Alex" but by the index.
print(names)
#you can do this if you want to see if something already exists in a list.
if 1 in [1, 2, 3, 4, 5]:
    print("True")

#for a word you need to give it a variable.
word = "Jared"

if word in names:
    print(word + " is in the list")
else:
    print(word + " is not in the list")