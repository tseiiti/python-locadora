from model import Model

class AtorModel(Model):
  def __init__(self):
    super().__init__()
    self.filme = Model("Filme")
    self.atuar = Model("Atuar")
