# Video Processing Project

Этот проект предназначен для обработки видеофайлов из RAR-архива, объединения их в одно видео и оптимизации.

## Требования

- Python 3.7 или выше
- pip (пакетный менеджер Python)
- FFmpeg
- unrar

video_processing_project/
│
├── main.py               # Основной скрипт для обработки видео
├── requirements.txt      # Файл для установки зависимостей
├── README.md             # Инструкции по использованию
└── example_archive.rar   # Пример архива (может быть удален или заменен вашим архивом)


## Установка зависимостей

1. Клонирование репозитория

Сначала клонируйте репозиторий проекта (если он размещен на GitHub):

    ```
    git clone https://github.com/yourusername/video_processing_project.git
    cd video_processing_project
    ```

2. Установите зависимости из `requirements.txt`:

   ```
   pip install -r requirements.txt
   sudo apt-get install unrar
   ```

3. Установка FFmpeg

    ```
    sudo apt-get update
    sudo apt-get install ffmpeg
    ```

4. Установка unrar

    ```
    sudo apt-get install unrar
    ```

5. Использование
    ```
    python main.py путь/к/архиву.rar путь/к/выходному/файлу.mp4
    ```

Пример:

    ``` python main.py example_archive.rar output.mp4
    ```




