from model import Model

class ClienteModel(Model):
  def __init__(self):
    super().__init__()
    self.alugar = Model("Alugar")
