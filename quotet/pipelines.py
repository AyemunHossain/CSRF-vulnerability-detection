from itemadapter import ItemAdapter
import sqlite3

class QuotetPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def create_connection(self):
        self.conn = sqlite3.connect("myqutes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""
                          DROP TABLE IF EXISTS qutes
                          """)

        self.curr.execute("""
                          CREATE TABLE qutes(
                              title text,
                              author text,
                              tag text)
                          """)

    def store_db(self,item):
        self.curr.execute("""
                    INSERT INTO qutes VALUES(?,?,?)""",(item['title'][0],
                                                       item['author'][0],
                                                        ",".join(item['tag']))
                    )
        self.conn.commit()