# -*- coding: UTF-8 -*-

import re

def list_names(names):
  print('Listando os nomes:')
  for name in names:
    print(name)

def add_name(names):
  print('Digite o nome que deseja inserir à lista:')
  name = input()
  names.append(name)

def remove_name(names):
  print('Digite o nome que deseja remover da lista:')
  name = input()

  if name in names:
    names.remove(name)
  else:
    print('O nome {} não existe na lista'.format(name))

def change_name(names):
  print('Digite o nome que deseja alterar:')
  name_to_be_changed = input()

  if name_to_be_changed in names:
    print('Digite o nome com a alteração que deseja fazer:')
    position = names.index(name_to_be_changed)
    new_name = input()
    names[position] = new_name
  else:
    print('O nome informado não existe na lista')

def re_search_name(names):
  print('Digite o nome que deseja procurar:')
  name = input()

  if name in names:
    names_concat = ' '.join(names)
    result = re.findall(name, names_concat)
    print(result)
  else:
    print('O nome {} não existe na lista.'.format(name))

def menu():
  names = []
  user_input = ''

  while user_input != '0':
    print('Digite:')
    print('1 para inserir um nome')
    print('2 para listar os nomes')
    print('3 para remover um nome')
    print('4 para alterar um nome')
    print('5 para procurar um nome')
    print('Ou 0 para sair da aplicação:')
    user_input = input()

    if user_input == '1':
      add_name(names)

    if user_input == '2':
      list_names(names)

    if user_input == '3':
      remove_name(names)

    if user_input == '4':
      change_name(names)

    if user_input == '5':
      re_search_name(names)

menu()