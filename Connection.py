import MySQLdb # para instalar (pip install mysqlclient)

# cria a conexao
con = MySQLdb.connect(host='servidor', user='usuario', passwd='senha', db='nome_bd')

# habilita as transacoes
cursor = con.cursor()

# executa comando
cursor.execute('SELECT * FROM nome_bd.nome_tabela')

# contagem do numero de linhas da tabela
numRows = int(cursor.rowcount)

# resultados (linha(coluna 0), linha(coluna 1))
for row in cursor.fetchall():
    print (" " + row[0] + ", " + row[1])