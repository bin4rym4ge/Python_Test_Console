from console.interpreter import *
cmd = ""

print("****************")
print("* Test Console *")
print("****************")

while True:
	cmd = input("\n~~>")
	if cmd == "":
		break
	interpret(cmd)
