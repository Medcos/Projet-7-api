from flask import Flask, jsonify, send_file
import pandas as pd
import mlflow.lightgbm
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shap
import jinja2
import os
import sys


app = Flask(__name__)

## Importer les données
data_path = os.path.join(os.getcwd(), 'kernel', 'info_clients.csv')
#data = pd.read_csv(r".\kernel\info_clients.csv").head(1000)
data = pd.read_csv(data_path).head(1000)

## Page d'accueil
@app.route('/', methods=['GET'])
def hello():
    return " Bienvenue à la société financière, nommée 'Prêt à dépenser'"

print(data)

if __name__ == '__main__':
    app.run()