print("This program will tell you if a triangle is possible with given lengths.")
s1 = input("Enter the length of first side: ")
s2 = input("Enter the length of second side: ")
s3 = input("Enter the length of third side: ")
if ((s1 + s2) < s3) and ((s2 + s3) < s1) and ((s3 + s1) < s2) :
    print("triangle cannot be formed")
else:
    print("triangle can be formed")
