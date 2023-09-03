from app import sg, App

class Read(App):
  def __init__(self, model, save):
    self.model = model
    self.save = save
    self.save.set_model(self.model)

  def view(self):
    self.set_cols_rows()
    
    layout = [
      [self.titulo(f"Lista de {self.model.tname}s")], 
      [self.gen_table(self.rows, self.cols)], 
      [sg.Button(" Voltar "), sg.Button(" Novo ")]]
    
    self.window = sg.Window(self.model.tname, layout, size=(800, 320), resizable=True)
    
  def controller(self, event, values):
    if event == " Novo ":
      self.edit(0)

    elif "+CLICKED+" in event and event[2][0] is not None:
      self.edit(self.rows[event[2][0]][0])

  def set_cols_rows(self):
    self.rows = self.model.select()
    self.cols = self.model.columns()
  
  def edit(self, id):
    self.save.set_dic(self.model.find(id))
    self.save.run()
    self.set_cols_rows()
    self.window["-TABLE-"].update(values=self.rows)



if __name__ == "__main__":
  from model import Model
  from save import Save
  Read(Model("Categoria"), Save()).run()
