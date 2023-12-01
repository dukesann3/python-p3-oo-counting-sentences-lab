#!/usr/bin/env python3

import re

class MyString:
  
  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value,str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    value_converted_list = list(self._value)
    return True if value_converted_list[-1] == "." else False

  def is_question(self):
    value_converted_list = list(self._value)
    return True if value_converted_list[-1] == "?" else False
  
  def is_exclamation(self):
    value_converted_list = list(self._value)
    return True if value_converted_list[-1] == "!" else False
  
  def count_sentences(self):
    sentence_list = re.split('[(! )(. )(? )][\s]', self._value)
    if not sentence_list == [""]:
      return len(sentence_list)
    else:
       return 0

  