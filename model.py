import psycopg2
from db_conf import db
from app import App

class Model:
  def __init__(self, tname=None):
    self.tname = type(self).__name__.replace("Model", "") if tname is None else tname
  
  def find(self, id):
    rows = self.exec(self.sel, f"where id = {id}")
    if self.error == "":
      rows = rows[0] if rows else None
      return App().gen_dict(self.cols, rows)
    else:
      return self.error

  def select(self):
    return self.exec(self.sel)
  
  def where(self, params):
    return self.exec(self.sel, params)

  def insert(self, params):
    return self.exec(self.ins, params)

  def update(self, params):
    return self.exec(self.upd, params)

  def delete(self, params):
    return self.exec(self.dlt, params)

  def columns(self):
    return self.exec(self.col)

  def find_by_sql(self, params):
    return self.exec(self.fnd, params)

  def conn(self):
    self.con = psycopg2.connect(
      database = db["database"],
      user = db["user"],
      password = db["password"],
      host = db["host"],
      port = db["port"])
    self.cur = self.con.cursor()
  
  def exec(self, func, params=None):
    try:
      self.conn()
      self.params = params
      self.error = ""
      return func()
      
    except (Exception, psycopg2.Error) as error:
      print("Error:", error)
      self.error = error
      return error

    finally:
      print("SQL:", self.sql)
      if self.cur:
        self.cur.close()
      if self.con:
        self.con.close()

  def sel(self):
    self.sql = f"select * from {self.tname.lower()} {str(self.params or '')} order by 1"
    self.cur.execute(self.sql)
    self.cols = [dsc[0] for dsc in self.cur.description]
    return self.cur.fetchall()

  def ins(self):
    col = ", ".join(k for k in self.params.keys() if k != "id")
    val = ", ".join(f"'{v}'" for k, v in self.params.items() if k != "id")
    self.sql = f"insert into {self.tname.lower()} ({col}) values ({val})"
    self.cur.execute(self.sql)
    self.con.commit()
    return ""

  def upd(self):
    aux = ", ".join(f"{k} = '{v}'" for k, v in self.params.items() if k != "id")
    self.sql = f"update {self.tname.lower()} set {aux} where id = {self.params['id']}"
    self.cur.execute(self.sql)
    self.con.commit()
    return ""

  def dlt(self):
    self.sql = f"delete from {self.tname.lower()} {str(self.params)}"
    self.cur.execute(self.sql)
    self.con.commit()
    return ""

  def col(self):
    if not self.sql:
      self.sql = f"select * from {self.tname.lower()} limit 0"
      self.cur.execute(self.sql)
      self.cols = [dsc[0] for dsc in self.cur.description]
    return self.cols

  def fnd(self):
    self.sql = self.params
    self.cur.execute(self.sql)
    self.cols = [dsc[0] for dsc in self.cur.description]
    return self.cur.fetchall()
