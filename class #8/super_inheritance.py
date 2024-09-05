class Person:
    def __init__(self, first_name, last_name, age, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Job(Person):
    def __init__(self, first_name, last_name, age, role, experience, previouse_role):
        super().__init__(first_name, last_name, age, role)
        self.experience = experience
        self.previouse_role = previouse_role

    def get_current_job(self):
        return f"{self.get_full_name()} {self.age} {self.role} {self.experience}"

    def get_full_name(self):
        return f"Modified Class {self.first_name} {self.last_name}"

job = Job("Joko", "Damono", 19, "Senior Software Engineer", 4, "Junior Devleloper")
print(job.get_current_job())
print(job.get_full_name())

