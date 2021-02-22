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
from pyDeepInsight import ImageTransformer, LogScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def convert(file, out):
    assert(data is not None)
    assert(lab is not None)
    assert(out is not None)
    
    df = pd.read_csv(file, sep="\t")
    
    X = df.iloc[:, 1:].values
    Y = df.ix[:,0]

    assert(X.shape[0] == Y.shape[0]) # Make sure we have the same number of samples
    
    ln = LogScaler()
    
    # Second normalization as described by the paper
    X_norm = ln.fit_transform(X)
    
    it = ImageTransformer(feature_extractor='tsne', 
                          pixels=50, random_state=1701, 
                          n_jobs=-1) 
    
    # Convert to images
    X_train_img = it.fit_transform(X_norm)    

    
    #matplotlib.image.imsave('name.png', array)
    #os.system("mkdir -p " + out)

convert(sys.argv[1], sys.argv[2)
