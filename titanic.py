import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('titanic.parquet') #Чтение файла titanic.parquet

df.to_csv('titanic.parquet', index=False) #сохранение данный DataFrame в csv и убираем индексы 

df_csv = pd.read_csv('titanic.parquet') #читаем csv файл

quantity_passengers = df_csv.groupby('Pclass').size() #Мы группируем DataFrame по столбцу Pclass пассажира.size(): Эта функция возвращает количество элементов в каждой группе.
survived = df_csv[df_csv['Survived'] == 1].groupby('Pclass').size() / quantity_passengers * 100#(пассажиры, которые выжили),процент выживших
not_survived = df_csv[df_csv['Survived'] == 0].groupby('Pclass').size() / quantity_passengers * 100#(пассажиры, которые не выжили),процент не выживших

survival_data = pd.DataFrame({
    'Выжившие': survived,
    'Не выжившие': not_survived
})

# Построение гистограммы
ax = survival_data.plot(kind='bar', stacked=True, color=['green', 'red'])#kind - тип графика bar - столбчатая диаграмма
                                                                        #stacked - столбцы будут накладываться друг на друга
ax.set_xlabel('Класс билета') #название оси X
ax.set_ylabel('Доля пассажиров (%)') #название оси Y
ax.set_title('Выживаемость пассажиров в зависимости от класса билета') #заголовок для графика
ax.legend(title='Статус')
plt.show()