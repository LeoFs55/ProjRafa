import json
class ConnectionJson:
    def __init__(self):
        self.nameArq = ''
        self.arqWay = 'Arquivos_Python\\pasta arquivo\\'

    def nameChanger(self,nameNew):
        self.nameArq = nameNew
        caminho = self.arqWay + self.nameArq
        return caminho
    
    def reader(self,  arqWay):
        with open(arqWay,'r',encoding='utf8') as arquivo:
            people = json.load(arquivo)
            return people
    
    def writer(self, nemUser, arqWay, list):
        with open(arqWay, 'w',encoding='utf8') as arquivo:
            list.append(nemUser)
            json.dump(list, arquivo,indent=3)

import pymysql.cursors
class ConnectioSql:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='1234', database='bd_project',cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.connection.cursor()

    def writer(self, infFormted):
        with self.cur as cur:
            sql = "INSERT INTO cadastro (name, surname, birth, cpf, email, password) VALUES (%s, %s, %s, %s, %s,%s)"
            cur.execute(sql,infFormted)
        self.connection.commit()
    
    def extration(self,strSelect):
        with self.cur as cur:
            cur.execute(f"SELECT {strSelect} FROM cadastro")
            result = cur.fetchall()
        return result
