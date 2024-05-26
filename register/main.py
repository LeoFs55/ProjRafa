class Usuario:
    def __init__(self):
        self.nome = str()
        self.sobrenome = str()
        self.data_nascimento = str()
        self.cpf = str()
        self.senha = str()
        self.email = str()
        self.validado = bool()

    def formaterInfoToSQL(self):
        name = self.nome
        surname = self.sobrenome
        birth = self.data_nascimento
        cpf = self.cpf
        password = self.senha
        email = self.email
        return (name, surname, birth, cpf,email, password)

    def register(self,nome,sobrenome,data_nascimento,cpf,password,email):
        if validations(nome,data_nascimento,cpf,password):
            self.nome = inputFormat(nome,tipo='name')
            self.sobrenome = inputFormat(sobrenome,tipo='name')
            self.data_nascimento = inputFormat(data_nascimento,tipo='birth')
            self.cpf = inputFormat(cpf,tipo='name')
            self.senha = password
            self.email = email
            self.validado = True
        else:
            self.validado = False

from datetime import date

def validations(nome, data_nascimento, cpf, password):

    def nomeValid(nome):
        nameList = [i.isalpha() for i in nome.split(' ')]
        if False in nameList:
            return False
        firstName = nome.split()[0]
        repFirstName = firstName[0]*len(firstName)
        if firstName == repFirstName:
            return False
        return True
    
    def dataValid(data_nascimento):
        dia,mes,ano = data_nascimento.split('/')
        dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)

        try:
            valition = date(ano_int, mes_int, dia_int)
            return True
        
        except:
            return False

    def cpfValid(cpf):

        if not cpf.isnumeric():
            return False
        
        resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(10,1,-1))]
        soma = sum(resultado)        
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        digito1 = str(digito)

        resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(11,1,-1))]
        soma = sum(resultado)        
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        digito2 = str(digito)

        cpfCriado = cpf[:9]+digito1+digito2

        return True if cpfCriado == cpf else False
    
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

    allValid = nomeValid(nome) and dataValid(data_nascimento) and cpfValid(cpf) and passwordValid(password)
    return allValid

def inputFormat(input, tipo):

    if tipo == 'name':
        return input.lower()
    
    if tipo == 'birth':
        dia,mes,ano = input.split('/')
        dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)
        return f'{ano_int}-{mes_int}-{dia_int}'