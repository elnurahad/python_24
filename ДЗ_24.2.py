# 2. Напишите генератор, который будет генерировать арифметическую прогрессию

def arithmetic_progression(first_term, common_difference, num_terms):
    term = first_term
    for _ in range(num_terms):
        yield term
        term += common_difference


for term in arithmetic_progression(1, 2, 10):
    print(term)       