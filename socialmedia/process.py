import pandas as pd

with open('E:/Usuarios/Daniel/GitHub/SocialMedia-Web-Scraper/socialmedia/itemscopy.csv') as f:
    df = pd.read_csv(f, error_bad_lines= False, delimiter=';')
    df = df.iloc[:,0:7]
    df = df[df.SourceDomain != df.TargetDomain]
    
    #
    #Create nodes dataframe
    nodes = df[['SourceDomain','TargetDomain']]
    weights = nodes.SourceDomain + nodes.TargetDomain
    weights = weights.value_counts()
