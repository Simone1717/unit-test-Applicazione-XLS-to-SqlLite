import unittest
import json
import sqlite3
from json_to_sqlite3 import create_studenti_table, populate_studenti_table, get_studenti_con_debito

class TestJsonToSqlite3(unittest.TestCase):

    def setUp(self):
        # Crea un database SQLite3 di test
        self.db_name = "test_studenti.db"
        self.conn = sqlite3.connect(self.db_name)
        create_studenti_table(self.conn)

        # Crea dati JSON di test
        self.test_json_data = [
            {
                "Alunno": "Mario Rossi",
                "RELIGIONE": 7,
                "LINGUA E LETT.IT": 8,
                "LINGUA INGLESE": 7,
                "STORIA": 6,
                "EDUCAZIONE CIVICA": 8,
                "MATEMATICA": 7,
                "DIRITTO ED ECONOMIA": 6,
                "FISICA": 6,
                "CHIMICA": 7,
                "Tecn.informatiche": 8,
                "Tecn.e Tecn.di rappr": 6,
                "SC.DELLA TERRA/GEO": 6,
                "SCIENZE MOT. E SPORT": 8,
                "COMPORTAMENTO": 8,
                "Media": 7.1,
                "Esito": "Promosso"
            }
        ]

    def tearDown(self):
        # Rimuovi il database di test
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_creazione_tabella(self):
        # Verifica che la tabella sia stata creata correttamente
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='studenti'")
        self.assertIsNotNone(cursor.fetchone(), "La tabella 'studenti' dovrebbe esistere")

    def test_popolamento_tabella(self):
        # Verifica che la tabella sia stata popolata con i dati corretti
        populate_studenti_table(self.conn, self.test_json_data)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM studenti")
        result = cursor.fetchall()
        self.assertEqual(len(result), 1, "Dovrebbe esserci 1 record nella tabella")
        self.assertEqual(result[0][1], "Mario Rossi", "Il nome dello studente dovrebbe essere 'Mario Rossi'")

    def test_query_studenti_con_debito(self):
        # Verifica che la query per studenti con debito funzioni correttamente
        self.test_json_data[0]["Esito"] = "Sospensione del giudizio"
        populate_studenti_table(self.conn, self.test_json_data)
        studenti_con_debito = get_studenti_con_debito(self.conn)
        self.assertEqual(len(studenti_con_debito), 1, "Ci dovrebbe essere 1 studente con debito")
        self.assertEqual(studenti_con_debito[0][0], "Mario Rossi", "Il nome dello studente con debito dovrebbe essere 'Mario Rossi'")

if __name__ == "__main__":
    unittest.main()
