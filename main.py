from interpreter import *

cmd = ""

print("****************")
print("* Test Console *")
print("****************")

while True:
	try:
		cmd = input("\n~~>")
		if cmd == "quit":
			break
		interpret(cmd)
	except:
		print("error")
