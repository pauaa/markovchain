import unittest
from markov import generate
from twitter_parser import get_statuses
from parser import Parser
import database


class MarkovTest(unittest.TestCase):
    def test_markov_generate(self):
        assert len(generate(["ipaananen"])) > 0
        assert len(generate(["Vapaavuori"])) > 0
        assert len(generate(["juhasipila"])) > 0
        assert len(generate(["juhasipila", "ipaananen", "Vapaavuori"])) > 0

    def test_twitter(self):
        assert len(get_statuses("ipaananen")) > 0
        assert len(get_statuses("Vapaavuori")) > 0
        assert len(get_statuses("juhasipila")) > 0

    def test_parser_remove_tags(self):
        parser = Parser()
        assert parser.remove_tags("https://t.co/imYXMCjkDz") == ""
        assert parser.remove_tags("http://t.co/imYXMCjkDz") == ""
        assert parser.remove_tags("Hei http://t.co/imYXMCjkDz") == "Hei "
        assert parser.remove_tags("Hei http://t.co/imYXMCjkDz moi") == "Hei  moi"

    def test_parse(self):
        parser = Parser()
        p = parser.parse("Quick brown fox jumps over a lazy dog.")
        assert next(p) == ["^", "quick"]
        assert next(p) == ["quick", "brown"]
        assert next(p) == ["brown", "fox"]
        assert next(p) == ["fox", "jumps"]
        assert next(p) == ["jumps", "over"]
        assert next(p) == ["over", "a"]
        assert next(p) == ["a", "lazy"]
        assert next(p) == ["lazy", "dog."]
        assert next(p) == ["dog.", "$"]

        p = parser.parse("")
        assert next(p) == ["^", "$"]

    def test_database(self):
        database.add(["^", "$"])
        results = database.table.find(first="^")
        for r in results:
            assert r['second'] == "$"
        database.add(["quick", "brown"])
        results = database.table.find(first="quick")
        for r in results:
            assert r['second'] == "brown"

        results = database.table.find(second="brown")
        for r in results:
            assert r['first'] == "quick"

        assert database.find("quick") == "brown"

        d = {"brown": 2, "fox": 2, "jumps": 4, "over": 3, "lazy": 5, "dog": 10}
        database.pick_by_weight(d) in d.keys()


if __name__ == '__main__':
    unittest.main()
