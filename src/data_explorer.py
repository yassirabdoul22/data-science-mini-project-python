import pandas as pd


class DataExplorer:
    def __init__(self,df:pd.DataFrame)->None:
        self.df = df

    # Get n first line (default 5)
    def show_head(self,n:int = 5)->pd.DataFrame:
        return self.df.head(n)

    # Get n last lines (default 5)
    def show_tail(self,n:int = 5)->pd.DataFrame:
        return self.df.tail(n)

    # Get columns
    def show_columns(self)->list:
        return list(self.df.columns)
    
    # Get missing values
    def missing_values(self)->pd.Series:
        return self.df.isnull().sum()

    # Get shape of DataFrame
    def show_shape(self)->tuple:
        return self.df.shape
    # Get duplicated rows
    def duplicated_rows(self)->int:
        return self.df.duplicated().sum()

    # Get statistics
    def descriptive_statistics(self)->pd.DataFrame:
        return self.df.describe(include = "all")

    # Diplay all infos (overview)
    def overview(self)->None:
        print("DataSet shape:",self.show_shape())
        print("\n Columns:")
        for c in self.show_columns():
            print("-",c)

        print("missing Values")
        print(self.missing_values())

        print("Duplicated rows:",self.duplicated_rows())