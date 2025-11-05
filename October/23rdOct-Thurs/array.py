print(
    '''
    ****************
    * Pandas Array *
    ****************
    '''
)
import pandas as pd
mydataset={
    'cars':["BMW", "Toyoto"],
    'passing':[3,5]
}
data=pd.DataFrame(mydataset)
print(data)
