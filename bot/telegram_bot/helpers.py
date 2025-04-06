import random
import os


def list_formatter(non_formatted_list):
    smiles = ['🙈', '🙉', '🙊']

    if not non_formatted_list or not isinstance(non_formatted_list, (list, tuple)):
        return "Список пользователей пуст или недоступен"

    return f" {random.choice(smiles)} ".join(map(str, non_formatted_list))

def find_random_video():
    VIDEO_FOLDER = os.path.join(os.getcwd(), "bot/video_data")
    try:
        files = os.listdir(VIDEO_FOLDER)
        print(f"Файлы в папке: {files}")  # Выведет список файлов

        videos = [f for f in files if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
        print(f"Найденные видеофайлы: {videos}")

        if not videos:
            return None

        return os.path.join(VIDEO_FOLDER, random.choice(videos))

    except Exception as error:
        print(f"Ошибка: {error}")
        return None
