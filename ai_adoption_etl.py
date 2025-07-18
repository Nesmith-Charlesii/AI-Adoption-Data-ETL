import os
import yaml
import pandas as pd

DATA_STORE = "data_store"

class AIAdoptionETL:
    def __init__(self, config_filename = "config.yaml"):
        # Absolute path to this file
        current_file = os.path.abspath(__file__)
        parent_dir = os.path.dirname(current_file)

        # Full path to the config file
        config_path = os.path.abspath(os.path.join(parent_dir, config_filename))

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.datastore_config = self.config.get("ai_adoption_datastore", {})

    def extract(self):
        print(f"Extracting data from data source")
        csv_data = f"{DATA_STORE}/{self.datastore_config.get("file_path")}"
        df = pd.read_csv(csv_data)
        print(f"Extracted {len(df)} records")

ai_adoption_etl = AIAdoptionETL()
ai_adoption_etl.extract()