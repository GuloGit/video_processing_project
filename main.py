import os
import subprocess
import rarfile
import re

def extract_files(rar_path, extract_to):
    with rarfile.RarFile(rar_path) as rf:
        rf.extractall(path=extract_to)
    print(f"Files extracted to {extract_to}")

def create_file_list(video_files, list_path):
    with open(list_path, 'w') as f:
        for video in video_files:
            f.write(f"file '{video}'\n")
    print(f"File list created at {list_path}")

def concatenate_videos(file_list, output_path):
    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', file_list, 
        '-vf', 'scale=1280:720', '-c:v', 'libx264', '-preset', 'fast', '-crf', '23', 
        '-c:a', 'aac', '-b:a', '128k', output_path
    ]
    subprocess.run(command, check=True)
    print(f"Videos concatenated into {output_path}")

def natural_sort_key(s):
    # Function to define a sort key that handles numbers naturally
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def process_archive(rar_path, output_video):
    extract_to = '/tmp/extracted_videos'
    os.makedirs(extract_to, exist_ok=True)
    
    # Распаковка файлов
    extract_files(rar_path, extract_to)
    
    # Получение списка видеофайлов
    #video_files = [os.path.join(extract_to, file) for file in os.listdir(extract_to) if file.endswith('.mp4')]
    #video_files = sorted([os.path.join(extract_to, file) for file in os.listdir(extract_to) if file.endswith('.mp4')], key=lambda x: int(x.split('-')[1].strip().split('.')[0].replace('M-', '')))
    video_files = sorted([os.path.join(extract_to, file) for file in os.listdir(extract_to) if file.endswith('.mp4')], key=natural_sort_key)
    
     
    # Вывод списка файлов для проверки
    print("Список видеофайлов для объединения:")
    for video_file in video_files:
        print(video_file)
    
    # Запрашиваем подтверждение от пользователя
    response = input("Хотите продолжить с этими файлами? (yes/no): ")
    
    # Проверяем ответ пользователя
    if response.lower() != "yes":
        print("Вы отказались продолжать. Программа завершена.")
        exit()

    # Создание файла списка видео
    file_list_path = os.path.join(extract_to, 'mylist.txt')
    create_file_list(video_files, file_list_path)
    
    # Объединение видео
    concatenate_videos(file_list_path, output_video)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Process and concatenate video files from a RAR archive.")
    parser.add_argument("rar_path", type=str, help="Path to the RAR archive")
    parser.add_argument("output_video", type=str, help="Path to the output video file")
    
    args = parser.parse_args()
    process_archive(args.rar_path, args.output_video)
