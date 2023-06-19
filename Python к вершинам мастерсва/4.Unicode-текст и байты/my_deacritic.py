import unicodedata



def shave_marks(txt):
    """
    Удаляет диакритические знаки из заданной строки и возвращает результат.

    Аргументы:
    txt -- строка, из которой нужно удалить диакритические знаки

    Возвращаемое значение:
    Строка без диакритических знаков

    Используемые модули:
    unicodedata -- модуль для работы с текстом в Unicode формате

    Используемый алгоритм:
    1. Нормализация текста в Unicode-форме NFD с помощью функции normalize().
    2. Создание новой строки, в которой удаляются все символы,
      являющиеся комбинирующими знаками диакритик,
      с помощью генератора списка и функции combining().
    3.Применение функции normalize("NFC", shaved)
       к строке shaved для получения результата в формате NFC.

    Пример использования:
    order = "Herr Voß: • 1⁄2 cup of OEtkerTM caffè latte • bowl of açaí."
    result = shave_marks(order)
    print(result)
    # результат: "Herr Voss: • 1⁄2 cup of OEtkerTM caffe latte • bowl of acai."
    """
    norm_txt =unicodedata.normalize('NFD',txt)
    shaved = ''.join(c for c in norm_txt 
                     if not unicodedata.combining(c))
    print(shaved)
    return unicodedata.normalize("NFC", shaved)

order = "Herr Voß: • 1⁄2 cup of OEtkerTM caffè latte • bowl of açaí."

print(shave_marks(order))
