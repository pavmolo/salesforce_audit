import streamlit as st
import pandas as pd

# Ссылка на CSV экспорт таблицы
url = "https://docs.google.com/spreadsheets/d/17Fq2KaMbp_KiQ-RZcEHIMU9bjiFYYYF4jmvez4xnl48/export?format=csv"

# Загрузка данных из Google Таблиц в DataFrame
data = pd.read_csv(url)

# Отображаем данные в Streamlit

# Инициализация total_vector с нулями
total_vector = [0] * 5  # Предполагаем, что длина каждого option_vector равна 5

with st.sidebar:
    for index, row in data.iterrows():
        with st.container():
            st.subheader(f'{row["Вопрос"]}:')
            default = "Затрудняюсь ответить"
            choice = st.radio(f'{row["Вопрос"]}:', options=[row['Левый'], default, row['Правый']], index=1, label_visibility='hidden')
            numbers = [row['Волк'], row['Работяга'], row['Строитель Отношений'], row['Чемпион'], row['Решатель Проблем']]
            numbers = [2*x for x in numbers]
            inverted_numbers = [-x for x in numbers]
            transformed_numbers = [1 if x == 0 else -1 for x in numbers]
            
            if choice == row['Левый']:
                option_vector = numbers
            elif choice == row['Правый']:
                option_vector = inverted_numbers
            elif choice == default:
                option_vector = transformed_numbers
            
            # Суммирование option_vector с total_vector поэлементно
            total_vector = [sum(x) for x in zip(total_vector, option_vector)]
            st.divider()

# Отображаем итоговый total_vector в Streamlit
keys = ['Волк', 'Работяга', 'Строитель Отношений', 'Чемпион', 'Решатель Проблем']
result_dict = dict(zip(keys, total_vector))
st.bar_chart(result_dict, height = 800)
