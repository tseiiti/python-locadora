from model import Model

class FitaModel(Model):
  def __init__(self):
    super().__init__()
    self.filme = Model("Filme")
    self.dupla = Model("Dupla")
