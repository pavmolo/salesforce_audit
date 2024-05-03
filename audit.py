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
    with st.container(border=True):
        st.subheader(f'{row["Вопрос"]}:')
        default = "Затрудняюсь ответить"
        choise = st.radio(f'{row["Вопрос"]}:', options=[row['Левый'], default, row['Правый']], index=1, label_visibility='hidden')
        numbers = [row['Волк'], row['Работяга'], row['Строитель Отношений'], row['Чемпион'], row['Решатель Проблем']]
        numbers = [2*x for x in numbers]
        inverted_numbers = [-x for x in numbers]
        transformed_numbers = [1 if x == 0 else -1 for x in numbers]
        if choise == row['Левый']:
            option_vector = numbers
        elif choise == row['Правый']:
            option_vector = inverted_numbers
        elif choise == default:
            option_vector = transformed_numbers
        st.write(option_vector)
