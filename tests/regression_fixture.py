from django.contrib.auth.models import User
from pytest import fixture

@fixture
def test_user(db):
    user = User.objects.create_user('test', 'test@test.com', '123')
    return user
