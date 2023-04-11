def inches(centm):
    return centm / 2.54

centm = int(input("Enter the length in centimeter : "))
print(f"The value of {centm} in inches is {inches(centm)}")