import pytest
from user import UserManager, User

class TestUserManager:
    def test_init(self):
        manager = UserManager()
        assert manager.user_list == []
        assert manager.counter == 0

    def test_generate_id(self):
        manager = UserManager()
        assert manager.generate_id() == 1
        assert manager.generate_id() == 2

    def test_create_a_user(self):
        manager = UserManager()
        manager.create_a_user("Alice", "secure123", "student")
        assert len(manager.user_list) == 1
        assert manager.user_list[0].name == "Alice"
        assert manager.user_list[0].password == "secure123"
        assert manager.user_list[0].type == "student"

    def test_find_users(self):
        manager = UserManager()
        manager.create_a_user("Bob", "password", "teacher")
        manager.create_a_user("Charlie", "12345", "admin")
        users = manager.find_users([1, 3])
        assert len(users) == 1
        assert users[0].name == "Bob"

class TestUser:
    def test_init(self):
        user = User(1, "Dave", "passwd", "admin")
        assert user.user_id == 1
        assert user.name == "Dave"
        assert user.password == "passwd"
        assert user.type == "admin"

    def test_str(self):
        user = User(2, "Eve", "pass123", "teacher")
        assert str(user) == "ID: 2, name: Eve, type: teacher"

