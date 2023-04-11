# letter = '''Dear <|NAME|>,
# Greetings from ABC coding house. I am happy to tell you about your selection
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Bill
# Date: <|DATE|>
# '''
# name = input("Enter Your Name\n")
# date = input("Enter Date\n")
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

# letter='''Dear <|NAME|>,
#             Greetings of the day!
#             We are very pleased to inform you 
#             regarding your interview with us
#             You are selected !!
#             Have a great day ahead
#             Thanks and regards
#             MNC company
#             Suryadev
#             Date : <|DATE|>'''
# name=input("Enter your name:\n")
# date=input("Enter the date:\n")
# letter=letter.replace("<|NAME|>",name)
# letter=letter.replace("<|DATE|>",date)
# print(letter)

class Email:
    company = "MNC"

    def greet(self, name, date):
        self.name = name
        self.date = date
        letter = ('''Dear <|NAME|>,
            Greetings of the day!
            We are very pleased to inform you 
            regarding your interview with us
            You are selected !!
            Have a great day ahead
            Thanks and regards
            MNC company
            Suryadev
            Date : <|DATE|>''')
        letter =letter.replace("<|NAME|>",name)
        letter =letter.replace("<|DATE|>",date)
        print(letter)

hari = Email()
name = input("Enter your name:\n")
date = input("Enter the date:\n")
hari.greet(name, date)
    
