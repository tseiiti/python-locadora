from read import Read

class FilmeRead(Read):
  def set_cols_rows(self):
    sql = "select "
    sql += "filme.id, filme.titulo, categoria.nome as categoria "
    sql += "from filme "
    sql += "join categoria on categoria.id = filme.categoria_id "
    sql += "order by 1 "
    self.rows = self.model.find_by_sql(sql)
    self.cols = self.model.columns()
    