import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok, we will create an ec2 instance for you")
else:
    print("your input is not t2.micro we cannot create an instance for you")
