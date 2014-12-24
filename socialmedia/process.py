import json
import pandas as pd
data = []
with open('/home/acrocephalus/GitHub/Social-Media-Web-Scraper/socialmedia/scraped_data_utf8.json') as f:
    for line in f: 
        data.append(json.loads(line))
df = pd.DataFrame(data)

#Discard inbound links by comparing the source & target domains
df = df[df["SourceDomain"] != df["TargetDomain"]]

#Drop rows with NA values
df = df.dropna()

#Create files to use with Gephi
#Create nodes dataframe
Nodes = df["SourceDomain"]
Nodes.append(df["TargetDomain"])
Nodes = Nodes.drop_duplicates()
Id = range(1,len(Nodes)+1)
Labels = Nodes
nodesFile = pd.DataFrame(Nodes)
nodesFile[1] = Id
nodesFile[2] = Labels
nodesFile.columns = ["Nodes","Id","Labels"]

#Create edges file
Weights = df["SourceDomain"]+df["TargetDomain"]
Weights = Weights.value_counts()
edgesFile = pd.DataFrame(df["SourceDomain"])
edgesFile[1] = pd.DataFrame(df["TargetDomain"])
edgesFile = edgesFile.drop_duplicates()
Id = range(1,len(Weights)+1)
edgesFile[2] = Id
Type = ["Directed"] * len(Id)
edgesFile[3] = Type
edgesFile[4] = Weights
edgesFile.columns = ['Source','Target','Id','Type','Weights']

print "I have scraped "+ str(nodesFile.shape[0]) + " websites and " + str(len(Weights)) + " links."
