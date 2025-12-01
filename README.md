# Estudos Aleatórios em Python

Este repositório contém diversos scripts Python para estudos e experimentos com machine learning e análise de dados.

## Scripts

### 1. `run.py` - Previsão com Rede Neural (PyTorch)

Modelo de rede neural usando PyTorch para prever tempo de conclusão baseado em dados de treinamento.

**Características:**

- Implementa uma rede neural com duas camadas lineares
- Usa função de ativação ReLU
- Treina o modelo por 1000 épocas usando otimizador SGD
- Calcula a perda usando MSELoss
- Faz uma previsão final para um valor de entrada

**Dependências:**

- `torch`

**Uso:**

```bash
python run.py
```

**Saída esperada:**

- Progresso do treinamento a cada 100 épocas (mostrando a perda)
- Previsão final do tempo de conclusão para um valor de teste

---

### 2. `prev.py` - Classificação de Solubilidade (scikit-learn)

Modelo de classificação usando LinearSVC para determinar se compostos são solúveis ou insolúveis.

**Características:**

- Usa Support Vector Machine (SVM) linear para classificação
- Treina com 5 exemplos de compostos e suas classificações
- Testa com 3 novos compostos
- Mapeia previsões para rótulos legíveis (Solúvel/Insolúvel)

**Dependências:**

- `scikit-learn`

**Uso:**

```bash
python prev.py
```

**Saída esperada:**

- Previsões do modelo para os compostos de teste
- Classificação de cada composto como "Solúvel" ou "Insolúvel"

---

### 3. `solubility.py` - Classificação de Solubilidade com Métricas

Similar ao `prev.py`, mas inclui cálculo de acurácia do modelo.

**Características:**

- Usa LinearSVC para classificação de solubilidade
- Inclui rótulos de teste para avaliação
- Calcula e exibe a taxa de acurácia do modelo

**Dependências:**

- `scikit-learn`

**Uso:**

```bash
python solubility.py
```

**Saída esperada:**

- Taxa de acerto do modelo em percentual

---

## Dependências

Para instalar todas as dependências necessárias:

```bash
pip install torch scikit-learn
```

Ou use os comandos individuais:

```bash
# Para run.py
pip install torch

# Para prev.py e solubility.py
pip install scikit-learn
```

## Requisitos

- Python 3.6+
- PyTorch (para `run.py`)
- scikit-learn (para `prev.py` e `solubility.py`)
