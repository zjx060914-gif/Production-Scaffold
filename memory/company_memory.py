import json, os

class CompanyMemory:
    def __init__(self, company):
        self.path = f"memory_store/{company}.json"

    def load(self):
        if os.path.exists(self.path):
            return json.load(open(self.path, "r", encoding="utf-8"))
        return {}

    def save(self, data):
        os.makedirs("memory_store", exist_ok=True)
        json.dump(data, open(self.path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)