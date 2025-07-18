import torch
import os
import json

from transformers import AutoImageProcessor, AutoModelForImageClassification
from transformers import TrainingArguments, Trainer
from torch.utils.data import Dataset
from PIL import Image
from datetime import datetime

class DogCatDataset(Dataset):
    def __init__(self, data_dir: str, split: str = "train"):
        self.data_dir = data_dir
        self.split = split
        self.processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
        self.samples = self._load_samples()
    
    def _load_samples(self):
        samples = []
        for class_idx, class_name in enumerate(["cats", "dogs"]):
            class_path = f"{self.data_dir}/{self.split}/{class_name}"
            if os.path.exists(class_path):
                for img_name in os.listdir(class_path):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        samples.append({
                            "path": os.path.join(class_path, img_name),
                            "label": class_idx
                        })
        return samples
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        sample = self.samples[idx]
        image = Image.open(sample["path"]).convert("RGB")
        inputs = self.processor(image, return_tensors="pt")
        
        return {
            "pixel_values": inputs["pixel_values"].squeeze(),
            "labels": torch.tensor(sample["label"], dtype=torch.long)
        }

class ModelTrainer:
    def __init__(self, model_name: str = "microsoft/resnet-50"):
        self.model_name = model_name
        self.model = None
        self.processor = None
        self.training_history = []
    
    def setup_model(self, num_labels: int = 2):
        """Setup model for fine-tuning"""
        self.processor = AutoImageProcessor.from_pretrained(self.model_name)
        self.model = AutoModelForImageClassification.from_pretrained(
            self.model_name
            , num_labels                = num_labels
            , ignore_mismatched_sizes   = True
        )
    
    def train(self, data_dir: str, epochs: int = 3, batch_size: int = 8):
        """Train the model"""
        if not self.model:
            self.setup_model()
        
        train_dataset = DogCatDataset(data_dir, "train")
        
        training_args = TrainingArguments(
            output_dir                      = "./results"
            , num_train_epochs              = epochs
            , per_device_train_batch_size   = batch_size
            , warmup_steps                  = 500
            , weight_decay                  = 0.01
            , logging_dir                   = "./logs"
            , logging_steps                 = 10
            , save_strategy                 = "epoch"
            , evaluation_strategy           = "no"
        )
        
        trainer = Trainer(
            model           = self.model
            , args          = training_args
            , train_dataset = train_dataset
        )
        
        trainer.train()
        
        # Save training history
        self.training_history.append({
            "timestamp"     : datetime.now().isoformat(),
            "epochs"        : epochs,
            "batch_size"    : batch_size,
            "dataset_size"  : len(train_dataset)
        })
        
        return trainer
    
    def save_model(self, save_path: str = "./models/dog_cat_classifier"):
        """Save the trained model"""
        os.makedirs(save_path, exist_ok=True)
        self.model.save_pretrained(save_path)
        self.processor.save_pretrained(save_path)
        
        # Save training history
        with open(f"{save_path}/training_history.json", "w") as f:
            json.dump(self.training_history, f, indent=2)
        
        print(f"Model saved to {save_path}")
    
    def load_model(self, model_path: str):
        """Load a trained model"""
        self.model = AutoModelForImageClassification.from_pretrained(model_path)
        self.processor = AutoImageProcessor.from_pretrained(model_path)
        print(f"Model loaded from {model_path}")