import random
import os

def list_formatter(non_formatted_list):
    """Функция для форматирования списка с добавлением смайликов."""
    smiles = ['🙈', '🙉', '🙊']

    # Добавляем смайлики между элементами списка
    formatted_list = f" {random.choice(smiles)} ".join(non_formatted_list)

    return formatted_list

def find_random_video():
    VIDEO_FOLDER = os.path.join(os.getcwd(), "video_data")
    try:
        files = os.listdir(VIDEO_FOLDER)
        print(f"Файлы в папке: {files}")  # Выведет список файлов

        videos = [f for f in files if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
        print(f"Найденные видеофайлы: {videos}")

        if not videos:
            return None

        return os.path.join(VIDEO_FOLDER, random.choice(videos))

    except Exception as e:
        print(f"Ошибка: {e}")
        return None
