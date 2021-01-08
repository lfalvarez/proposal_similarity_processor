"""Console script for proposal_similarity_processor."""
import argparse
import cmd
import sys
import csv

from proposal_similarity_processor.document import Document
from proposal_similarity_processor.similarity_searcher import SimilaritySearcher
from proposal_similarity_processor.BETO_search_engine import BETOSearchEngine


def get_searcher():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs=1)
    args = parser.parse_args()

    filename = args.filename[0]
    docs = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            id = row[0]
            content = row[1]
            doc = Document(id,content)
            docs.append(doc)
    print('inicializando...')
    searcher = SimilaritySearcher(BETOSearchEngine)
    print('Listo')
    for doc in docs:
        try:
            searcher.add_document(doc)
            print('Parseado documento con id {id}'.format(id=doc.id))
        except Exception as e:
            print(e)
            print('Ocurrió un error con el doc que tiene contenido', doc.id)
    print('agregué todos los docs')
    return searcher

class Shell(cmd.Cmd):
    intro = 'Hola!.  Type help or ? to list commands.\n'
    prompt = '(psp) '
    file = None

    def __init__(self, searcher):
        super().__init__()
        self.searcher = searcher

    def do_search(self, id:int):
        print('Buscando {text}'.format(text=id))
        docs = self.searcher.get_closest_doc(id, 5)
        print(docs)
        ##print('el más cercano es el que tiene id {id} y contenido {content}'.format(id=doc.id, content=doc.content))


if __name__ == "__main__":
    searcher = get_searcher()
    Shell(searcher).cmdloop()
