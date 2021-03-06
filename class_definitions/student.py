class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
        if not (characters.issuperset(lname) and characters.issuperset(fname) and
                characters.issuperset(major)):
            raise ValueError

        if gpa and not isinstance(gpa, float):
            raise ValueError

        if gpa and gpa < 0.0 or gpa > 4.0:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
