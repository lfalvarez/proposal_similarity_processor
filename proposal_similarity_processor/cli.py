"""Console script for proposal_similarity_processor."""
import argparse
import sys
import json
import csv

formato_propuesta = '''{solution_at_the_end}'''
'''
Buscando 537
['537', '393', '103', '399', '401']
Buscando 537
['537', '393', '103', '399', '401']
Buscando 306
['306', '311', '385', '48', '533']

'''
def main():
    """Console script for proposal_similarity_processor."""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs=1)
    args = parser.parse_args()

    filename = args.filename[0]
    keys = sorted(['causes', 'clasification', 'problem', 'solution', 'solution_at_the_end', 'terms_and_conditions', 'title', 'when'])
    other_keys = sorted(['causes', 'clasification', 'problem', 'solution_at_the_end', 'terms_and_conditions', 'title', 'when'])
    with_one_liner = sorted(['causes', 'clasification', 'one_liner', 'problem', 'solution_at_the_end', 'terms_and_conditions', 'title', 'when'])
    ids_que_si_corresponden = []
    para_ser_guardado_en_un_csv = []
    with open(filename) as infile:
        data = json.load(infile)
        for result in data['results']:
            data_keys = sorted(list(result['data'].keys()))
            if data_keys in [keys, other_keys, with_one_liner]:
                ids_que_si_corresponden.append(result['id'])
                r = formato_propuesta.format(**result['data'])
                para_ser_guardado_en_un_csv.append([result['id'], r])

    with open('info_votainteligente.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(para_ser_guardado_en_un_csv)
        csvfile.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
