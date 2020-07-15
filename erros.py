# -*- coding: UTF-8 -*-
from models import Profile

try:
  file = open('nao_existe.txt','r')
  print('O arquivo foi aberto')
  file.close()
except (IOError, TypeError, NameError) as error:
  print('Error: %s !' % error)

try:
  file = open('perfis.csv','r')
  values = file.readline().split(':')
  Profile(*values)
  file.close()
except IOError as error:
  print('IOError: %s' % error)
except  TypeError as error:
  print('TypeError: %s' % error)
