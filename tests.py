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
    assert test_code_syntax(generate_ans("напиши функцию, которая выводит \"hello, world\"", tokenizer=TOKENIZER, model=MODEL))
    assert test_code_syntax(generate_ans("напиши функцию, которая считает факториал", tokenizer=TOKENIZER, model=MODEL))
    assert test_code_syntax(generate_ans("напиши функцию, которая проверяет число на простоту", tokenizer=TOKENIZER, model=MODEL))

tests()
