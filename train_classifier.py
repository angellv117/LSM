#importacón de librerias
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
#==================== PATH y nombres de los dos modelos a crear =============================#

#nombrepickle = './data2.pickle'
#nombremodelo = 'model2.p'
nombrepickle = './data1.pickle'
nombremodelo = 'model1.p'

#============================================================================================#

#Se abre el archivo.pickle segun el modelo a crear
data_dict = pickle.load(open(nombrepickle, 'rb'))

data = np.asarray(data_dict['data'])
print(data)
labels = np.asarray(data_dict['labels'])
print(labels)

#Creación de el árbol aleatoreo
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly !'.format(score * 100))

#Creación del modelo final
f = open(nombremodelo, 'wb')
pickle.dump({'model': model}, f)
f.close()