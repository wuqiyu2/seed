from sklearn.ensemble import RandomForestClassifier
import numpy as np
testdomainlist =[]
domainlist = []
class Testdomain:
        def __init__(self,_name, _length,_numbers,_entropy):
                self.name = _name
                self.length = _length
                self.numbers =_numbers
                self.entropy =_entropy




        def returnData(self):
                return [self.length,self.numbers,self.entropy]

class Domain:
	def __init__(self,_name,_label, _length,_numbers,_entropy):
		self.name = _name
		self.label = _label
                self.length = _length
                self.numbers =_numbers
                self.entropy =_entropy

		


	def returnData(self):
		return [self.length,self.numbers,self.entropy]

	def returnLabel(self):
		if self.label == "notdga":
			return 0
		else:
			return 1

def inittestData(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line =="":
                continue
            tokens = line.split(",")
            name = tokens[0]
            length = int (len(tokens[0]))
            int_count=0
            for i in str(tokens[0]):
                if i.isdigit():
                    int_count +=1
            numbers = int(int_count)
            entropy = float(int_count/length)

            testdomainlist.append(Testdomain(name,length,numbers,entropy))


		
def initData(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line.startswith("#") or line =="":
				continue
			tokens = line.split(",")
			name = tokens[0]
                        label =tokens[1]
                        length = int (len(tokens[0]))
                        int_count=0 
                        for i in str(tokens[0]):
                            if i.isdigit():
                                int_count +=1
                          
                        numbers = int(int_count)
                        entropy = float(int_count/length) 
                       

			domainlist.append(Domain(name,label,length,numbers,entropy))

def main():
	initData("train.txt")
        inittestData("test.txt")
	featureMatrix = []
	labelList = []
        
	for item in domainlist:
		featureMatrix.append(item.returnData())
		labelList.append(item.returnLabel())

	clf = RandomForestClassifier(random_state=0)
	clf.fit(featureMatrix,labelList)
        matrix1 = []
        f= open("result.txt","w")    
        hang=0
        h=0
        for item in testdomainlist:
            matrix1.append(item.returnData())
            hang+=1
        
        
        while h<hang+1: 
            print(clf.predict([matrix1[h]]))
            h+=1
        f.close()
    
if __name__ == '__main__':
	main()
