#Importation du fichier
import pandas as pd


def loadData(url='donnees_immobiliers.csv'):
    df=pd.read_csv(url)
    return df




