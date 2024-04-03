import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class CadastroCliente(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cadastro de Cliente')
        self.setGeometry(100, 100, 300, 200)

        self.label_nome = QLabel('Nome:', self)
        self.label_nome.move(20, 20)
        self.entry_nome = QLineEdit(self)
        self.entry_nome.move(120, 20)

        self.label_email = QLabel('Email:', self)
        self.label_email.move(20, 50)
        self.entry_email = QLineEdit(self)
        self.entry_email.move(120, 50)

        self.label_telefone = QLabel('Telefone:', self)
        self.label_telefone.move(20, 80)
        self.entry_telefone = QLineEdit(self)
        self.entry_telefone.move(120, 80)

        self.btn_adicionar = QPushButton('Adicionar Cliente', self)
        self.btn_adicionar.clicked.connect(self.adicionar_cliente)
        self.btn_adicionar.move(20, 120)

        self.btn_exibir = QPushButton('Exibir Detalhes', self)
        self.btn_exibir.clicked.connect(self.exibir_detalhes)
        self.btn_exibir.move(150, 120)

        self.clientes = {}

    def adicionar_cliente(self):
        nome = self.entry_nome.text().strip()
        email = self.entry_email.text().strip()
        telefone = self.entry_telefone.text().strip()

        if nome and email and telefone:
            self.clientes[nome] = {'Email': email, 'Telefone': telefone}
            QMessageBox.information(self, 'Sucesso', 'Cliente adicionado com sucesso!')
        else:
            QMessageBox.critical(self, 'Erro', 'Por favor, preencha todos os campos.')

    def exibir_detalhes(self):
        nome = self.entry_nome.text().strip()

        if nome in self.clientes:
            cliente = self.clientes[nome]
            QMessageBox.information(self, 'Detalhes do Cliente', f"Nome: {nome}\nEmail: {cliente['Email']}\nTelefone: {cliente['Telefone']}")
        else:
            QMessageBox.critical(self, 'Erro', 'Cliente não encontrado.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cadastro_cliente = CadastroCliente()
    cadastro_cliente.show()
    sys.exit(app.exec_())
