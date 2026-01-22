# Instalação das Dependências

!pip install --upgrade openai pandas
import os
os.environ["OPENAI_API_KEY"] = "SUA_API_KEY_AQUI"
import pandas as pd
from openai import OpenAI

# Extract – Extração dos Dados

# Simulação de uma base de usuários. Neste projeto, a origem é uma lista fixa
# Extrair os dados dos usuários.
    
def extract_users():
    users = [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Bruno"},
        {"id": 3, "name": "Carla"},
        {"id": 4, "name": "Diego"},
        {"id": 5, "name": "Eduarda"}
    ]
    return pd.DataFrame(users)


df_users = extract_users()
df_users

#Transform – Geração de mensagens de marketing bancário personalizadas.

client = OpenAI()

 # Gerar uma mensagem de marketing personalizada usando IA.

def generate_marketing_message(name):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": (
                    f"Crie uma mensagem curta (até 100 caracteres) "
                    f"para {name} sobre a importância dos investimentos."
                )
            }
        ],
        temperature=0.7,
        max_tokens=60
    )
    return response.choices[0].message.content.strip()


# Aplicação da transformação:

def transform_users(df):
    df["marketing_message"] = df["name"].apply(generate_marketing_message)
    return df

df_transformed = transform_users(df_users)
df_transformed

# Load – Carga dos Dados. Salvar dados em CSV.

def load_users(df, file_name="marketing_users_etl.csv"):
    df.to_csv(file_name, index=False, encoding="utf-8")
    print(f"Arquivo '{file_name}' salvo com sucesso!")

load_users(df_transformed)

# Resultado Final

Arquivo gerado: marketing_users_etl.csv

id,name,marketing_message
1,Ana,Investir hoje é o primeiro passo para um futuro financeiro mais seguro.
2,Bruno,Pequenos investimentos agora geram grandes conquistas amanhã.
3,Carla,Investimentos inteligentes ajudam você a realizar seus sonhos.
4,Diego,Planejar investimentos é cuidar do seu futuro financeiro.
5,Eduarda,Seu futuro agradece cada decisão consciente de investimento.
