import pandas as pd

with open('E:/Usuarios/Daniel/GitHub/SocialMedia-Web-Scraper/socialmedia/itemscopy.csv') as f:
    df = pd.read_csv(f, error_bad_lines= False, delimiter=',')
    df = df.iloc[:,0:7]
    df = df[df.SourceDomain != df.TargetDomain]

#-----------------------------------------------        
#Create files suitable to upload to Gephi
#Create nodes dataframe
    Nodes = df['SourceDomain']
    Nodes.append(df['TargetDomain'])
    Nodes = pd.DataFrame(Nodes)
    Nodes = Nodes.drop_duplicates()
    Id = range(1,len(Nodes)+1)
    Nodes[1] = Id
    Nodes[2] = Nodes.SourceDomain
    Nodes.columns = ['Nodes', 'Id', 'Label']
    Nodes.dropna(subset = ['Nodes', 'Label'])
#Create edges dataframe
    
