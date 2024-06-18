import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

info_emprestimo = pd.read_csv('emprestimo.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

info_emprestimo.columns = ['Idade', 'Sexo', 'Ocupacao', 'Educacao',
                           'Estado Civil', 'Renda', 'Pontuacao de Crédito', 'Status Emprestimo']

info_emprestimo['Sexo'] = info_emprestimo['Sexo'].replace(
    {'Male': 'Masculino', 'Female': 'Feminino'})
info_emprestimo['Ocupacao'] = info_emprestimo['Ocupacao'].replace({
    'Engineer': 'Engenheiro',
    'Teacher': 'Professor',
    'Student': 'Estudante',
    'Manager': 'Gerente',
    'Accountant': 'Contador',
    'Nurse': 'Enfermeira',
    'Lawyer': 'Advogado',
    'Artist': 'Artista',
    'IT': 'Tecnologia da Informação',
    'Doctor': 'Médico',
    'Consultant': 'Consultor',
    'Analyst': 'Analista',
    'Salesman': 'Vendedor',
    'Marketing': 'Marketing',
    'Architect': 'Arquiteto',
    'Designer': 'Designer',
    'Pharmacist': 'Farmacêutico',
    'Researcher': 'Pesquisador',
    'Professor': 'Professor',
    'Pilot': 'Piloto',
    'Receptionist': 'Recepcionista',
    'Banker': 'Banqueiro',
    'Writer': 'Escritor',
    'Chef': 'Chefe de Cozinha',
    'Veterinarian': 'Veterinário',
    'Sales': 'Vendas',
    'HR': 'Recursos Humanos',
    'Electrician': 'Eletricista',
    'Realtor': 'Corretor de Imóveis',
    'Photographer': 'Fotógrafo',
    'Editor': 'Editor',
    'Programmer': 'Programador',
    'Dentist': 'Dentista',
    'Musician': 'Músico',
    'Psychologist': 'Psicólogo',
    'Server': 'Garçom',
    'Software': 'Desenvolvedor de Software',
    'Stylist': 'Estilista',
    'Doctor': 'Médico'
})
info_emprestimo['Educacao'] = info_emprestimo['Educacao'].replace({
    "Bachelor's": 'Graduação',
    "Master's": 'Mestrado',
    "Doctoral": 'Doutorado',
    "High School": 'Ensino Médio',
    "Associate's": 'Curso Técnico'
})
info_emprestimo['Estado Civil'] = info_emprestimo['Estado Civil'].replace({
    'Married': 'Casado',
    'Single': 'Solteiro'
})
info_emprestimo['Status Emprestimo'] = info_emprestimo['Status Emprestimo'].replace({
    'Approved': 'Aprovado',
    'Denied': 'Negado'
})
info_emprestimo['Renda'] = info_emprestimo['Renda'].map(lambda x: f"{x:.2f}")

plt.figure(figsize=(12, 8))
sns.countplot(data=info_emprestimo, x='Pontuacao de Crédito',
              hue='Status Emprestimo')

# Adiciona título e rótulos aos eixos
plt.title('Distribuição do Status de Empréstimo por Pontuação de Crédito')
plt.xlabel('Pontuação de Crédito')
plt.ylabel('Contagem')


plt.show()

info_emprestimo.to_csv('emprestimo_traduzido.csv', index=False)
