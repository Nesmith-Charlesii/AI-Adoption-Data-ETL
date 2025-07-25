import os
import yaml
import pandas as pd

DATA_STORE = "data_store"

class AIAdoptionETL:
    def __init__(self, config_filename="config.yaml"):
        # Get absolute path to this script and config
        current_file = os.path.abspath(__file__)
        parent_dir = os.path.dirname(current_file)
        config_path = os.path.abspath(os.path.join(parent_dir, config_filename))

        # Load config
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.datastore_config = self.config.get("ai_adoption_datastore", {})
        self.file_path = os.path.join(DATA_STORE, self.datastore_config.get("file_path", ""))
        self.file_type = self.datastore_config.get("file_type", "csv")
        self.sort_by = self.datastore_config.get("sort_by", None)

        # Get output dir from config or default
        output_dir_name = self.datastore_config.get("output_dir", "separated_industries")
        self.output_dir = os.path.join(parent_dir, output_dir_name)
        os.makedirs(self.output_dir, exist_ok=True)

    def extract(self):
        print(f"📤 Extracting data from: {self.file_path}")
        if self.file_type != "csv":
            raise ValueError(f"Unsupported file type: {self.file_type}")
        df = pd.read_csv(self.file_path)
        print(f"✅ Extracted {len(df)} records.")
        return df

    def transform(self, df):
        print("🔧 Transforming data by 'industry'...")

        if "industry" not in df.columns:
            raise KeyError("❌ Column 'industry' not found in the dataset.")

        df = df.dropna(subset=["industry"])

        if self.sort_by and self.sort_by in df.columns:
            df = df.sort_values(by=self.sort_by)

        industry_dfs = {industry: group for industry, group in df.groupby("industry")}
        print(f"✅ Split into {len(industry_dfs)} industry groups.")
        return industry_dfs

    def load(self, industry_dfs):
        print(f"💾 Saving files to: {self.output_dir}")
        for industry, data in industry_dfs.items():
            sanitized = industry.replace("/", "_").replace(" ", "_").replace("\\", "_")
            filename = f"{sanitized}.csv"
            path = os.path.join(self.output_dir, filename)
            data.to_csv(path, index=False)
            print(f"📁 Saved {len(data)} rows to {filename}")

    def run(self):
        df = self.extract()
        industry_dfs = self.transform(df)
        self.load(industry_dfs)

# Entry point
if __name__ == "__main__":
    etl = AIAdoptionETL()
    etl.run()
