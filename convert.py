#
# python3 convert.py <Gene Matrix TSV Format> <Output>
#
# DeepInsight image conversion. Only RNA is supported in this release.
# For convention, the first colummn is assumed be the labels.
#

import os
import sys
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from pyDeepInsight import ImageTransformer, LogScaler

#
# Apply DeepInsight neighbour transformation
#

def convert(file, out):
    assert(file is not None)
    assert(out is not None)
    
    df = pd.read_csv(file, sep="\t")
    
    heads = list(df.columns.values)
    assert(not heads[0].isnumeric()) # Make sure the first column is a label and there's header
    
    X = df.iloc[:,1:].values
    Y = df.iloc[:,0].values
    assert(X.shape[0] == Y.shape[0]) # Make sure we have the same number of samples
    
    ln = LogScaler()
    
    s1 = X.shape
    X = ln.fit_transform(X)
    X = ln.transform(X)
    assert(s1 == X.shape)
    
    # Pixel dimension
    dim = 120
        
    it = ImageTransformer(feature_extractor='tsne', pixels=dim, random_state=1701, n_jobs=-1)
    
    print("Training image transformer...")
    it.fit(X, plot=True) # Actual DeepInsight image transformation
    print("Training completed")
    
    # Transform data to image matricies
    X_image = it.transform(X)

    assert(Y.shape[0] == X_image.shape[0])
    os.system("mkdir -p " + out)
        
    with open(out + os.sep + "DeepInsight.tsv", "w") as w:
        for i in range(X_image.shape[0]):
            name = str(i) + ".png"
            path = out + os.sep + name
            w.write(Y[i] + "\t" + path + "\n")
            matplotlib.image.imsave(path, X_image[i])

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
