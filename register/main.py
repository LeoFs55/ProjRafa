from register import Usuario
user = Usuario()
user.register(nome='Leonardo',sobrenome='Figorelli Santana',data_nascimento='28/10/2005',cpf='48448072855',password='Senha123!',number='11944636254',genero='masculino')
#{'nome': 'leonardo', 'sobrenome': 'figorelli santana', 'data_nascimento': '28/10/2005', 'cpf': '48448072855', 'password': 'Senha123!'
print(user.__dict__)
