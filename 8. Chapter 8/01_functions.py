# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
#     return p

# marks1 = [45, 78, 86, 77]
# percentage1 = percent(marks1)

# marks2 = [75, 98, 88, 78]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)

def percent(marks):
    return (sum(marks)/len(marks))

marks1=[56, 55, 90, 91]
p1=percent(marks1)

marks2=(77, 78, 99, 85, 70)
p2=percent(marks2)

print(p1,p2)