from model import Model

class FilmeModel(Model):
  def __init__(self):
    super().__init__()
    self.categoria = Model("Categoria")
