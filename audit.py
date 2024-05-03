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
descriptions = [
    "Одинокие волки полагаются на свои инстинкты и часто игнорируют правила и стандарты. Они чрезвычайно самостоятельны и часто действуют вопреки установленным процессам, что может создавать проблемы для управления.",
    "Трудяги всегда готовы приложить дополнительные усилия, они первыми приходят на работу и последними уходят. Эти продавцы не устают искать способы улучшить свои навыки и производительность, активно ищут обратную связь и готовы учиться.",
    "Строители отношений сосредотачиваются на создании сильных связей с клиентами и готовы на всё, чтобы удовлетворить их потребности. Они искренне заботятся о клиентах и ставят их интересы на первое место, даже если это идет в ущерб продажам.",
    "Челленджеры используют своё глубокое понимание бизнеса клиента, чтобы изменить их мышление, обучая их новым подходам к решению проблем. Они не боятся высказывать своё мнение, даже если оно противоречиво, и активно воздействуют на клиента, в том числе и в вопросах ценообразования.",
    "Реактивные решатели проблем фокусируются на обеспечении выполнения обещаний, данных клиентам в процессе продаж. Они внимательны к деталям и стремятся убедиться, что послепродажное обслуживание и реализация услуг проходят гладко."
]

result_dict = dict(zip(keys, total_vector))
description_dict = dict(zip(keys, descriptions))
st.bar_chart(result_dict, height = 600)
# Определение ключевых и слабых ролей
sorted_roles = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
top_roles = [role for role, value in sorted_roles if value > 0][:2]
weak_roles = [role for role, value in sorted_roles if value < 0][-2:]

# Отображение результатов с цветными заголовками
st.markdown("<h2 style='color: green;'>Самые сильные роли:</h2>", unsafe_allow_html=True)
for role in top_roles:
    with st.expander(role):
        st.write(description_dict[role])

st.markdown("<h2 style='color: red;'>Самые слабые роли:</h2>", unsafe_allow_html=True)
for role in weak_roles:
    with st.expander(role):
        st.write(description_dict[role])
