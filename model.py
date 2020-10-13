from __future__ import annotations
from typing import List, Set,Optional
from hashlib import sha1
from datetime import date, datetime

'''
社区有上下级
'''
class NotFound(Exception):pass
class UserExists(Exception): pass


def generate_password(password):
    s = sha1()
    s.update(f'{password}{str(len(password)+1)}'.encode('utf-8'))
    return s.hexdigest()

# def reg(self, name,password):
#     try:
#         account = Account._by_name(name)
#         raise UserExists
#     except NotFound:
#         account = Account(
#             name=name,
#         )
#
#     return account


class User:
    def __init__(self,name):
        # self.ref = ref
        self.name = name
        self.mod_spaces = set() # type: Set[Space]

    def submit(self,space:Space,post:Post):
        post.creator = self
        space.posts.add(post)



class Post:
    def __init__(self,ref,kind,content,):
        self.ref = ref
        self.kind = kind
        self.content = content
        self.creator = None

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return other.ref == self.ref

    def __hash__(self):
        return hash(self.ref)


class Space:
    '''社区有空间概念 多个 父社区,子社区,
    '''
    def __init__(self,ref,name,create=datetime.utcnow()):
        self.ref = ref
        self.name = name
        self.moderators = set()
        self.posts = set()
        self.parents = set() #type: Set[Space]
        self.childs = set() #type: Set[Space]

    def join_to(self,space:Space):
        self.parents.add(space)

    def exit_form(self,space:Space):
        self.parents.remove(space)

    def __repr__(self):
        return f'<Space {self.ref}>'

    def __eq__(self, other):
        if not isinstance(other,Space):
            return False
        return other.ref == self.ref

    def __hash__(self):
        return hash(self.ref)

    @classmethod
    def create(cls,user:User,space_name:str,descriptions:str):

        space = Space(ref='',name=space_name,)
        mod = Moderator(space,user)
        space.moderators.add(user)
        user.mod_spaces.add(space)
        return space




class Moderator:
    def __init__(self,space:Space,account:User,):
        self.space = space
        self.account = account

    def __eq__(self, other):
        if not isinstance(other,Moderator):
            return False
        return other.space == self.space and other.account == self.account

    def __hash__(self):
        return hash(self.account)


