import codecs
import json

# 一个一行保存对象
def save(outFile,saveObject): 
	out = codecs.open(outFile, "w", "utf-8")
	for x in saveObject:
		out.write(json.dumps(x))
		out.write("\n")

# 读取保存在一个文件里的对象，一行一个
def load(inFile,saveObject):
	returnObject = []
	inList = open(inFile, "r").readlines()
	i = 0
	for x in saveObject:
		x = json.loads(inList[i])
		i += 1
		returnObject.append(x)
	return returnObject

if __name__ == '__main__':
	test = [[1,2,3,4,5],[4,5,6,7,{"中文":True}]]
	test2 = [[1,2,3],[4,5,6]]
	DIRECTION = ((0,0),(-2,0),(2,0),(0,2),(0,-2))
	save("out.txt",[test,test2,DIRECTION])
	in1 = []
	in2 = []
	[in1,in2] = load("out.txt",[in1,in2])
	print(in1)
	print(in2)