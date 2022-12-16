name = input("Enter your name: ")
sid = input("Enter your SID: ")
depart = input("Enter your department: ")
cgpa = input("Enter your CGPA: ")
start = "\033[1m"
end = "\033[0;0m"
print("\nHey, " + start + name + end +  " Here!")
print("My SID is " + start + sid + end)
print("I am from " + start + depart + end + " department and my CGPA is " + start + cgpa + end)
