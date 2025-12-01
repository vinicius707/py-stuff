from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

composto1 = [1,1,1]
composto2 = [1,0,0]
composto3 = [0,1,1]
composto4 = [0,1,0]
composto5 = [0,0,1]

dados_treino = [composto1, composto2, composto3, composto4, composto5]
rotulos_treino = ['S','N','S','S','N']

modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

teste1 = [1,1,0]
teste2 = [1,0,1]
teste3 = [0,0,0]


dados_teste = [teste1, teste2, teste3]
rotulos_teste = ['S','N','N']

previsoes = modelo.predict(dados_teste)

acuracia = accuracy_score(rotulos_teste, previsoes)

print("Taxa de acerto: %.2f%%" % (acuracia * 100))