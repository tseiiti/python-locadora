from save import sg, Save

class FilmeSave(Save):
  def get_content(self):
    content = [[
      sg.Text(text=f"{k.capitalize()}: ", size=12), 
      sg.Input(default_text=v, key=f"-{k.upper()}-", disabled=(k=="id"))
    ] for k, v in self.dic.items() if k != "categoria_id"]
    item = self.model.categoria.find(self.dic["categoria_id"]) if self.dic["categoria_id"] != "" else { "nome": "" }
    content.append([
      sg.Text(text=f"Categoria: ", size=12), 
      sg.Combo([item[1] for item in self.model.categoria.select()], default_value=item["nome"], key="-CATEGORIA_ID-", size=44)])
    return content
  
  def get_params(self, values):
    params = super().get_params(values)
    categoria_id = self.model.categoria.where(f"where nome = '{params['categoria_id']}'")[0][0]
    params["categoria_id"] = categoria_id
    return params
