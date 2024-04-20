# test_assignment.py
import pytest
from assignment import Assignment, Submission

# Tests for Assignment
class TestAssignment:
    def test_init(self):
        assignment = Assignment(1, "4-15-2024", 101)
        assert assignment.assignment_id == 1
        assert assignment.due_date == "4-15-2024"
        assert assignment.course_id == 101
        assert assignment.submission_list == []

    def test_submit(self):
        assignment = Assignment(1, "4-15-2024", 101)
        submission = Submission(201, "Essay about Github")
        assignment.submit(submission)
        assert len(assignment.submission_list) == 1
        assert assignment.submission_list[0].student_id == 201

class TestSubmission:
    def test_init(self):
        submission = Submission(301, "Project report")
        assert submission.student_id == 301
        assert submission.submission == "Project report"
        assert submission.grade == -1.0
