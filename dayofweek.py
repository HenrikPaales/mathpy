import math

weekDays = ('Pühapäev', 'Esmaspäev', 'Teisipäev', 'Kolmapäev', 'Neljapäev', 'Reede', 'Laupäev')

def yearDay(x):
    delta = (2+(-1*(2000-x)+math.trunc((-1*(2000-x))/4))) % 7
    return delta


print(weekDays[yearDay(2021)])

    