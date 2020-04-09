import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Wilhelm', 'Greg', 'Java Application Developer Certificate')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Wilhelm')
        self.assertEqual(self.student.first_name, 'Greg')
        self.assertEqual(self.student.major, 'Java Application Developer Certificate')

    def test_object_created_all_attributes(self):
        student = t.Student('Wilhelm', 'Greg', 'Java Application Developer Certificate', 4.0)
        assert student.last_name == 'Wilhelm'
        assert student.first_name == 'Greg'
        assert student.major == 'Java Application Developer Certificate'
        assert student.gpa == 4.0


if __name__ == '__main__':
    unittest.main()
