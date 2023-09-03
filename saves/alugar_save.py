from app import sg, App

class AlugarSave(App):
  def view(self):
    table = self.gen_table(self.add_extra_sql(), self.model.columns())
    layout = [
      [self.titulo(f"{self.model.tname} {self.dic['nome'].capitalize()} {self.dic['sobrenome'].capitalize()}")], 
      [sg.HorizontalSeparator()], 
      [sg.Text(text="Fita: ", size=12), sg.Combo([flm[0] for flm in self.add_extra_sql_2()], key="-FITA_ID-", size=44)], 
      [sg.Button(" Alugar "), sg.Text("(Para excluir um aluguel clique no título abaixo)", font=("Arial", 11))], 
      [table], 
      [sg.Text(key="-SAIDA-")], 
      [sg.Button(" Voltar ")]]
    
    self.window = sg.Window("Alugar", layout, resizable=True)
  
  def controller(self, event, values):
    if event == " Alugar " and not values["-FITA_ID-"] == "":
      fita_id = int(values['-FITA_ID-'].split(' - ')[0])
      params = {
        "fita_id": fita_id, 
        "cliente_id": self.dic["id"]
      }
      self.error_out(self.model.alugar.insert(params))
      if self.error == "":
        self.window["-TABLE-"].update(values=self.add_extra_sql())
        self.window["-FITA_ID-"].update(values=[flm[0] for flm in self.add_extra_sql_2()])

    elif "+CLICKED+" in event and event[2][0] is not None:
      layout = [
        [sg.Text("Tem certeza que deseja excluir esse registro?")], 
        [sg.Button(" Sim "), sg.Button(" Não ")]]
      if sg.Window("Confirme", layout).read(close=True)[0] == " Sim ":
        fita_id = self.add_extra_sql()[event[2][0]][0]
        self.error_out(self.model.alugar.delete(f"where fita_id = {fita_id} and cliente_id = {self.dic['id']}"))
        if self.error == "":
          self.window["-TABLE-"].update(values=self.add_extra_sql())
          self.window["-FITA_ID-"].update(values=[flm[0] for flm in self.add_extra_sql_2()])

  def add_extra_sql(self):
    sql  = "select alugar.fita_id, filme.titulo, "
    sql += "case when dupla_1.fita_id_1 is not null then 'Fita 1' "
    sql += "when dupla_2.fita_id_2 is not null then 'Fita 2' "
    sql += "else 'Simples' end tipo "
    sql += "from alugar "
    sql += "join fita on fita.id = alugar.fita_id "
    sql += "join filme on filme.id = fita.filme_id "
    sql += "left join dupla dupla_1 on dupla_1.fita_id_1 = fita.id "
    sql += "left join dupla dupla_2 on dupla_2.fita_id_2 = fita.id "
    sql += f"where alugar.cliente_id = {self.dic['id']} "
    sql += "order by 1 "
    return self.model.find_by_sql(sql)

  def add_extra_sql_2(self):
    sql  = "select concat(fita.id, ' - ', filme.titulo) "
    sql += "from fita "
    sql += "join filme on filme.id = fita.filme_id "
    sql += "where fita.id not in (select fita_id from alugar) "
    sql += "order by fita.id "
    return self.model.find_by_sql(sql)
  