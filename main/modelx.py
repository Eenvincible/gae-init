# -*- coding: utf-8 -*-

import hashlib


class BaseX(object):
  @classmethod
  def retrieve_one_by(cls, name, value):
    return cls.query(getattr(cls, name) == value).get()


class ConfigX(object):
  @classmethod
  def get_master_db(cls):
    return cls.get_or_insert('master')


class UserX(object):
  def avatar_url_size(self, size=None):
    return '//gravatar.com/avatar/%(hash)s?d=identicon&r=x%(size)s' % {
        'hash': hashlib.md5((self.email or self.username).encode('utf-8')).hexdigest().lower(),
        'size': '&s=%d' % size if size > 0 else '',
      }
  avatar_url = property(avatar_url_size)
