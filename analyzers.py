from base import Analyzer
import os
import hashlib
from pathlib import Path

class SizeAnalyzer(Analyzer):
    """Считает размер папки и её подпапок."""
    def run(self, path: str) -> dict:
        size_dict = {}
        for root, dirs, files in os.walk(path):
            total = sum(os.path.getsize(Path(root) / f) for f in files)
            size_dict[root] = total
        return size_dict
    
class DuplicateFinder(Analyzer):
    """Ищет дубликаты файлов (по размеру и хешу MD5)"""
    def run(self, path: str) -> dict:
        hashes = {}
        for file in Path(path).glob('*'):
            if file.is_file():
                file_hash = self._calculate_hash(file)
                if file_hash in hashes:
                    hashes[file_hash].append(str(file))
                else:
                    hashes[file_hash] = [str(file)]
        return {k: v for k, v in hashes.items() if len(v) > 1}

    def _calculate_hash(self, file: Path) -> str:
        md5 = hashlib.md5()
        with open(file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5.update(chunk)
        return md5.hexdigest()
