from save import sg, Save

class FitaSave(Save):
  def get_content(self):
    content = [[
      sg.Text(text=f"{k.capitalize()}: ", size=12), 
      sg.Input(default_text=v, key=f"-{k.upper()}-", disabled=(k=="id"))
    ] for k, v in self.dic.items() if k != "filme_id"]
    item = self.model.filme.find(self.dic["filme_id"]) if self.dic["filme_id"] != "" else { "titulo": "" }
    content.append([
      sg.Text(text=f"Filme: ", size=12), 
      sg.Combo([item[1] for item in self.model.filme.select()], default_value=item["titulo"], key="-FILME_ID-", size=44)])
    
    sql = f"select fita_id_2 from dupla where fita_id_1 = {self.dic['id']} union "
    sql += f"select fita_id_1 from dupla where fita_id_2 = {self.dic['id']} "
    self.itens = self.model.find_by_sql(sql)
    df = self.itens[0][0] if self.dic['id'] != "" and len(self.itens) > 0 else ""

    sql = f"select * from fita "
    sql += f"where id != {self.dic['id']} "
    sql += f"and filme_id = {self.dic['filme_id']} "
    sql += f"and id not in (select fita_id_1 from dupla) "
    sql += f"and id not in (select fita_id_2 from dupla) "
    self.itens = [item[0] for item in self.model.find_by_sql(sql)]
    content.append([
      sg.Text(text=f"Definir Dupla: ", size=12), 
      sg.Combo([item for item in self.itens], default_value=df, key="-DUPLA_ID-", size=8)])
    return content
  
  def get_params(self, values):
    params = super().get_params(values)
    filme_id = self.model.filme.where(f"where titulo = '{params['filme_id']}'")[0][0]
    params["filme_id"] = filme_id
    return params

  def controller_helper(self, event, values):
    fita_id = values["-DUPLA_ID-"]
    if event == " Salvar " and fita_id == "" or fita_id in self.itens:
      id = values["-ID-"]
      self.error_out(self.model.dupla.delete(f"where fita_id_1 = {id} or fita_id_2 = {id}"))

      if fita_id != "" and self.error == "":
        self.error_out(self.model.dupla.insert({ "fita_id_1": id, "fita_id_2": fita_id }))
      
      if self.error == "":
        self.error = "Fechar"
      