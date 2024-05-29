class Usuario:
    def __init__(self):
        arguments = ['nome','sobrenome','data_nascimento','cpf','senha','email','numero','genero','valido']
        for i in arguments:
            setattr(self, i, None)

    def register(self,nome,sobrenome,data_nascimento,cpf,password,genero,email=None,number=None):
        if validations(nome,sobrenome,cpf,password):
            atributs = [
            ('nome', inputFormat(nome,tipo='name')),
            ('sobrenome', inputFormat(sobrenome,tipo='name')),
            ('data_nascimento', data_nascimento),
            ('cpf', cpf),
            ('senha', password),
            ('email', email),
            ('numero', number),
            ('genero', genero),
            ('valido', True)
            ]
            for atributo, valor in atributs:
                setattr(self, atributo, valor)
        else:
            self.validado = False

from datetime import date

def validations(nome, sobrenome, cpf, password):

    def nomeValid(nome):
        nameList = [i.isalpha() for i in nome.split(' ')]
        if False in nameList:
            return False
        firstName = nome.split()[0]
        repFirstName = firstName[0]*len(firstName)
        if firstName == repFirstName:
            return False
        return True


    def cpfValid(cpf):

        if not cpf.isnumeric():
            return False
        
        listInd = [10,11]
        cpf_base = cpf[:9]
        for i in listInd:
            resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(i,1,-1))]
            soma = sum(resultado)        
            digito = ((soma*10)%11)
            digito = 0 if digito > 9 else digito
            cpf_base += str(digito)

        return True if cpf_base == cpf else False
    
    def passwordValid(password):
        
        first = password[0].isupper()
        if not first:
            return False
        
        quant = len(password)
        if quant<7:
            return False
        
        special = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','_','+']
        for i in special:
            if i in password:
                return True

    allValid = nomeValid(nome) and nomeValid(sobrenome) and cpfValid(cpf) and passwordValid(password)
    return allValid

def inputFormat(input, tipo):

    if tipo == 'name':
        return input.lower()
    
    if tipo == 'birth':
        dia,mes,ano = input.split('/')
        dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)
        return f'{ano_int}-{mes_int}-{dia_int}'
    
    if tipo == 'number':
        number = input
        return f'({number[:2]}){number[2:7]}-{number[7:]}'
         