
import pandas as pd
from pathlib import Path
import json


# def dump_to_table(table_name):
#     engine = create_engine(
#     'postgresql+psycopg2://username:password@host:port/database')

#     # Drop old table and create new empty table
#     df.head(0).to_sql('table_name', engine, if_exists='replace',index=False)

#     conn = engine.raw_connection()
#     cur = conn.cursor()
#     output = io.StringIO()
#     df.to_csv(output, sep='\t', header=False, index=False)
#     output.seek(0)
#     contents = output.getvalue()
#     cur.copy_from(output, 'table_name', null="") # null values become ''
#     conn.commit()
#     cur.close()
#     conn.close()




class EDumper:
    def __init__(self, basedir, session, params=None):
        self.basedir = basedir
        self.session = session
        self.workdir = f"{self.basedir}/{self.session}"

        Path(self.basedir).mkdir(exist_ok=True, parents=True)
        Path(self.workdir).mkdir(exist_ok=True)
        print(f"Dumper working in {self.workdir}")


    def dump_indicators(self, ticker: str, df_indi: pd.DataFrame):
        filename = f"indi_{ticker}.csv"
        filepath = Path(self.workdir) / filename
        csv_path = str(filepath)
        df_indi.to_csv(csv_path, sep=',')

    def dump_article_yaml(self, article_info):
        # sha_id = sha256(article_info['content'].encode('utf-8')).hexdigest()
        # filename = f"{sha_id}.json"
        filename = f"senti_ALL.list.yaml"
        filepath = Path(self.workdir) / filename
        item =  json.dumps(article_info)
        line_item = f"- {item}\n"
        with open(filepath, "a") as fd:
            fd.write(line_item)   
 
    def dump_sentiment_analysis(self, news_sentiments, company="", ticker=""):
        from hashlib import sha256
        print(f"ESentiment analysis for {company}: {ticker}")
        for article_info in news_sentiments:
            # article_info = dict()
            # article_info['title'] = str(article)
            article_info['sha_id'] = sha256(article_info['title'].encode('utf-8')).hexdigest()
            # article_info.update(**info)
            self.dump_article_yaml(article_info)

__dumper_store = []    

def get_EDumper() -> EDumper:
    if not __dumper_store:
        __dumper_store.append(EDumper("__output/drumper", "att"))
    return __dumper_store[0]
