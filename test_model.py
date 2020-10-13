from datetime import date, timedelta
import pytest
from model import Space,User

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)
user1 = User(name='li')

def test_became_an_child_space():
    s1 = Space('s1','祁县')
    s2 = Space('s11','铺西')
    s2.join_to(s1)
    s2.join_to(s1)
    assert {Space('s1', '铺西')} == s2.parents

def test_user_create_space():
    space = Space.create(user1,space_name='铺西',descriptions='我们的家乡')
    assert user1 in space.moderators and space in user1.mod_spaces
