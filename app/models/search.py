import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.load_json()

    def load_json(self):
        """Lire le fichier JSON et stocker les données."""
        try:
            with open(self.file_path, 'r') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")
        except json.JSONDecodeError:
            print(f"Le fichier {self.file_path} n'est pas un JSON valide.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {e}")

    def get_data(self):
        """Retourne les données JSON."""
        return self.data

#### Exemple d'utilisation
# json_reader = JsonReader('data.json')
# print(json_reader.get_data())
