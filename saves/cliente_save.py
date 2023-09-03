from save import sg, Save
from saves.alugar_save import AlugarSave

class ClienteSave(Save):
  def add_extra_button(self):
    return sg.Button(" Alugar ") if self.dic["id"] != "" else []
  
  def controller_helper(self, event, values):
    if event == " Alugar ":
      save = AlugarSave()
      save.set_model(self.model)
      save.set_dic(self.dic)
      save.run()
