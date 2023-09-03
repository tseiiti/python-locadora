from save import sg, Save
from saves.atuar_save import AtuarSave

class AtorSave(Save):
  def add_extra_button(self):
    return sg.Button(" Atuar ") if self.dic["id"] != "" else []
  
  def controller_helper(self, event, values):
    if event == " Atuar ":
      save = AtuarSave()
      save.set_model(self.model)
      save.set_dic(self.dic)
      save.run()
