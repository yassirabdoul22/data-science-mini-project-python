import pandas as pd




class DataCleaner:
    def __init__(self,df:pd.DataFrame)->None:
        self.df = df.copy()


    def missing_values_report(self)->pd.Series:
        return self.df.isnull().sum()

    def duplicated_rows_count(self)->int:
        return self.df.duplicated.sum()

    def remove_duplicates(self)->"DataCleaner":
        self.df = self.df.drop_duplicates(keep="first")
        self.df = self.df.reset_index(drop=True)
        #return self to directly acce to instance to save the result in cvs file
        return self
    
    def data_type_report(self)->pd.Series:
        return self.df.dtypes

    def save_clean_data(self,output_file:str)->None:
        self.df.to_csv(output_file,index=False)

    def get_clean_data(self)->pd.DataFrame:
        return self.df
    
