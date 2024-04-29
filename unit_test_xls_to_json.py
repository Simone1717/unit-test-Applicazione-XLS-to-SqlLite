import unittest
import pandas as pd
import json
import os
from xls_to_json import excel_to_json

class TestXlsToJson(unittest.TestCase):

    def setUp(self):
        # Crea un piccolo DataFrame di esempio da utilizzare per i test
        data = {
            "Pr.": [1, 2],
            "Alunno": ["Mario Rossi", "Luigi Bianchi"],
            "RELIGIONE": [7, 8],
            "LINGUA E LETT.IT": [8, 7]
        }
        self.df = pd.DataFrame(data)
        self.test_excel = "test_data.xlsx"
        self.df.to_excel(self.test_excel, index=False)

    def tearDown(self):
        # Rimuovi il file di test dopo i test
        if os.path.exists(self.test_excel):
            os.remove(self.test_excel)

    def test_excel_to_json(self):
        # Testa la conversione da Excel a JSON
        json_data = excel_to_json(self.test_excel)
        self.assertIsNotNone(json_data, "Il JSON non dovrebbe essere nullo")
        json_dict = json_data.to_dict(orient='records')
        self.assertEqual(len(json_dict), 2, "Dovrebbero esserci 2 record nel JSON")

    def test_file_non_esistente(self):
        # Testa il caso in cui il file Excel non esiste
        json_data = excel_to_json("file_non_esistente.xlsx")
        self.assertIsNone(json_data, "Il JSON dovrebbe essere nullo se il file non esiste")

    def test_colonne_corrette(self):
        # Testa che le colonne siano corrette nel JSON
        json_data = excel_to_json(self.test_excel)
        colonne = list(json_data.columns)
        expected_columns = ["Pr.", "Alunno", "RELIGIONE", "LINGUA E LETT.IT"]
        self.assertEqual(colonne, expected_columns, "Le colonne dovrebbero essere corrette")

if __name__ == "__main__":
    unittest.main()
