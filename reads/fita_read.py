from read import Read

class FitaRead(Read):
  def set_cols_rows(self):
    sql = "select "
    sql += "fita.id, filme.titulo, "
    sql += "coalesce(nullif(concat('Dupla com ', coalesce(dupla_1.fita_id_2, dupla_2.fita_id_1, 0)), 'Dupla com 0'), 'Simples') tipo "
    sql += "from fita "
    sql += "join filme on filme.id = fita.filme_id "
    sql += "left join dupla dupla_1 on dupla_1.fita_id_1 = fita.id "
    sql += "left join dupla dupla_2 on dupla_2.fita_id_2 = fita.id "
    sql += "order by 1 "
    self.rows = self.model.find_by_sql(sql)
    self.cols = self.model.columns()
    