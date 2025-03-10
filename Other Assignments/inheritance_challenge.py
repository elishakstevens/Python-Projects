
#Parent Class
class Job:
    title = "Unknown"
    location = "Unknown"
    entry_level = True
    start_time = "09:00"
    end_time = "17:00"

    def info(self):
        msg = "\nPosition: {}\nLocation: {}\nEntry Level: {}\nBeginning of Day: {}\nEnd of Day: {}".format(self.title, self.location, self.entry_level, self.start_time, self.end_time)
        return msg

#Child Class
class Teacher(Job):
    title = "High School Math Teacher"
    location = "Bellingham High School"
    entry_level = False
    start_time = "07:45"
    end_time = "14:15"
    education = "Master's Degree"

    def detail(self):
        msg = "\nAll teachers at {} are required to have at least a {}!".format(self.location, self.education)
        return msg






if __name__ == "__main__":
    teacher = Teacher()
    print(teacher.info())
    print(teacher.detail())
