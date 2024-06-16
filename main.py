import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

info_emprestimo = pd.read_csv('emprestimo.csv')
info_emprestimo.columns = ['Idade', 'Sexo', 'Ocupacao', 'Educacao',
                           'Estado civil', 'Renda', 'Pontuacao de Crédito', 'Status Emprestimo']

print(info_emprestimo)
