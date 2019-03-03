from math import sqrt

class commands:
	def test():
		print("This is a test.")


	def pythag(a,b,c):

		if a and b and c:
			print("please input only 2 values")

		elif a and b:
			c = (a**2) + (b**2)
			return sqrt(c)

		elif b and c:
			a = (c**2) - (b**2)
			return sqrt(a)

		elif a and c:
			b = (c**2) - (a**2)
			return sqrt(b)

		elif a or b or c:
			print("please input more than 1 value")

		else:
			print("Error no input")


	def pythagInputHandler():
		while True:
			a = input("a: ")
			if a == "" or a == None:
				a = 0

			elif a == "q" or a == "quit" or a == "exit":
				break

			try:
				a = int(a)

			except:
				print("That is not a number")
				break

			b = input("b: ")
			if b == "" or b == None:
				b = 0

			try:
				b = int(b)

			except:
				print("That is not a number")
				break

			c = input("c: ")
			if c == "" or c == None:
				c = 0

			try:
				c = int(c)

			except:
				print("That is not a number")
				break

			print(commands.pythag(a,b,c))


	def Rsum(Ra,Rb,lod):
		



cmds = {
"test": commands.test,
"pythag": commands.pythagInputHandler,
"": commands.Rsum
}
