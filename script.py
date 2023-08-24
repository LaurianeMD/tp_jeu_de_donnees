import requests 
import pandas as pd
# import numpy as np

def download_data(url,dataset='data_file.csv'):
   reponse=requests.get(url)
   with open(dataset, 'wb') as file:
    file.write(reponse.content)
      
# def check_data_quality(dataset):
#    df=pd.read_csv(dataset)
#    numeric_values=df.select_dtypes(include=['int64','float64']).columns
#    categoric_values=df.select_dtypes(include=['object']).columns
#    #Enlever  les doublons
#    df.drop_duplicates(inplace=True)

#    #Traitement des valeurs manquantes
#    df.isna().sum()
   
   