from config import conexao
cursor = conexao.cursor()

print("selecione a consulta")
print("01 - selecionar todas as pessoas que tem mais de 18 anos")
print("02 - selecionar todas as colunas da cidade")
print("03 - selecionar a uf e quantas cidades tem em cada uf")
print("04 - selecionar a pessoa mais velha")
print("05 - selecionar qual a pessoa mais nova")
print("06 - selecionar o nome, endereco, telefone, celular, nome_cidade, nascimento das pessoas que moram no PR")
print("07 - selecionar as cidades possuem pessoas cadastradas e quantas pessoas em cada cidade")
print("08 - selecionar todas as pessoas ativas exibindo todas as colunas ordenando pelo telefone")
print("09 - selecionar todas as cidades que nao possuem pessoas")
print("10 - selecionar quais pessoas tem e-mail do hotmail")

opt=int(input(print("Qual opção: ")))
sql: str

match opt:
    case 1:
        sql="select * from pessoa where nascimento <= DATE_SUB(CURRENT_DATE, INTERVAL 18 YEAR)"
       
    case 2:
        sql="select * from cidade"
        
    case 3:
        sql = ""
      
    case 4:
        sql = ""
       
    case 5:
        sql = ""
       
    case 6:
        sql = ""
     
    case 7:
        sql = ""
      
    case 8:
        sql = ""
        
    case 9:
        sql = ""
        
    case 10:
        sql = ""
   
cursor.execute(sql)

resultados = cursor.fetchall()

cursor.close()
conexao.close()

for linha in resultados:
    print(str(linha))
    print('--------------------------------------')        