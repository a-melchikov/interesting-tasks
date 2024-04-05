# Функция для окружения матрицы нулями
def surround_with_zeros(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Рассчитываем новые размеры матрицы с окружением нулями
    new_rows = rows + 2
    new_cols = cols + 2

    # Создаем новую матрицу с нулями
    new_matrix = [[0] * new_cols for _ in range(new_rows)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[i + 1][j + 1] = matrix[i][j]

    return new_matrix


# Функция для нахождения максимального прямоугольника
def find_max_rectangle(matrix):
    if not matrix:
        return (-1, -1, -1, -1)

    rows = len(matrix)
    cols = len(matrix[0])

    # Инициализация переменных для максимального прямоугольника
    max_area = 0
    max_rect = (-1, -1, -1, -1)

    # Функция для вычисления площади прямоугольника
    def area(rect):
        return rect[2] * rect[3]

    # Функция для проверки окруженности прямоугольника
    def is_surrounded(rect):
        top, left, height, width = rect
        return (
            not any(matrix[top - 1][left - 1 : left + width + 1])
            and not any(matrix[top + height][left - 1 : left + width + 1])
            and not any([i[left - 1] for i in matrix[top : top + height]])
            and not any([i[left + width] for i in matrix[top : top + height]])
        )

    # Перебираем все элементы матрицы
    for i in range(rows):
        for j in range(cols):
            # Если текущий элемент истинный, начинаем поиск прямоугольника
            if matrix[i][j]:
                height = 1
                for k in range(i + 1, rows):
                    if matrix[k][j]:
                        height += 1
                    else:
                        break
                width = 1
                for k in range(j + 1, cols):
                    if matrix[i][k]:
                        width += 1
                    else:
                        break

                # Вычисляем площадь текущего прямоугольника
                curr_area = area((i, j, height, width))

                # Проверяем, является ли текущий прямоугольник максимальным и окруженным
                if curr_area > max_area and is_surrounded((i, j, height, width)):
                    max_area = curr_area
                    max_rect = (i, j, height, width)

    return max_rect


# Функция для чтения матрицы из ввода пользователя
def read_matrix():
    matrix = []
    print("Введите матрицу (для окончания ввода введите пустую строку):")
    while True:
        row = input().strip()
        if not row:
            break
        matrix.append([c == "1" for c in row])
    return matrix


matrix = surround_with_zeros(read_matrix())
result = find_max_rectangle(matrix)

# Вывод результата
if result == (-1, -1, -1, -1):
    print("Прямоугольник не найден.")
else:
    print(
        f"Координаты: {result[0] - 1}, {result[1] - 1}; высота {result[2]}; ширина {result[3]}"
    )
