
# This class contains basic histogram and density plot functions
class distrib_plot:
    def __init__(self,dataframe):
        self.df = dataframe
    def histogram(self):
        self.df.hist(bins=50, figsize=(20,15))
        plt.show()
    def density(self):
        df_numeric = self.df._get_numeric_data()
        for index,row in df_numeric.iteritems():
            sns.kdeplot(df[index])
            plt.show()
