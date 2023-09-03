from app import sg, App

class Save(App):
  def view(self):
    content = self.get_content()
    
    layout = [
      [self.titulo(f"{'Criar' if self.dic['id'] == '' else 'Atualizar'} {self.model.tname}")], 
      [sg.HorizontalSeparator()], 
      *content, 
      [sg.HorizontalSeparator()], 
      [sg.Text(key="-SAIDA-")], 
      [sg.Button(" Voltar "), sg.Button(" Salvar "), 
      self.add_extra_button()]]
    
    self.window = sg.Window(self.model.tname, layout, resizable=True)
    
  def controller(self, event, values):
    if event == " Salvar ":
      params = self.get_params(values)
      if self.dic["id"] == "":
        self.error_out(self.model.insert(params))
      else:
        self.error_out(self.model.update(params))

      if self.error == "":
        self.error = "Fechar"
      
    self.controller_helper(event, values)

  def get_content(self):
    return [[
      sg.Text(text=f"{k.capitalize()}: ", size=12), 
      sg.Input(default_text=v, key=f"-{k.upper()}-", disabled=(k=="id"))]
      for k, v in self.dic.items()]

  def get_params(self, values):
    return {
      str(key).replace("-", "").lower(): val 
      for key, val in values.items() 
      if str(key).replace("-", "").lower() in self.dic.keys()
    }

  def add_extra_button(self):
    return []
  
  def controller_helper(self, event, values):
    print()



if __name__ == "__main__":
  from model import Model
  model = Model("Categoria")
  save = Save()
  save.set_model(model)
  save.set_dic(model.find(1))
  save.run()
