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

class Manga(BaseModel):
    titulo: str
    resumo: str
    similaridade: float

class RespostaModel(BaseModel):
    resultados: List[Manga]
    mensagem: str

def calcular_similaridade(consulta: str, limite_relevancia: float):
    # Substituir "?" por espaços para garantir que a consulta seja processada corretamente
    consulta = consulta.replace("?", " ")

    # Transformando a consulta em vetor TF-IDF
    q = vectorizer.transform([consulta]).toarray()

    # Normalizando o vetor da consulta
    q = normalize(q)

    # Calculando a similaridade usando o conceito da imagem (produto escalar e soma dos produtos)
    R = np.dot(X, q.T).flatten()

    # Filtrando documentos pela relevância mínima e ordenando por relevância
    resultados_filtrados = [(df['title'][idx], df['summary'][idx], R[idx]) 
                            for idx in np.argsort(R)[::-1] if R[idx] >= limite_relevancia]

    # Limitando a 10 resultados mais relevantes
    resultados = [Manga(titulo=titulo, resumo=resumo, similaridade=similaridade) 
                  for titulo, resumo, similaridade in resultados_filtrados[:10]]

    return resultados

@app.get("/consulta", response_model=RespostaModel)
def obter_recomendacoes(
    query: str = Query(..., description="Tema para buscar mangás relevantes"),
    limite_relevancia: float = Query(0.0, description="Relevância mínima dos resultados")
):
    try:
        resultados = calcular_similaridade(query, limite_relevancia)
        if not resultados:
            return {"resultados": [], "mensagem": "Nenhum resultado encontrado com a relevância mínima especificada"}
        return {"resultados": resultados, "mensagem": "OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API de Recomendação de Mangás"}
