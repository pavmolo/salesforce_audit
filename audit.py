import streamlit as st
import pandas as pd


# Ссылка на CSV экспорт таблицы
url = "https://docs.google.com/spreadsheets/d/17Fq2KaMbp_KiQ-RZcEHIMU9bjiFYYYF4jmvez4xnl48/export?format=csv"

# Загрузка данных из Google Таблиц в DataFrame
data = pd.read_csv(url)

# Отображаем данные в Streamlit
st.title('Данные аудита продажников')
st.dataframe(data)

for index, row in data.iterrows():
    st.subheader(row['Вопрос'])
    st.radio(row['Вопрос'], options=[row['Левый'], "Затрудняюсь ответить", row['Правый']], index=1)
