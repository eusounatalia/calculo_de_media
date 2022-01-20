from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='notasAlunos'

)


def funcao_principal():
    linha1 = teste.lineEdit_4.text()
    print('MATRÍCULA:', linha1)

    linha2 = teste.lineEdit_3.text()
    print('NOME ALUNO(A):', linha2)

    linha3 = teste.lineEdit.text()
    print('PROVA 1:', linha3)

    linha4 = teste.lineEdit_2.text()
    print('PROVA 2:', linha4)

    cursor = banco.cursor()
    comando_sql = 'insert into registro (matricula, nome,prova1,prova2) VALUES (%s,%s,%s,%s)'
    dados = (str(linha1), str(linha2), str(linha3), str(linha4))
    cursor.execute(comando_sql, dados)
    banco.commit()


def excluir():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT matricula FROM registro")
    dados_lidos = cursor.fetchall()
    valor_matricula = dados_lidos[linha][0]
    cursor.execute("DELETE from registro WHERE matricula=" + str(valor_matricula))
    print(valor_matricula)

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_sql = 'select * from registro'
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
teste = uic.loadUi('teste.ui')
segunda_tela = uic.loadUi('resultado.ui')
teste.pushButton.clicked.connect(funcao_principal)
teste.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir)

teste.show()
app.exec()
