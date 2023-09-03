from app import sg, App

class AtuarSave(App):
  def view(self):
    table = self.gen_table(self.add_extra_sql(), self.model.columns())
    
    layout = [
      [self.titulo(f"{self.model.tname} {self.dic['nome_real']}")], 
      [sg.HorizontalSeparator()], 
      [sg.Text(text="Filme: ", size=12), sg.Combo([flm[1] for flm in self.model.filme.select()], key="-FILME_ID-", size=44)], 
      [sg.Text(text="Personagem: ", size=12), sg.Input(default_text="", key="-PERSONAGEM-")], 
      [sg.Text(text="Estrela: ", size=12), sg.Checkbox(text="", key="-ESTRELA-")], 
      [sg.Button(" Atuar "), sg.Text("(Para excluir uma atuação clique no título abaixo)", font=("Arial", 11))], 
      [table], 
      [sg.Text(key="-SAIDA-")], 
      [sg.Button(" Voltar ")]]
    
    self.window = sg.Window("Atuar", layout, resizable=True)
  
  def controller(self, event, values):
    if event == " Atuar " and not (values["-FILME_ID-"] == "" or values["-PERSONAGEM-"] == ""):
      filme_id = self.model.filme.where(f"where titulo = '{values['-FILME_ID-']}'")[0][0]
      params = {
        "filme_id": filme_id, 
        "ator_id": self.dic["id"], 
        "personagem": values["-PERSONAGEM-"], 
        "estrela": values["-ESTRELA-"]
      }
      self.error_out(self.model.atuar.insert(params))
      if self.error == "":
        self.window["-TABLE-"].update(values=self.add_extra_sql())
        self.window["-FILME_ID-"].update(value="")
        self.window["-PERSONAGEM-"].update(value="")
        self.window["-ESTRELA-"].update(value=False)

    elif "+CLICKED+" in event and event[2][0] is not None:
      layout = [
        [sg.Text("Tem certeza que deseja excluir esse registro?")], 
        [sg.Button(" Sim "), sg.Button(" Não ")]]
      if sg.Window("Confirme", layout).read(close=True)[0] == " Sim ":
        filme_id = self.model.filme.where(f"where titulo = '{self.add_extra_sql()[event[2][0]][0]}'")[0][0]
        self.error_out(self.model.atuar.delete(f"where filme_id = {filme_id} and ator_id = {self.dic['id']}"))
        if self.error == "":
          self.window["-TABLE-"].update(values=self.add_extra_sql())

  def add_extra_sql(self):
    sql = "select filme.titulo, atuar.personagem, atuar.estrela "
    sql += "from atuar "
    sql += "join filme on filme.id = atuar.filme_id "
    sql += f"where ator_id = {self.dic['id']}"
    return self.model.find_by_sql(sql)
  