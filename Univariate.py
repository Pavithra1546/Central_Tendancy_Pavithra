class Univariate():
    def quanQual(dataset):
    quan=[]
    qual=[]
    for columnName in dataset.columns:
    #print(columnName)
        if(dataset[columnName].dtypes=='O'):
        #print("qual")
            qual.append(columnName)
        else:
        #print("quan")
             quan.append(columnName)
    return quan,qual
    def freqTable(colunName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["cusum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive
    def outlier_columnName():
        lesser=[]
        greater=[]
        for colunName in quan:
            if(descriptive[colunName]["Min"]<descriptive[colunName]["Lesser"]):
                lesser.append(colunName)
            if(descriptive[colunName]["Max"]>descriptive[colunName]["Greater"]):
                greater.append(colunName)
    def replacing_outliers():
        for columnName in lesser:
             dataset[columnName][dataset[columnName]<descriptive[colunName]["Lesser"]]=descriptive[colunName]["Lesser"]
        for columnName in greater:
             dataset[columnName][dataset[columnName]>descriptive[colunName]["Greater"]]=descriptive[colunName]["Greater"]    