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

	except KeyError:
#		print("KeyError")
		print("No such command")

	except:
		print("nope")
