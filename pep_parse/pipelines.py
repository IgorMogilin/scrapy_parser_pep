from collections import defaultdict
from pathlib import Path

from pep_parse.settings import BASE_DIR, RESULTS_DIR, TIMESTAMP


class PepParsePipeline:
    def open_spider(self, spider):
        """Инициализация счетчика статистики."""
        self.status_count = defaultdict(int)
        self.total_peps = 0

    def process_item(self, item, spider):
        """Сбор статистики статусов."""
        status = item.get('status')
        if status:
            self.status_count[status] += 1
            self.total_peps += 1
        return item

    def close_spider(self, spider):
        """Запись данных статистки в файл."""
        file_name_stamp = f'{RESULTS_DIR}/status_summary_{TIMESTAMP}.csv'
        output_file_name = BASE_DIR / Path(file_name_stamp)
        with open(
            output_file_name,
            mode='w',
            encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for status, count in sorted(self.status_count.items()):
                f.write(f'{status},{count}\n')
            f.write(f'Total,{self.total_peps}\n')
