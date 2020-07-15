### Playing With Python

#### Pré-requisitos
Para os códigos desse repositório funcionarem, é necessário ter o Python 3 instalado na máquina.
[Download](https://www.python.org/downloads/)

#### Manipulando uma lista
Para manipular uma lista de nomes, acesse a pasta da aplicação:
```sh
cd playing.py/
```

Inicie a aplicação:
```sh
python app.py
```

Agora, é só seguir as instruções que aparecerão no terminal.

#### Criando perfis de usuários
Para utilizar as classes de criação de perfis para usuários, é necessário estar na pasta do repositório:
```sh
cd playing.py/
```

E iniciar o terminal do Python:
```sh
python
```

Agora, é necessário importar as classes de models:
```py
from models import *
```

Criando um perfil normal e um perfil vip:
```py
perfil = Profile('Pandora', '1234567', 'Pandora S/A')
perfil_vip = Profile_Vip('Apolo', '9876543', 'Pandora S/A')
```

Imprimindo um perfil:
```py
perfil.print()
```

Criando vários perfis a partir de um arquivo:
```py
perfis = Profile.generate_profiles('perfis.csv')
```

Imprimindo uma lista de perfis:
```py
Profile.print_all(perfis)
```