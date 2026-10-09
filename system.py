import os
import sys
import platform
os_name = os.name
os_getcwd = os.getcwd()
sys_platform = sys.platform
python_version = sys.version
platform_system = platform.system()
platform_release = platform.release()
platform_processor = platform.processor()
system_info_list = [
    os_name,
    os_getcwd,
    sys_platform,
    python_version,
    platform_system,
    platform_release,
    platform_processor
]
menu_items = [
    "Имя ОС (os.name)",
    "Текущая рабочая директория (os.getcwd)",
    "Платформа Python (sys.platform)",
    "Версия Python (sys.version)",
    "Система (platform.system)",
    "Релиз (platform.release)",
    "Процессор (platform.processor)"
]

def print_menu():
    """Выводит меню на экран, используя sys.stdout"""
    sys.stdout.write("\n--- МЕНЮ СИСТЕМНОЙ ИНФОРМАЦИИ ---\n")
    for i, item in enumerate(menu_items):
        sys.stdout.write(f"{i + 1}. {item}\n")
    sys.stdout.write("0. Выход\n")
    sys.stdout.write("Выберите пункт: ")
    sys.stdout.flush()

def main():
    while True:
        print_menu()
        try:
            choice = sys.stdin.readline().strip()
        except KeyboardInterrupt:
            sys.stdout.write("\nВыход...\n")
            break

        if choice == '0':
            sys.stdout.write("Завершение работы программы.\n")
            break
        if choice.isdigit() and 1 <= int(choice) <= len(system_info_list):
            index = int(choice) - 1
            result = system_info_list[index]
            # 5. Распечатываем результат
            sys.stdout.write(f"\nРезультат: {result}\n")
        else:
            sys.stdout.write("\nНекорректный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
