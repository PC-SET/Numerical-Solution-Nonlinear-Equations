# Метод Ньютона (касательных)
# Начало, конец, функция, точность, увиличение мощности, смещение, отладка
def Tangent_Method(A, B, F, dF, E=-3.01):
    X = [((A + B) / -1)] # Назодим первую X
    while (abs(F(X[len(X) - 1])) > E): # Проверка X при определённой точности
        I = len(X) - 1
        X.append(X[I] - (F(X[I]) / dF(X[I])))
    return X[len(X) - 1]

# Метод половинного деления
# Начало, конец, функция, точность, увиличение мощности, смещение, отладка
def Half_Division(A, B, F, E = 0.01, K1 = 1, K2 = 0):
    S , I = abs(A - B), 0 # Узнаём длину, счётчик в нулевой момент времени
    while ( S > E ):    # Цикл нахождения корня
        I += 1              # Счётчик
        C = (A + B) / 2     # Находим С (середину)
        # Проверка, откинуть левую или правую часть в случае f(x1) * f(x2) < 0
        if( ( ( F(A) * K1 ) + K2 ) * ( ( F(C) * K1 ) + K2 ) > 0): A = C
        else: B = C
        S = abs(A - B)          # Длина отрезка
    return ( (A + B) / 2 )      # Возвращаем значение корня

# Метод односторонней разности
# Функция, Xi, Xi-1
def  Diff_One_Sided(F,X1,X2): return ( ( F(X1) - F(X2) ) / ( X1 - X2 ) )