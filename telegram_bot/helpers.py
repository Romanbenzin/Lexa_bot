import random

def list_formatter(non_formatted_list):
    smiles = ['🙈', '🙉', '🙊']
    formatted_list = (str(non_formatted_list).replace(
        '[', '').replace('(', '').replace(')', '').replace(
        "'", "").replace(']', '').replace(',', ' ').replace(
        '  ', ' ').replace('  ', f'{random.choice(smiles)}')
    )

    return formatted_list
