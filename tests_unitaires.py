import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from io import StringIO
from main import InventoryManager


class TestInventoryManager(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_load_success(self, mock_read_csv):
        """Test si les fichiers CSV sont correctement chargés dans l'inventaire."""
        # Mock des données CSV
        mock_data = pd.DataFrame({
            'category': ['A', 'B', 'A'],
            'quantity': [10, 20, 30],
            'unit_price': [5.0, 10.0, 15.0]
        })
        mock_read_csv.return_value = mock_data

        # Initialisation du gestionnaire
        manager = InventoryManager()
        directory = 'fake_directory'

        # Simulation des fichiers CSV dans le dossier
        with patch('os.listdir', return_value=['file1.csv', 'file2.csv']), \
             patch('os.path.isdir', return_value=True), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_load(directory)
            output = mock_stdout.getvalue()

        self.assertFalse(manager.inventory.empty)
        self.assertEqual(manager.inventory.shape[0], 6)  # 2 fichiers chargés de 3 lignes chacun
        self.assertIn("Loaded: file1.csv", output)
        self.assertIn("All CSV files have been consolidated.", output)

    @patch('os.listdir', return_value=[])
    @patch('os.path.isdir', return_value=True)
    def test_load_no_csv_files(self, mock_isdir, mock_listdir):
        """Test si la fonction renvoie une erreur quand il n'y a pas de fichiers CSV."""
        manager = InventoryManager()
        directory = 'empty_directory'

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_load(directory)
            output = mock_stdout.getvalue()

        self.assertIn("No CSV files found in the folder.", output)

    def test_search_existing_data(self):
        """Test de la recherche de données existantes dans l'inventaire."""
        manager = InventoryManager()
        manager.inventory = pd.DataFrame({
            'category': ['A', 'B', 'A'],
            'quantity': [10, 20, 30],
            'unit_price': [5.0, 10.0, 15.0]
        })

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_search('category=A')
            output = mock_stdout.getvalue()
            self.assertIn('A', output)
            self.assertIn('10', output)
            self.assertIn('30', output)

    def test_search_no_results(self):
        """Test si la recherche ne renvoie aucun résultat."""
        manager = InventoryManager()
        manager.inventory = pd.DataFrame({
            'category': ['A', 'B', 'A'],
            'quantity': [10, 20, 30]
        })

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_search('category=Z')
            output = mock_stdout.getvalue()
            self.assertIn("No results found.", output)

    def test_summary_success(self):
        """Test de la génération d'un rapport résumé."""
        manager = InventoryManager()
        manager.inventory = pd.DataFrame({
            'category': ['A', 'B', 'A'],
            'quantity': [10, 20, 30],
            'unit_price': [5.0, 10.0, 15.0]
        })

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, \
             patch('pandas.DataFrame.to_csv') as mock_to_csv:
            manager.do_summary('test_summary.csv')
            output = mock_stdout.getvalue()

        self.assertIn('Summary report exported to test_summary.csv.', output)
        mock_to_csv.assert_called_once_with('test_summary.csv')

    def test_show_success(self):
        """Test de l'affichage des premières lignes de l'inventaire."""
        manager = InventoryManager()
        manager.inventory = pd.DataFrame({
            'category': ['A', 'B', 'C'],
            'quantity': [10, 20, 30],
            'unit_price': [5.0, 10.0, 15.0]
        })

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_show('2')
            output = mock_stdout.getvalue()
            self.assertIn('A', output)
            self.assertIn('B', output)
            self.assertNotIn('C', output)

    def test_show_invalid_number(self):
        """Test si la fonction renvoie une erreur pour un nombre invalide."""
        manager = InventoryManager()
        manager.inventory = pd.DataFrame({
            'category': ['A', 'B'],
            'quantity': [10, 20]
        })

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            manager.do_show('invalid')
            output = mock_stdout.getvalue()
            self.assertIn("Please provide a valid number", output)


if __name__ == '__main__':
    unittest.main()
