from transformers import AutoTokenizer, AutoModelForCausalLM

TOKENIZER = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
MODEL = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

def generate_ans(user_prompt, tokenizer, model):
    try:
        # модель, которую необходимо использовать, продолжает текст, а не выдает самостоятельный ответ (как например chatgpt)
        # поэтому пользовательский промпт заворачивается в питоновский комментарий, а далее напишется "def", чтобы модель восприняла это
        # как начало кода, который необходимо продолжить.
        text = f"'''\nuser prompt:\n{user_prompt}\nWrite Python code IN ENGLISH below:\n'''\ndef"

        input_ids = tokenizer(text, return_tensors="pt").input_ids

        generated_ids = model.generate(
            input_ids,
            max_length=512,
            num_return_sequences=1,
            temperature=0.1,        # случайность генерации (детерминированность)
            do_sample=True,         # также для более случаной генерации (при True)
            top_p=0.95,             # с какой минимальной вероятностью рассматривать следующий токен
            top_k=40,               # ограничевает выборку данным количеством наиболее вероятных токенов
            repetition_penalty=1.1, # значение >1.0 - штраф за повторения
        )

        ans = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        # обрезаем начало (пользовательский промпт)
        # также модель часто начинает повторяться, если не достигла максимальной длины ответа.
        # поэтому все повторения (они опять же начинаются с плльзовательского промпта) обрезаем тем же срезом.
        ans = ans[len(text) - 3:ans.find(text[:15], len(text)) if ans.find(text[:15], len(text)) != -1 else len(ans)]
        print(ans)
        return ans

    except Exception as e:
        print(f"ошибка: {e}")
        return None
