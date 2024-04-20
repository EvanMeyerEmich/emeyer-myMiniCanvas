# test_course.py
import pytest
from course import CourseManager, Course

class TestCourseManager:
    def test_init(self):
        manager = CourseManager()
        assert manager.course_list == []
        assert manager.counter == 0

    def test_generate_id(self):
        manager = CourseManager()
        id1 = manager.generate_id()
        assert id1 == 1
        id2 = manager.generate_id()
        assert id2 == 2

    def test_create_a_course(self):
        manager = CourseManager()
        course_id = manager.create_a_course("COSC381", "Winter", [1, 2, 3])
        assert course_id == 1
        assert len(manager.course_list) == 1
        course = manager.course_list[0]
        assert course.course_code == "COSC381"
        assert course.semester == "Winter"
        assert course.teacher_list == [1, 2, 3]

    def test_find_a_course(self):
        manager = CourseManager()
        manager.create_a_course("COSC311", "Fall", [4])
        found_course = manager.find_a_course(1)
        assert found_course.course_code == "COSC311"
        assert not manager.find_a_course(2)  # Should return None

class TestCourse:
    def test_init(self):
        course = Course(1, "Math101", "Winter", [5])
        assert course.course_id == 1
        assert course.course_code == "Math101"
        assert course.semester == "Winter"
        assert course.teacher_list == [5]
