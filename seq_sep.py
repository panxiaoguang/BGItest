def seq_tiqu():
	with open("D:/guangguang/Documents/Q1_reads_of_insert.fa/reads_of_insert.fa") as f:
		fasta={}
		for line in f:
			if line.startswith(">"):
				seqlst=[]
				name=line
				continue
			seqlst.append(line)
			fasta[name]="".join(seqlst)
	return fasta
sm1barcode="GTACACGCTGTGACTA"
rev_sm1barcode="TAGTCACAGCGTGTAC"
sm2barcode="TCTATGTCTCAGTAGT"
rev_sm2barcode="ACTACTGAGACATAGA"

def mismatch(x,y):
	if x==y:
		return x,y
	else:
		for i in range(len(x)):
			if x[i]!=y[i]:
				if x[i+1:]==y[i+1:]:
					return x,y
				else:
					break

def quchong(dct):
	return {x:y for y,x in dct.items()}

def count(dct1,dct2):
	newdct={}
	for key,val in dct1.items():
		count=len([haha for haha in dct2.values() if haha==val])
		newdct[count]=key+val
	return newdct

def sort(dct):
	keylst=[key for key in dct.keys()]
	keylst.sort(reverse=True)
	return keylst

if __name__ == '__main__':
	sample1={}
	sample2={}
	for key,val in seq_tiqu().items():
		if mismatch(val[:16],sm1barcode) or mismatch(val[-16:],sm1barcode) or mismatch(val[:16],rev_sm1barcode) or mismatch(val[-16:],rev_sm1barcode):
			sample1[key]=val
		elif mismatch(val[:16],sm2barcode) or mismatch(val[-16:],sm2barcode) or mismatch(val[:16],rev_sm2barcode) or mismatch(val[-16:],rev_sm2barcode):
			sample2[key]=val
		else:
			continue
with open("D:/guangguang/Documents/Q1_reads_of_insert.fa/sample1.fa",'w') as sam1:
	for key,val in sample1.items():
		sam1.write(key+val)
with open("D:/guangguang/Documents/Q1_reads_of_insert.fa/sample2.fa",'w') as sam2:
	for key,val in sample2.items():
		sam2.write(key+val)


new_sample1=quchong(quchong(sample1))
new_sample2=quchong(quchong(sample2))

with open("D:/guangguang/Documents/Q1_reads_of_insert.fa/sample1.uniq.fa",'w') as u1:
	for shunxu in sort(count(new_sample1,sample1)):
		u1.write(str(shunxu)+"\t"+count(new_sample1,sample1)[shunxu]+"\n")
with open("D:/guangguang/Documents/Q1_reads_of_insert.fa/sample2.uniq.fa",'w') as u2:
	for shunxu2 in sort(count(new_sample2,sample2)):
		u2.write(str(shunxu2)+"\t"+count(new_sample2,sample2)[shunxu2]+"\n")
