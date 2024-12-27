#!/bin/bash

# Перевіряємо, чи існує cli.py в поточній директорії
if [ -f "cli.py" ]; then
    # Створюємо символічне посилання в /usr/bin
    sudo ln -s "$(pwd)/cli.py" /usr/bin/mashup
    echo "Символічне посилання створено: /usr/bin/mashup."
else
    echo "Файл cli.py не знайдений в поточній директорії."
    exit 1
fi

