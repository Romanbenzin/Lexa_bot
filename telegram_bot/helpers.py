import random

def list_formatter(non_formatted_list):
    """Функция для форматирования списка с добавлением смайликов."""
    smiles = ['🙈', '🙉', '🙊']

    # Добавляем смайлики между элементами списка
    formatted_list = f" {random.choice(smiles)} ".join(non_formatted_list)

    return formatted_list

