import pandas as pd
A={'Student':['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}

B={'Student':['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}

C={'Student':['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,93]}

D={'Student':['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}

Math=pd.DataFrame(A, columns=['Student', 'Math'])

Electronics=pd.DataFrame(B, columns=['Student', 'Electronics'])

GEAS=pd.DataFrame(C, columns=['Student', 'GEAS'])

ESAT=pd.DataFrame(D, columns=['Student', 'ESAT'])

MBare=pd.merge(Math,Electronics, how='left', on='Student')

MBear=pd.merge(GEAS,ESAT, how='left', on='Student')

MBareBears=pd.merge(MBare,MBear, how='left', on='Student')

x=pd.melt(MBareBears, id_vars='Student', value_vars=['Math','Electronics','GEAS','ESAT'])

y=x.rename(columns={'variable':'Subjects','value':'Grades'})

z=y.sort_values('Student')

Z=z.reset_index()

LongFormatBear=Z.drop(columns=['index'])