import os
import json

os.chdir('..')
DATA_PATH=os.getcwd()+'/data/'

with open(DATA_PATH+'sentenceWikiTopGrossing.txt', "r") as wiki:
  dataset = json.loads(wiki.read())
  print(dataset)