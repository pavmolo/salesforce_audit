import streamlit as st
import pandas as pd

# Функция для загрузки данных из Excel
def load_data():
    url = "https://github.com/pavmolo/salesforce_audit/blob/main/autit_table.xlsx?raw=true"
    df = pd.read_excel(url, sheet_name='Лист1')
    return df

# Загружаем данные
data = load_data()

# Отображаем данные в Streamlit
st.title('Данные аудита продажников')
st.dataframe(data)

for index, row in data.iterrows():
    row['Вопрос']
