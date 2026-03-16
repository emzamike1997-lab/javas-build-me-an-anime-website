### Test Strategy
The test strategy for the anime website project will involve a combination of unit tests and integration tests. Unit tests will focus on individual components and functions, while integration tests will verify the interactions between these components.

### Unit Tests
Unit tests will be written for the following components:
- Anime model
- User model
- Authentication service
- Anime service

### Integration Tests
Integration tests will be written for the following scenarios:
- User registration and login
- Anime creation, update, and deletion
- Search and filtering of anime

### Test Files

=== test_anime_model.py ===
```python
import unittest
from anime_website.models import Anime

class TestAnimeModel(unittest.TestCase):
    def test_anime_creation(self):
        anime = Anime(title="Test Anime", genre="Action")
        self.assertEqual(anime.title, "Test Anime")
        self.assertEqual(anime.genre, "Action")

    def test_anime_update(self):
        anime = Anime(title="Test Anime", genre="Action")
        anime.title = "Updated Title"
        self.assertEqual(anime.title, "Updated Title")

    def test_anime_deletion(self):
        anime = Anime(title="Test Anime", genre="Action")
        anime.delete()
        self.assertIsNone(anime)

if __name__ == "__main__":
    unittest.main()
```

=== test_user_model.py ===
```python
import unittest
from anime_website.models import User

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        user = User(username="test_user", email="test@example.com")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")

    def test_user_update(self):
        user = User(username="test_user", email="test@example.com")
        user.username = "updated_username"
        self.assertEqual(user.username, "updated_username")

    def test_user_deletion(self):
        user = User(username="test_user", email="test@example.com")
        user.delete()
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
```

=== test_auth_service.py ===
```python
import unittest
from anime_website.services import AuthService

class TestAuthService(unittest.TestCase):
    def test_user_registration(self):
        auth_service = AuthService()
        user = auth_service.register_user("test_user", "test@example.com", "password")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")

    def test_user_login(self):
        auth_service = AuthService()
        user = auth_service.login_user("test_user", "password")
        self.assertEqual(user.username, "test_user")

    def test_user_logout(self):
        auth_service = AuthService()
        auth_service.logout_user()
        self.assertIsNone(auth_service.get_current_user())

if __name__ == "__main__":
    unittest.main()
```

=== test_anime_service.py ===
```python
import unittest
from anime_website.services import AnimeService

class TestAnimeService(unittest.TestCase):
    def test_anime_creation(self):
        anime_service = AnimeService()
        anime = anime_service.create_anime("Test Anime", "Action")
        self.assertEqual(anime.title, "Test Anime")
        self.assertEqual(anime.genre, "Action")

    def test_anime_update(self):
        anime_service = AnimeService()
        anime = anime_service.create_anime("Test Anime", "Action")
        anime_service.update_anime(anime.id, "Updated Title", "Comedy")
        self.assertEqual(anime.title, "Updated Title")
        self.assertEqual(anime.genre, "Comedy")

    def test_anime_deletion(self):
        anime_service = AnimeService()
        anime = anime_service.create_anime("Test Anime", "Action")
        anime_service.delete_anime(anime.id)
        self.assertIsNone(anime_service.get_anime(anime.id))

if __name__ == "__main__":
    unittest.main()
```

=== test_integration.py ===
```python
import unittest
from anime_website.models import User, Anime
from anime_website.services import AuthService, AnimeService

class TestIntegration(unittest.TestCase):
    def test_user_registration_and_login(self):
        auth_service = AuthService()
        user = auth_service.register_user("test_user", "test@example.com", "password")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        logged_in_user = auth_service.login_user("test_user", "password")
        self.assertEqual(logged_in_user.username, "test_user")

    def test_anime_creation_and_deletion(self):
        anime_service = AnimeService()
        anime = anime_service.create_anime("Test Anime", "Action")
        self.assertEqual(anime.title, "Test Anime")
        self.assertEqual(anime.genre, "Action")
        anime_service.delete_anime(anime.id)
        self.assertIsNone(anime_service.get_anime(anime.id))

    def test_search_and_filtering(self):
        anime_service = AnimeService()
        anime1 = anime_service.create_anime("Test Anime 1", "Action")
        anime2 = anime_service.create_anime("Test Anime 2", "Comedy")
        search_results = anime_service.search_anime("Test")
        self.assertEqual(len(search_results), 2)
        filtered_results = anime_service.filter_anime("Action")
        self.assertEqual(len(filtered_results), 1)
        self.assertEqual(filtered_results[0].title, "Test Anime 1")

if __name__ == "__main__":
    unittest.main()
```

### Running Tests
To run the tests, navigate to the project directory and execute the following command:
```bash
python -m unittest discover -s tests -p 'test_*.py'
```
This will discover and run all test files in the `tests` directory that match the pattern `test_*.py`.