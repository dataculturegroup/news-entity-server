import unittest
import helpers.custom.dates as dates
from helpers import SPANISH, ENGLISH, PORTUGUESE

test_string_es = """Hoy es 8/3/21, lunes. el mes es marzo, el próximo mes es abril 
    y más tarde hay septiembre, noviembre y diciembre. Algunas abreviaturas son 
    sep., Oct., Nov., nov., jul., ago, etc. Mis amigos tienen 22 y 24 años."""

test_string_pt = """Hoje é 08/03/21, segunda. o mês é março, próximo mês é abril 
    e depois há setembro, novembro e dezembro. Algumas abreviações são
    set., Out., Nov., nov., jul., ago, etc. Meus amigos têm 22 e 24 anos."""

# https://www.sandiegouniontribune.com/en-espanol/noticias/story/2021-03-08/papa-francisco-visitaria-capital-de-hungria-en-septiembre
test_string_es_2 = """BUDAPEST, Hungría —  BUDAPEST, Hungría (AP) — El papa Francisco viajará a la capital de Hungría 
    en septiembre, donde participará en la misa de clausura de un encuentro internacional católico de varios días, de 
    acuerdo con el cardenal de la Iglesia católica del país europeo."""


class TestCustomDateExtraction(unittest.TestCase):

    def test_extract_dates_es_short(self):
        results = dates.extract_dates(test_string_es_2, SPANISH)
        assert len(results) == 1
        assert results[0]['text'] == 'septiembre'

    def test_extract_dates_es_long(self):
        results = dates.extract_dates(test_string_es, SPANISH)
        results = sorted(results, key=lambda k: k['start_char'])
        assert len(results) == 12
        assert results[0]['text'] == '8/3/21'
        assert results[11]['text'] == 'jul.'

    def test_extract_dates_pt_long(self):
        results = dates.extract_dates(test_string_pt, PORTUGUESE)
        results = sorted(results, key=lambda k: k['start_char'])
        assert len(results) == 12
        assert results[0]['text'] == '08/03/21'
        assert results[11]['text'] == 'jul.'

    def test_extract_dates_en(self):
        results = dates.extract_dates("This happend on 8/3/21", ENGLISH)
        assert len(results) == 0


if __name__ == "__main__":
    unittest.main()
