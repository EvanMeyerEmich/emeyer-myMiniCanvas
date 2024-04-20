from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
from course import Course  

client = TestClient(app)

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.strip('"') == "Welcome to our miniCanvas!"

def test_create_a_course():
    """Test creating a course."""
    course_data = {
        "teacher_id_list": [1, 2, 3],
        "semester": "Winter"
    }
    response = client.post("/courses/COSC381", json=course_data)
    assert response.status_code == 200, f"Course should be created successfully, got: {response.text}"
    assert "course_id" in response.json(), "Response should include a 'course_id'"

def test_import_students():
    with patch('main.coursemanager.find_a_course') as mock_find:
        mock_course = Course(course_id=1, course_code='COSC381', semester='Winter', teacher_list=[])
        mock_course.import_students = lambda x: None  # Mock the method to do nothing
        mock_find.return_value = mock_course
        
        student_data = [101, 102, 103]
        response = client.put("/courses/1/students", json=student_data)
        assert response.status_code == 200, f"Students should be imported successfully, got: {response.text}"
        assert mock_course.student_list == [], "Check that no students were actually added in the mock"
