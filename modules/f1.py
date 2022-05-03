print("__name__:",__name__)
print("f1 started")
def fun():
	print("this is fun in f1")
if __name__ == "__main__":
	def fun1():
		print("this is fun1 in f1")
	fun1()
x=1000
print("f1 ended")