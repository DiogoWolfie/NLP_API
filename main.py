import numpy as np
import pandas as pd
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

app = FastAPI()

# Carregando o dataset
df = pd.read_csv('manga.csv')

# Inicializando o TfidfVectorizer para transformar os resumos em vetores TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['summary'].fillna('')).toarray()

# Normalizando os vetores para facilitar o cálculo da similaridade
X = normalize(X)

# Definindo o limite de similaridade no código
LIMITE_SIMILARIDADE = 0.1  # Ajuste o valor conforme necessário

class Manga(BaseModel):
    titulo: str
    resumo: str
    similaridade: float

class RespostaModel(BaseModel):
    resultados: List[Manga]
    mensagem: str

def calcular_similaridade(consulta: str):
    # Substituir "?" por espaços para garantir que a consulta seja processada corretamente
    consulta = consulta.replace("?", " ")

    # Transformando a consulta em vetor TF-IDF
    q = vectorizer.transform([consulta]).toarray()

    # Normalizando o vetor da consulta
    q = normalize(q)

    # Calculando a similaridade usando o conceito da imagem (produto escalar e soma dos produtos)
    R = np.dot(X, q.T).flatten()

    # Ordenando os documentos por relevância
    resultados_filtrados = [(df['title'][idx], df['summary'][idx], R[idx]) 
                            for idx in np.argsort(R)[::-1] if R[idx] >= LIMITE_SIMILARIDADE]

    # Limitando a 10 resultados mais relevantes
    resultados = [Manga(titulo=titulo, resumo=resumo, similaridade=similaridade) 
                  for titulo, resumo, similaridade in resultados_filtrados[:10]]

    return resultados

@app.get("/consulta", response_model=RespostaModel)
def obter_recomendacoes(
    query: str = Query(..., description="Tema para buscar mangás relevantes")
):
    try:
        resultados = calcular_similaridade(query)
        if not resultados:
            return {"resultados": [], "mensagem": "Nenhum resultado encontrado com a similaridade mínima especificada"}
        return {"resultados": resultados, "mensagem": "OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API de Recomendação de Mangás"}
