# myDict = {
#     "Pankha": "Fan",
#     "Dabba": "Box",
#     "Vastu": "Item"
# }
# print("Options are ", myDict.keys())
# a = input("Enter the Hindi Word\n")
# # print("The meaning of your word is:", myDict[a])

# # Below line will not throw an error if the key is not present in the dictionary
# print("The meaning of your word is:", myDict.get(a))

myDict = { "Surya":"SUN", "Chandra":"Moon", "Guru":"Jupiter"}

print("Options are : ", list(myDict.keys()))
a = input("Enter your Marathi Word :\n")
print("The Meaning of your word in English is : ", myDict.get(a))
