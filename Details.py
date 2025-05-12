import json

class Details:
    def __init__(self, file_path="Details.json"):
        self.file_path = file_path
        self.data = self.load_details()

    def load_details(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get_subjects_for_section(self, section_code):
        return self.data.get(section_code, [])

    def add_section_subjects(self, section_code, subjects):
        self.data[section_code] = subjects
        self.save_details()

    def save_details(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)