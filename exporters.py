from base import Exporter
import json
import csv

class JSONExporter(Exporter):
    """Сохраняет данные в JSON."""
    def save(self, data: dict, filename: str):
        with open(f"{filename}.json", 'w') as f:
            json.dump(data, f, indent=4)

class CSVExporter(Exporter):
    """Сохраняет данные в CSV."""
    def save(self, data: dict, filename: str):
        with open(f"{filename}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Path", "Size (MB)"])
            for path, size in data.items():
                writer.writerow([path, f"{size / (1024*1024):.2f}"])
