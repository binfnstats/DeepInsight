%
% Conversion of DeepInsight TCGA RNA "dataset1" to TSV format
% Reference: https://github.com/binfnstats/PPMI/blob/main/RNA_Step0_Matlab2JSON.m
%

%
% wget https://www.dropbox.com/s/mfwcivoprp3jozx/dataset1.mat?dl=1;
% mv dataset1.mat?dl=1 dataset1.mat
%
% Start Matlab
%
% data = load("dataset1.mat");
% data = jsonencode(data.dset);
% print(data)
% fid = fopen('dataset1.json','w'); # Also available on Dropbox...
% fprintf(fid, data);
% fclose(fid);
%

r = open("/workspace/PPMI/dataset1.json")
data = json.load(r)
In [9]:
Xtrain  = data["Xtrain"] # List of list = matrix
Xtest   = data["Xtest"]
num_tr  = data["num_tr"]
num_tst = data["num_tst"]
class_  = data["class"]

