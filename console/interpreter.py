from Python_Test_Console.console.commands import *

'''
def interpret(cmd):
	if cmd == "test":
		commands.test()
'''
def interpret(cmd):
	cmds[cmd]()
