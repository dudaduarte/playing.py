# -*- coding: UTF-8 -*-

class Profile(object):
  'Classe padrão para perfis de usuários'

  def __init__(self, name, phone, company):
    if len(name) < 3:
      raise InvalidArgumentError('O nome precisa ter mais de 2 caracteres')

    self.name = name
    self.phone = phone
    self.company = company
    self.__likes = 0

  def print(self):
    print('Nome: %s, Telefone: %s, Empresa: %s, Curtidas: %s' % (
      self.name,
      self.phone,
      self.company,
      self.__likes
    ))

  def like(self):
    self.__likes += 1

  def get_likes(self):
    return self.__likes

  @classmethod
  def print_all(self, profiles_list):
    for profile in profiles_list:
      profile.print()

  @classmethod
  def generate_profiles(cls, received_file):
    profiles = []
    file = None
    try:
      with open(received_file, 'r') as file:
        for line in file:
          profile_params = line.split(',')
          if len(profile_params) is not 3:
            raise InvalidArgumentError('Uma linha precisa ter 3 informações.')
          profiles.append(cls(*profile_params))
      return profiles
    except Exception as error:
        print('Error: %s' % error)
    finally:
      if(file is not None):
        file.close()

class Profile_Vip(Profile):
  'Classe padrão para perfis de usuários VIP'

  def __init__(self, name, phone, company, nickname = ''):
    super().__init__(name, phone, company)
    self.nickname = nickname

  def get_credits(self):
    return super().get_likes() * 10.00

class InvalidArgumentError(Exception):
  def __init__(self, message):
    self.message = message

  def __str__(self):
    return repr(self.message)