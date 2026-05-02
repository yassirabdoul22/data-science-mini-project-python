import pandas as pd 



class DataAnalyser:
    
    def __init__(self,df:pd.DataFrame)->None:
        self.df = df

    def describe_statistics(self)->pd.DataFrame:
        return self.df.describe()

    def target_distribution(self)->pd.Series:
        return self.df["target"].value_counts()
    

    def target_percentage(self)->pd.Series:
        # normalize option give ability part/all
        return self.df["target"].value_counts(normalize=True) * 100 
    
    def group_by_target_mean(self):
        return self.df.groupby("target").mean()
    # changement en fonction d un autre col
    def correlation_martrix(self)->pd.DataFrame:
        return self.df.corr()