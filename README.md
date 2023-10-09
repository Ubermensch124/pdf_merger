# Обработка группы PDF-файлов

## По мотивам задания с фриланс-биржи

Использованные библиотеки:

- fire (для работы с CLI)
- PyPDF2

Собранный docker image: <https://hub.docker.com/r/ubermensch124/pdf_merger/tags>

Алгоритм запуска:

- Скачать Docker
- Создать директорию с двумя папками: изначальные pdf и обновленные титульные листы
- Открыть терминал и вставить следующие команды:

    ```bash
    :: путь до директории с нужными папками
    set DIR_PATH=C:/Users/Mark/Desktop/Freelance/pdf_inserter/files
    :: название папки с pdf
    set PDF=raw_files
    :: название папки с титульными листами
    set LIST=new_list
    
    docker pull ubermensch124/pdf_merger
    docker run --rm -v %DIR_PATH%:/app/files/ ubermensch124/pdf_merger %PDF% %LIST%

    start %DIR_PATH%/result
    echo "Для выхода нажмите enter"
    ```
