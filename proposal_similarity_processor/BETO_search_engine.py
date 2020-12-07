import torch
from transformers import BertForMaskedLM, BertTokenizer

from proposal_similarity_processor.abstract_search_engine import AbstractSearchEngine


text = '''Movilidad Segura y Educación para la Convivencia Vial
--
Problema: - OMS estima que al 2020, los siniestros viales serán la 3° causa de muerte a nivel mundial 
- En Chile, mueren 5 personas al día por esta causa. Esto corresponde a un costo del 2% del PIB. 
- Año 2016, 1.675 fallecidos, cifra más alta de los últimos 8 años (2.178 con ajuste OMS) y más de 63.000 lesionados de diversa índole. 
- Somos el país con la peor tasa de fallecidos por habitante de la OCDE
- Principales afectados: usuarios vulnerables (peatones, ciclistas, motociclistas) 52% de los fallecidos 
- Principales causas: Imprudencias (47%), Velocidad/pérdida de control vehículo (32%), alcohol (13%). 
- Siniestros viales son 1° causa de muerte en niños de 1 a 14 años y en adolescentes de 15 a 29 años. 
- Tasa de fallecidos de Chile (9,21 fallecidos/100.000 habitante), la peor de los países OCDE. 
- Víctimas “indirectas” (familiares)  no reciben apoyo ni orientación administrativa y/o sicológica cuando estos hechos ocurren.
Solución: Como Fundación Conciencia Vial y en conjunto con otras organizaciones y agrupaciones de familiares de víctimas que conforman OSEV (Organizaciones Ciudadanas por la Seguridad Vial), se definen las siguientes propuestas como relevantes para abordar este tema, para lograr instaurar la seguridad vial como un atributo, y reducir así las nefastas cifras existentes:

PROPUESTA 1
Abordar la Seguridad Vial como una política de Estado, asignando recursos acordes y robusteciendo la actual institucionalidad. Que el próximo gobierno considere como punto de partida la Nueva Política Nacional de Seguridad de Tránsito, trabajada con fuerte participación de la sociedad civil.

PROPUESTA 2
Instaurar educación formal para la convivencia vial, a todo nivel, comenzando con los más pequeños, para incidir en cambios de hábitos y culturales, y hasta la etapa adulta (reeducación constante, aprovechando la instancia de renovación de licencias de conducir, y a través de capacitaciones en empresas). Promover también la educación a través de campañas de concientización, periódicas y diseñadas/orientadas a distintos grupos de la población y abordando diversas temáticas (velocidad, distracciones por celular, alcohol, etc.) 

PROPUESTA 3
Fortalecer la fiscalización orientada a conductas de riesgo. Eficiente control de excesos de velocidad u otras infracciones críticas en puntos de alto riesgo, mediante el uso de leyes actualmente vigentes, adecuando normativas para hacer uso de tecnologías que permitan automatizar esto (fotorradares, cámaras fijas, TAG) y reasignando los recursos existentes. La idea es poner el foco en la prevención de accidentes y no en la sanción o recaudación. 

PROPUESTA 4
Instaurar un protocolo integral de emergencias para todas las victimas (directas/indirectas) que dejan los siniestros viales en Chile.
Clasificación: transporte'''

class BETOSearchEngine(AbstractSearchEngine):
    def __init__(self):
        super().__init__()
        self.tokenizer = BertTokenizer.from_pretrained("pytorch/", do_lower_case=False)
        self.model = BertForMaskedLM.from_pretrained("pytorch/")

    def get_tensor_of_entire_text(self, text):
        phrases = text.split('/n')
        list_of_tensors = []
        for phrase in phrases:
            tensor = self.get_entire_phrase_vectorized(phrase)
            list_of_tensors.append(tensor)
        return torch.stack(list_of_tensors)[0][0].mean(0)

    def get_entire_phrase_vectorized(self, phrase):
        phrase = phrase[0:2310]
        tokens = self.tokenizer.tokenize(phrase)
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokens)
        tokens_tensor = torch.tensor([indexed_tokens])
        predictions = self.model(tokens_tensor)[0]
        return predictions[0].mean(0)

    def vectorize(self, text):
        all_words = self.get_entire_phrase_vectorized(text)
        return all_words.detach().numpy()


