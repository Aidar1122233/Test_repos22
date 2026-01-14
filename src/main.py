
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


def print_author():
    # Читаем значение переменной AUTHOR из .env
    author = os.getenv('AUTHOR')

    # Проверяем, что переменная была найдена
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Переменная AUTHOR не найдена в .env файле")


# Проверка работы функции
if __name__ == "__main__":
    print_author()