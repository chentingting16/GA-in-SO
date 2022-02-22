# importing the required libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import xlrd
import math

# Setting up the Data Frame
test_data=pd.read_csv('C:/Users/ChenTingting/Desktop/figure_expert.csv')
ga = []
database = []
ml = []
mobile = []
service = []
web = []
for i in test_data.values:
    if i[1] > 0:
        d = math.log(i[1], 2)

        if i[0] == 'ga':
            ga.append(d)
        if i[0] == 'ml':
            ml.append(d)
        if i[0] == 'database':
            database.append(d)
        if i[0] == 'mobile':
            mobile.append(d)
        if i[0] == 'web':
            web.append(d)
        if i[0] == 'service':
            service.append(d)





# Plotting the KDE Plot
#blue
sns.kdeplot(ga,shade=True, label="GA",color='purple')
sns.kdeplot(database, shade=True, label="Database", color = 'orange')
sns.kdeplot(ml, shade=True, label="Machine Learning",color='black')
sns.kdeplot(mobile, shade=True, label="Mobile Development", color ='green')
sns.kdeplot(service, shade=True, label="Service", color = 'blue')
sns.kdeplot(web, shade=True, label="Web Development", color = 'PINK')

# Setting the X and Y Label
plt.xlabel('Log10(ExpertiseValue)')
plt.ylabel('Density')
plt.show()

"""
# Setting up the Data Frame
test_data=pd.read_csv('C:/Users/ctt/Downloads/expert_comparison_web_ml_docker_general.csv')



# Plotting the KDE Plot
sns.kdeplot(test_data.LogValueWeb.tolist(),shade=True, label="Web Development")
sns.kdeplot(test_data.LogValueDocker.tolist(), shade=True, label="Docker")
sns.kdeplot(test_data.LogValueML.tolist(), shade=True, label="Machine Learning")
sns.kdeplot(test_data.ExpetiseValueGeneral.tolist(), shade=True, label="Baseline Sample")

# Setting the X and Y Label
plt.xlabel('Log(ExpertiseValue)')
plt.ylabel(' Density')
plt.show()
"""