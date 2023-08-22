import requests 
# import pandas as pd
# import numpy as np

def download_data(url,dataset='data_file.csv'):
   reponse=requests.get(url)
   with open(dataset, 'wb') as file:
      file.write(reponse.content)
      
