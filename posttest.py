import pandas as pd
import numpy as np
from operator import itemgetter
import nltk

data = np.genfromtxt("textm_wine_reviews.csv", delimiter=',')

data = [
    [(word.replace(",", "")
          .replace(".", "")
          .replace("(", "")
          .replace(")", ""))
    for word in row[2].lower().split()]
    for row in reader]
    










    
  #Removes header
  data = data[1:]
def computeReviewTFDict(review):
    reviewTFDict = {}
    for word in review:
        if word in reviewTFDict:
            reviewTFDict[word] += 1
        else:
            reviewTFDict[word] = 1
    #Computes tf for each word           
    for word in reviewTFDict:
        reviewTFDict[word] = reviewTFDict[word] / len(review)
    return reviewTFDict


