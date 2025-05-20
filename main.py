from analyzers import SizeAnalyzer, DuplicateFinder
from exporters import JSONExporter, CSVExporter
import json

def config_loader():
    with open("config.json", 'r') as json_file:
        loader = json.load(json_file)
        return (
            loader["JSON"],
            loader["CSV"]
        )

def main():
    """Главная функция."""
    json_save, csv_save = config_loader()
    path = input("Введите путь к нужной папке: ")
    try:
        # Анализ
        size_analyzer = SizeAnalyzer()
        duplicate_finder = DuplicateFinder()
        size_dict = size_analyzer.run(path)
        duplicates = duplicate_finder.run(path)

        if json_save:
            json_exporter = JSONExporter()
            json_exporter.save(size_dict, "size_report")
            json_exporter.save(duplicates, "duplicate_report")

        if csv_save:
            csv_exporter = CSVExporter()
            csv_exporter.save(size_dict, "size_report")

    except Exception as e:
        print(f"Произошла ошибка, пожалуйста проверьте путь к папке.\n {e}")

if __name__ == "__main__":
    try:
        main()
        input("Press Enter To Exit..")
    except KeyboardInterrupt:
        print("\nДо свидания!")
