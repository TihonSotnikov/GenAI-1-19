from main import generate_ans, TOKENIZER, MODEL
import ast # parse

def test_code_syntax(generated_code):
    if generated_code is None:
        print("функция генерации вернула None")
        return 0

    try:
        ast.parse(generated_code)
    except SyntaxError:
        return 0
    return 1

def tests():
    print("\n\n---------------- Начало тестов... ----------------\n\n")

    assert test_code_syntax(generate_ans("напиши функцию, которая выводит \"hello, world\""))
    assert test_code_syntax(generate_ans("напиши функцию, которая считает факториал"))
    assert test_code_syntax(generate_ans("напиши функцию, которая проверяет число на простоту"))

    print("---------------- Все тесты пройдены успешно. ----------------")

tests()
