import csv
import json


class ReadCsvCreateForWordcloud:
    def read(self):
        # with open() as f:
        with open(, 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            t = list()
            for x, y in data:
                aa = dict(text=x, value=y)
                t.append(aa)
            p = json.dumps(t)
        return p

