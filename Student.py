import json

class StudentNode:
    def __init__(self, student_id, info):
        self.student_id = student_id
        self.info = info
        self.next = None

class StudentLinkedList:
    def __init__(self, file_path="Student.json"):
        self.head = None
        self.tail = None
        self.file_path = file_path
        self.students = self.load_students()
        self.build_linked_list()

    def load_students(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_students(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.students, f, indent=4)

    def build_linked_list(self):
        sorted_items = sorted(self.students.items(), key=lambda item: item[1]['last_name'].lower())
        for student_id, info in sorted_items:
            self.insert_node(student_id, info, save=False)

    def insert_node(self, student_id, info, save=True):
        new_node = StudentNode(student_id, info)

        if self.head is None or info['last_name'].lower() < self.head.info['last_name'].lower():
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            prev = None
            curr = self.head
            while curr and curr.info['last_name'].lower() < info['last_name'].lower():
                prev = curr
                curr = curr.next
            new_node.next = curr
            if prev:
                prev.next = new_node
            if new_node.next is None:
                self.tail = new_node

        self.students[student_id] = info
        if save:
            self.save_students()

    def display_students(self):
        curr = self.head
        while curr:
            info = curr.info
            print(f"{info['last_name']}, {info['first_name']} - {info['section']} ({curr.student_id})")
            curr = curr.next

    def get_student_info(self, student_id):
        return self.students.get(student_id)