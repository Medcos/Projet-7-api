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

print("Bonjour d'être venu")


if __name__ == '__main__':
    app.run()