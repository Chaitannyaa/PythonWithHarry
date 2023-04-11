# myDict = {
#     "fast": "In a Quick Manner",
#     "harry": "A Coder",
#     "marks": [1, 2, 5],
#     "anotherdict": {'harry': 'Player'},
#     1: 2
# }

# # Dictionary Methods
# print(list(myDict.keys())) # Prints the keys of the dictionary
# print(myDict.values()) # Prints the keys of the dictionary 
# print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
# print(myDict)
# updateDict = {
#     "Lovish": "Friend",
#     "Divya": "Friend",
#     "Shubham": "Friend",
#     "harry": "A Dancer"
# }
# myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
# print(myDict)

# print(myDict.get("harry")) # Prints value associated with key "harry"
# print(myDict["harry"]) # Prints value associated with key "harry"

# # The difference between .get and [] sytax in Dictionaries?
# print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
# print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary

myDict = { "Fast":"In Quick manner",
            "Chaitannyaa" : "An Administrator",
            "Package" : [10,12,19,21],
            "AnotherDict" : { "Chaitannyaa" : "Senior Cloud Admin"} }

print(list(myDict.keys()))
print(myDict.values())
print(myDict.keys())
print(myDict.items())
updatedmyDict={"CG":"Chaitannnyaa Gaikwad",
                1:3}
myDict.update(updatedmyDict)
myDict.update({"Gauranga":"Nityananda"})
print(myDict)
print(myDict.get("Chaitannyaa"))
print(myDict["Chaitannyaa"])

print(myDict.get("Chaitannyaa2"))
# print(myDict["Chaitannyaa2"])
