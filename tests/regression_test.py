from django.contrib.auth.models import User
from django.core.management import call_command
from pytest import mark
from tests.regression_fixture import test_user

@mark.django_db
def test_user_exists(test_user):
    print User.objects.all()
    call_command('loaddata', 'test_fixture.json')
    print User.objects.all()
    assert 0
