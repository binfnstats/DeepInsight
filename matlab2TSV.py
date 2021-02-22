#
# Conversion of DeepInsight TCGA RNA "dataset1" to TSV format
# Reference: https://github.com/binfnstats/PPMI/blob/main/RNA_Step0_Matlab2JSON.m
#

#
# wget https://www.dropbox.com/s/mfwcivoprp3jozx/dataset1.mat?dl=1;
# mv dataset1.mat?dl=1 dataset1.mat
#
# Start Matlab
#
# data = load("dataset1.mat");
# data = jsonencode(data.dset);
# print(data)
# fid = fopen('dataset1.json','w'); # Also available on Dropbox... Easier to work in Python.
# fprintf(fid, data);
# fclose(fid);
#

r = open("/workspace/PPMI/dataset1.json")
data = json.load(r)
In [9]:
Xtrain  = data["Xtrain"] # List of list = matrix
Xtest   = data["Xtest"]
num_tr  = data["num_tr"]
num_tst = data["num_tst"]
class_  = data["class"]

print(len(Xtrain))    # 60483 (genes)
print(len(Xtrain[2])) # 5594 (samples)

# Convert list of list to numpy format
#

X = numpy.zeros(shape=(len(Xtrain), len(Xtrain[2])))
for i in range(len(Xtrain)): # For each gene...
    for j in range(len(Xtrain[2])): # For each sample..
        X[i,j] = Xtrain[i][j]
        
print(X.shape) # Gene matrix is always in gene*samples format
print(X)

print(num_tr) # [1091, 453, 491, 543, 476, 518, 494, 496, 511, 521]


Y = numpy.zeros(shape=(1, len(Xtrain[2])))
n = 0
for i in range(len(num_tr)):
    for j in range(num_tr[i]):
        Y[0,n] = i
        n += 1
print(Y.shape) # (1, 5594)
Y


numpy.savetxt("/workspace/PPMI/DeepInsight_GeneMatrix.tsv", X, delimiter="\t")
numpy.savetxt("/workspace/PPMI/DeepInsight_GeneMatrix_Meta.tsv", Y, delimiter="\t")
