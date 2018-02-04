from sqlalchemy.orm import sessionmaker
from scrapy_spider.models import QuoteDB, db_connect, create_table


class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        quotedb = QuoteDB()
        quotedb.quote = item["quote"]
        quotedb.author = item["author"]

        try:
            session.add(quotedb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
