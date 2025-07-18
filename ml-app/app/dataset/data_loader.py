
import os
import requests

from typing import List, Tuple

from PIL import Image
from io import BytesIO

class DatasetLoader:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.create_directories()
    
    def create_directories(self):
        os.makedirs(f"{self.data_dir}/train/dogs", exist_ok=True)
        os.makedirs(f"{self.data_dir}/train/cats", exist_ok=True)
        os.makedirs(f"{self.data_dir}/test/dogs", exist_ok=True)
        os.makedirs(f"{self.data_dir}/test/cats", exist_ok=True)
    
    def load_sample_images(self) -> List[Tuple[str, str]]:
        """Load sample images for demo purposes"""
        sample_urls = [
            ("https://example.com/dog1.jpg", "dogs"),
            ("https://example.com/cat1.jpg", "cats"),
        ]
        
        loaded_images = []
        for url, label in sample_urls:
            try:
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                filename = f"sample_{label}_{len(loaded_images)}.jpg"
                image.save(f"{self.data_dir}/train/{label}/{filename}")
                loaded_images.append((filename, label))
            except Exception as e:
                print(f"Failed to load {url}: {e}")
        
        return loaded_images
    
    def get_dataset_stats(self) -> dict:
        """Get statistics about the dataset"""
        stats = {
            "train" : {"dogs": 0, "cats": 0},
            "test"  : {"dogs": 0, "cats": 0}
        }
        
        for split in ["train", "test"]:
            for class_name in ["dogs", "cats"]:
                path = f"{self.data_dir}/{split}/{class_name}"
                if os.path.exists(path):
                    stats[split][class_name] = len(os.listdir(path))
        
        return stats