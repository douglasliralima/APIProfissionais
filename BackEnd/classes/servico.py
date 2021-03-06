from datetime import datetime
from pytz import timezone

recife = timezone('America/Recife')

class Servico:
	def __init__(self, idservico, cliente, titulo, categoria, descricaoGeral, foto):
		self.__id = idservico
		self.__cliente = cliente
		self.__data = datetime.now(recife)
		self.__titulo = titulo
		self.__categoria = categoria
		self.__descricaoGeral = descricaoGeral
		self.__foto = foto
		self.__status = "pendente"
		self.__orcamentos = 0
		self.__visualizacoes = 0

	def getCliente(self):
		return self.__cliente

	def getData(self):
		return self.__data

	def getTitulo(self):
		return self.__titulo

	def getCategoria(self):
		return self.__categoria

	def getDescricaoGeral(self):
		return self.__descricaoGeral

	def getFoto(self):
		return self.__foto

	def getStatus(self):
		return self.__status

	def getId(self):
		return self.__id

	def setTitulo(self, novotitulo):
		self.__titulo = novotitulo

	def setCategoria(self, categoria):
		self.__categoria = categoria

	def setDescricaoGeral(self, descricaoGeral):
		self.__descricaoGeral = descricaoGeral

	def setFoto(self, foto):
		self.__foto = foto

	def setStatus(self, status):
		self.__status = status

	def setId(self, ident):
		self.__id = ident

	def addOrcamento(self):
		self.__orcamentos += 1

	def addVisualizacoes(self):
		self.__visualizacoes += 1

	def getOrcamentos(self):
		return self.__orcamentos

	def getVisualizacoes(self):
		return self.__visualizacoes
