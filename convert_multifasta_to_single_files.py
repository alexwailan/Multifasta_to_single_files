
inputData = []
with open("./incFIIK_human_global_kp_multifasta.fa", "r") as data:
	for line in data:
		fastaLine= line.strip().split("\n")
		print(fastaLine)
		inputData.append(fastaLine)