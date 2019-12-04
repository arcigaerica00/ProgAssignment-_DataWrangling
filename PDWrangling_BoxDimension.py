import pandas as pd
A={'Box':['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'], 'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messyA=pd.DataFrame(A,columns=['Box','Dimension','Value'])
tidyA=messyA.pivot_table(index=['Box'],columns='Dimension', values='Value')
tidyAwithVolume= tidyA.assign(Volume=lambda tidyA:tidyA.Length*tidyA.Height*tidyA.Width)
