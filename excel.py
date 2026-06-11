import pandas as pd 

def excel(data,filename="output.xlsx"):
     df=pd.DataFrame(data,columns=["english"])
     df.to_excel(filename,index=False)
     
