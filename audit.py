import streamlit as st
import pandas as pd
import altair as alt

url_to_logo = "https://i.ibb.co/cFYfFHq/5-4x.png"

# HTML для центрирования изображения логотипа

# Ссылка на CSV экспорт таблицы
#url = "https://docs.google.com/spreadsheets/d/17Fq2KaMbp_KiQ-RZcEHIMU9bjiFYYYF4jmvez4xnl48/export?format=csv"

# Загрузка данных из Google Таблиц в DataFrame
#data = pd.read_csv(url)

# Определение данных для датафрейма
dat = {
    "Критерии": [
        "Выбирать клиентов/брать любых", "Закрытие сделки/отношения с клиентом", "Новые клиенты/действующие клиенты",
        "Соблюдение стандартов/собственные методы", "Долгосрочные результаты/выполнение плана",
        "Вовлечь клиента в обсуждение проблемы/решить проблему", "Не затронуть неудобную информацию/подробно обсудить с клиентом",
        "Переубеждать клиента/соглашаться с клиентом", "Давить на клиента/быть обходительным", "Выполнение плана/отношения с клиентом",
        "Важно мнение клиента о себе/уверен в себе", "Количество сделок/закрытие сложных сделок",
        "Эмоциональный и межличностный подход/логический, аналитический подход", "Знать о личности клиента/знать о технических подробностях продукта",
        "Интуиция/факты и данные", "Самостоятельность/работа в команде", "Продажа - решение проблемы клиента/продажа - возможность для изменения клиента",
        "Давление на клиента через упущенную выгоду/давление через перспективы", "Новичкам нужно наработать практику, совершить их собственные ошибки, чтобы научиться/новичков, нужно научить, чтобы они совершили меньше ошибок",
        "Вникать в бизнес клиента / топить за срочность"
    ],
    "Вопрос": [
        "Я хотел бы", "В первую очередь я стремлюсь", "Я сначала", "При продажах я обычно",
        "В своей работе я делаю упор на", "Когда в ходе сделки возникает проблема я предпочитаю",
        "В ходе продаж я", "Если видение клиента отличается от нашего я скорее", "В случае сомнений у клиента я скорее",
        "Для меня важнее", "Чтобы оценить свою работу я использую", "Меня больше вдохновляет", "В работе я опираюсь на",
        "В перввую очередь я стараюсь узнать", "Я привык опираться на", "Я предпочитаю работать",
        "Продавая я делаю акцента на", "Если мне нужно надавить на клиента я в первую очередь использую",
        "Чтобы обучить хорошего продавца я", "Чтобы закрыть сделку я стараюсь"
    ],
    "Левый": [
        "Выбирать клиентов из списка", "Закрыть сделку", "Совершу запланированные звонки новым клиентам", "Следую стандартам",
        "Долгосрочных целях", "Представить проблему клиенту и обсудить с ним", "Могу опустить неудобную информацию, чтобы заключить сделку",
        "Постараюсь переубедить клиента", "Надавлю на клиента и закрою сделку", "Выполнение плана продаж",
        "Мнение клиента", "Закрытие большого числа сделок", "Эмоциональный и межличностный подход", "О личности клиента",
        "Интуицию", "Самостоятельно", "Решение проблемы клиента", "Существующие риски, страхи", "Дам ему 'набивать шишки', чтобы он научился на ошибках", "Вникнуть в бизнес клиента"
    ],
    "Правый": [
        "Получать неприрывный поток лидов", "Поддержать теплые отношения с клиентом", "Решу экстренные вопросы действующих клиентов",
        "Использую собственные методы", "Выполнении плана продаж", "Решить проблему, чтобы клиент с ней не столкнулся",
        "Обсуждаю с клиентом все нюансы", "Соглашусь с клиентом", "Сделаю упор на сохранении хороших отношений", "Поддержать теплые отношения с клиентом",
        "Свое собственное понимание", "Закрытие сложных сделок", "Аналитику и логику", "О технических аспектах продукта",
        "Факты и данные", "В команде", "Возможности развить клиента", "Упущенную выгоду, перспективы", "Обучу его, чтобы он совершил меньше ошибок", "Давить на срочность"
    ],
    "Волк": [1, 1, 1, -1, -1, 0, 1, 0, 1, 1, -1, 1, 0, 0, 1, 1, 0, 1, 1, -1],
    "Работяга": [-1, 0, -1, 1, -1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Строитель Отношений": [1, -1, -1, 0, 1, 0, 0, -1, -1, -1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    "Чемпион": [-1, 0, 0, 0, 1, 1, -1, 1, 0, 0, 0, -1, 0, -1, 0, -1, -1, -1, -1, 1],
    "Решатель Проблем": [-1, 0, -1, 1, 0, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, 0, 0, 0]
}

data = pd.DataFrame(dat)

# Отображаем данные в Streamlit

# Инициализация total_vector с нулями
total_vector = [0] * 5  # Предполагаем, что длина каждого option_vector равна 5

with st.sidebar:
    st.markdown(f"<a href='https://taplink.cc/ci_consult'><div style='text-align: center; width: 100%;'><img src='{url_to_logo}' style='width: 100%;'></div></a>", unsafe_allow_html=True)
    st.divider()
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
st.header("Результаты тестирования")
result_dict = dict(zip(keys, total_vector))
description_dict = dict(zip(keys, descriptions))
# Создание DataFrame для визуализации
df = pd.DataFrame({
    'Роли': keys,
    'Значения': total_vector
})
st.divider()
# Создание графика в Altair
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Роли:N', axis=alt.Axis(title='Роли', labelFontSize=18, titleFontSize=18)),  # Увеличен размер шрифта для оси X
    y=alt.Y('Значения:Q', axis=alt.Axis(title='Значения', labelFontSize=14, titleFontSize=18)),  # Увеличен размер шрифта для оси Y
    color=alt.condition(
        alt.datum.Значения > 0,  # Условие для раскраски
        alt.value('green'),  # Зеленый для положительных значений
        alt.value('red')  # Красный для отрицательных значений
    )
).properties(
    width=600,  # Ширина графика
    height=600  # Высота графика
)

# Отображение графика в Streamlit
st.altair_chart(chart, use_container_width=True)




# Определение ключевых и слабых ролей
sorted_roles = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
top_roles = [role for role, value in sorted_roles if value > 0][:2]
weak_roles = [role for role, value in sorted_roles if value < 0][-2:]

# Отображение результатов с цветными заголовками
st.markdown("<h2 style='color: green;'>Самые сильные роли:</h2>", unsafe_allow_html=True)
for role in top_roles:
    with st.expander(f":green[`{role}`]", expanded=False):
        st.write(description_dict[role])

st.markdown("<h2 style='color: red;'>Самые слабые роли:</h2>", unsafe_allow_html=True)
for role in weak_roles:
    with st.expander(f":red[`{role}`]", expanded=False):
        st.write(description_dict[role])
