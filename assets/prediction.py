import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import csv
import pymysql
import pandas as pd #Python tool for data manipulation and analysis. The two primary data structures are Series and DataFrame
import numpy as np
myConnection = pymysql.connect(host='bk3015.mysql.pythonanywhere-services.com',
                               user='bk3015',
                               passwd='los12345',
                               db='bk3015$los')
cur = myConnection.cursor()
cur.execute("SELECT * FROM patients")
myres = cur.fetchall()
labels = [x[0] for x in cur.description]
patients = pd.DataFrame(list(myres), columns = labels)
patients.to_csv('patients.csv')

data = pd.read_csv('patients.csv', index_col=0, na_values=(" ","  ","   ","    ","     "), low_memory=False)
data.columns = data.columns.str.strip()
# print first 10 rows
#data.shape
data['ins'] = data['INSURANCE']
data['mar'] = data['MARITAL']
data['lang'] = data['LANGUAGE']
data['race'] = data['RACE']
#data.head()
ins_type = data.INSURANCE.unique().tolist()
ins_type = [x for x in ins_type if str(x) != 'nan']
#print(ins_type)

race_type = data.RACE.unique().tolist()
race_type = [x for x in race_type if str(x) != 'nan']
#print(race_type)
lang_type = data.LANGUAGE.unique().tolist()
lang_type = [x for x in lang_type if str(x) != 'nan']
#print(lang_type)
mar_type = data.MARITAL.unique().tolist()
mar_type = [x for x in mar_type if str(x) != 'nan']
#print(mar_type)

new_data = data.copy()

#we are doing this the long way
ins_dict= {}
race_dict = {}
lang_dict = {}
mar_dict = {}
for i in range(len(ins_type)):
    ins_dict[ins_type[i]] = i;
for i in range(len(race_type)):
    race_dict[race_type[i]] = i;
for i in range(len(lang_type)):
    lang_dict[lang_type[i]] = i;
for i in range(len(mar_type)):
    mar_dict[mar_type[i]] = i;

new_data.ins = [ins_dict[item] for item in new_data.ins]
new_data.race = [race_dict[item] for item in new_data.race]
#new_data.lang = [lang_dict[item] for item in new_data.lang]
#new_data.mar = [mar_dict[item] for item in new_data.mar]

for index, row in new_data.iterrows():
    if(str(row['mar']) == 'nan' and str(row['lang']) == 'nan'):
        continue
    elif(str(row['lang']) == 'nan' and  not(str(row['mar']) == 'nan')):
        new_data.at[index, 'mar'] = mar_dict[row['mar']]
        continue
    if(not(str(row['lang']) == 'nan') and str(row['mar']) == 'nan'):
        new_data.at[index, 'lang'] = lang_dict[row['lang']]
        continue
    new_data.at[index, 'mar'] = mar_dict[row['mar']]
    new_data.at[index, 'lang'] = lang_dict[row['lang']]

sub_data = new_data.drop(columns = ['INSURANCE','RACE', 'LANGUAGE', 'MARITAL'])
sub_data.head()

cols = list(sub_data.columns.values)



imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(sub_data)
imp_data = pd.DataFrame(imp.transform(sub_data.values))
#cols = ['EOD10_EX', 'EOD10_PN','EOD10_NE', 'RADIATN', 'GRADE','SEQ_NUM', 'RAC_RECA', 'AGE_DX', 'srv_time_mon', 'alive']
imp_data.columns = cols
#imp_data.head()

to_split =  imp_data
test_data = to_split.iloc[:3000, :]
train_data = to_split.iloc[3000:, :]

X_test  = test_data.iloc[:, 2:]
X_train =  train_data.iloc[:, 2:]

y1_train = train_data.iloc[:, 1:2]# YOUR CODE HERE
y1_test  = test_data.iloc[:, 1:2]# YOUR CODE HERE
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y1_train)
#maital race language insurnace

# Make predictions using the testing set
y1_pred = regr.predict(X_test)


# The coefficients
#print('Coefficients: \n', regr.coef_)
# The mean squared error

# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % r2_score(y1_test, y1_pred))

#Print the intercept and coefficients of the resulting model.
#print (regr.intercept_)
#print (regr.coef_)


#print("Mean squared error: %.2f" % mean_squared_error(y1_test, y1_pred))
#print("root mean squared error: %.2f" % sqrt(mean_squared_error(y1_test, y1_pred)))


enum_list = []
a = ['PATIENT_ID', 'INSURANCE', 'RACE', 'LANGUAGE', 'MARITAL', 'LOS']
counter = 5957
for i in lang_type:
    for j in race_type:
        for m in ins_type:
            for n in mar_type:
                d = dict.fromkeys(a, 0)
                d['PATIENT_ID'] = counter
                d['INSURANCE'] = m
                d['RACE'] = j
                d['LANGUAGE'] = i
                d['MARITAL'] = n
                d['LOS'] = 0
                enum_list.append(d)
                counter+=1
                
mat = []
for i in enum_list:
    
    lst = []
    lst = [None] * 4
    play=list(i.values())
    lst[0] = ins_dict[play[1]] 
    lst[1] = race_dict[play[2]] 
    lst[2] = lang_dict[play[3]]
    lst[3] = mar_dict[play[4]]
    mat.append(lst)

q = regr.predict(np.array(mat))
for i in range(len(enum_list)):
    enum_list[i]['LOS'] = q[i]
    



toCSV = enum_list
keys = a
with open('people.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)


