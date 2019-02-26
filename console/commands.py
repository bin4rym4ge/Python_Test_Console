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


cmds = {
"test": commands.test,
"pythag": commands.pythag
}
