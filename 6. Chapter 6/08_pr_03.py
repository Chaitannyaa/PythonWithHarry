# text = input("Enter the text\n")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

# text = input(" Enter the text:\n")

# if ( "make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is Spam")
# else:
#     print("This text is not Spam")

list = ["make a lot of money", "buy now", "click this", "subscribe this"]
spam = False
text = input("Enter the text to check it: ")
for item in list:
    if (item in text):
        spam = True
        break
if spam:
    print("Contains spam inside text")
else:
    print("This text is not Spam")