from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import datetime

def date(string):
  ''' take a string and append the date to it'''
  return "{}-{}".format(string, datetime.date.today())

class FilterModule(object):
  def filters(self):
    return {
      'append_date' : date
    }
