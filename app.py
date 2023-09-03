import PySimpleGUI as sg

class App:
  def view(self):
    pass
  
  def controller(self, event, values):
    pass
  
  def run(self):
    sg.set_options(font=("Arial", 12))
    self.view()
    self.error = ""

    while True:
      event, values = self.window.read()
      print(type(self).__name__ + ":", event, values)

      if event == " Voltar " or event == sg.WIN_CLOSED:
        break

      self.controller(event, values)

      if self.error == "Fechar":
        break

    self.window.close()
  
  def titulo(self, text):
    return sg.Text(
      text=text, 
      font=("Arial Bold", 16), 
      size=16, 
      expand_x=True, 
      justification="center"
    )

  def gen_dict(self, keys, values=None):
    dic = {}
    for i in range(len(keys)):
      dic[keys[i]] = values[i] if values else ""
    return dic
  
  def gen_table(self, values, headings):
    return sg.Table(
      values=values, 
      headings=headings,
      auto_size_columns=True,
      display_row_numbers=False,
      justification="center", 
      key="-TABLE-",
      selected_row_colors="black on gray",
      enable_events=True,
      expand_x=True,
      expand_y=False,
      enable_click_events=True)
  
  def error_out(self, error):
    if error != "":
      self.window["-SAIDA-"].update(error)
    self.error = error

  def set_model(self, model):
    if model:
      self.model = model
  
  def set_dic(self, dic):
    if dic:
      self.dic = dic
  