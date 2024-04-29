import unittest
import json
from convertiStringheJson import converti_stringhe_json

class TestConvertiStringheJson(unittest.TestCase):

    def setUp(self):
        # Crea un file JSON di test
        data = [
            {
                "Unnamed: 0": 1,
                "Unnamed: 1": "Mario Rossi",
                "Unnamed: 10": 7,
                "Unnamed: 11": 8,
                "Unnamed: 12": 7,
                "Unnamed: 2": "",
                "Unnamed: 3": "",
                "Unnamed: 25": "",
                "Unnamed: 26": "",
                "Media": 7.5,
                "Esito": "Promosso"
            }
        ]
        self.test_json = "test_studenti.json"
        with open(self.test_json, "w") as f:
            json.dump(data, f, indent=4)

    def tearDown(self):
        # Rimuovi il file JSON di test
        if os.path.exists(self.test_json):
            os.remove(self.test_json)

    def test_rinomina_chiavi(self):
        # Testa la rinomina delle chiavi
        data = converti_stringhe_json(self.test_json)
        chiavi = list(data[0].keys())
        expected_keys = ["Pr", "Alunno", "RELIGIONE", "LINGUA E LETT.IT", "LINGUA INGLESE"]
        self.assertEqual(chiavi[:5], expected_keys, "Le chiavi dovrebbero essere rinominate correttamente")

    def test_rimozione_colonne_vuote(self):
        # Testa la rimozione delle colonne vuote
        data = converti_stringhe_json(self.test_json)
        chiavi = list(data[0].keys())
        colonne_non_vuote = ["Pr", "Alunno", "RELIGIONE", "LINGUA E LETT.IT", "LINGUA INGLESE", "Media", "Esito"]
        self.assertEqual(chiavi, colonne_non_vuote, "Le colonne vuote dovrebbero essere rimosse")

if __name__ == "__main__":
    unittest.main()
