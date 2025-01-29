def list_formatter(non_formatted_list):
    formatted_list = (str(non_formatted_list).replace('[', '').replace("'", "🔥")
                      .replace(']', '').replace(',', ' '))
    return formatted_list
