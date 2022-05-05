# import pandas as pd
# import numpy as np
# dataframe = pd.read_excel("German_Credit.xlsx")
# x = dataframe["CreditAmount"]
# y = dataframe["DurationOfCreditInMonths"]
# for i in range(len(x)):
#     print("{0}\t{1}".format(x[i],y[i]))

# import pandas as pd
# import numpy as np
# dataframe = pd.read_csv("heart_disease_data.csv")
# x = dataframe["age"]
# y = dataframe["target"]
# for i in range(len(x)):
#     print("{0}\t{1}".format(x[i],y[i]))

import pandas as pd
import numpy as np
dataframe = pd.read_csv("covid_19_data.csv")
x = dataframe["Last Update"]
y = dataframe["Deaths"]
for i in range(len(x)):
    print("{0}\t{1}".format(x[i],y[i]))