# ML App Template - Dog/Cat Prediction API

A FastAPI-based machine learning application template for image classification using HuggingFace Transformers.

## Features

- **FastAPI** - Modern, fast web framework for building ML APIs
- **HuggingFace Transformers** - Pre-trained models for image classification
- **PIL/Pillow** - Image processing and validation
- **Pydantic Settings** - Environment-based configuration management
- **Loguru** - Advanced logging with rotation and compression
- **Multi-format Support** - File upload and base64 image processing

## Project Structure

```
ml-app/
├── app/
│   ├── core/
│   │   ├── config.py          # Application configuration
│   │   └── logger.py          # Logging setup
│   ├── dataset/
│   │   ├── __init__.py
│   │   └── data_loader.py     # Dataset utilities
│   ├── prediction/
│   │   ├── __init__.py
│   │   └── model.py           # ML model and prediction logic
│   ├── training/
│   │   ├── __init__.py
│   │   └── trainer.py         # Training utilities
│   ├── utils/
│   │   ├── __init__.py
│   │   └── image_processor.py # Image validation and processing
│   └── tests/                 # Test files
├── logs/                      # Application logs
├── main.py                    # FastAPI application
├── run.py                     # Application runner
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── .env.example              # Environment template
└── README.md                  # This file
```

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings
```

### 3. Run the Application

```bash
# Using the runner script
python run.py

# Or directly with main.py
python main.py

# Or with uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /` - Application info and version
- `GET /health` - Health status

### Prediction
- `POST /predict` - Upload image file for prediction
- `POST /predict/base64` - Send base64 encoded image for prediction

## Usage Examples

### File Upload Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_image.jpg"
```

### Base64 Prediction

```bash
curl -X POST "http://localhost:8000/predict/base64" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_encoded_image_string"}'
```

### Response Format

```json
{
  "filename": "dog.jpg",
  "prediction": "dog",
  "confidence": 0.8925,
  "scores": {
    "dog": 0.8925,
    "cat": 0.1075
  }
}
```

## Environment Variables

Configuration is managed through `.env` file:

```env
# Application Settings
APP_NAME=Dog/Cat Prediction API
APP_VERSION=1.0.0
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False

# Model Settings
MODEL_NAME=microsoft/resnet-50
MAX_IMAGE_SIZE=224

# Logging
LOG_LEVEL=INFO
```

## Supported Image Formats

- JPEG/JPG
- PNG
- WEBP
- BMP
- TIFF

Images are automatically:
- Validated for format compatibility
- Converted to RGB color space
- Resized to model input requirements (224x224)

## Model Configuration

The application uses HuggingFace Transformers with configurable models:

- **Default Model**: `microsoft/resnet-50`
- **Image Size**: 224x224 pixels
- **Classification**: ImageNet-based with dog/cat mapping

### Changing Models

Update the `MODEL_NAME` in your `.env` file:

```env
# Examples of compatible models
MODEL_NAME=microsoft/resnet-50
MODEL_NAME=google/vit-base-patch16-224
MODEL_NAME=facebook/convnext-tiny-224
```

## Logging

Logs are configured with Loguru and include:
- Console output with colors
- Current log file: `logs/app.log`
- Daily rotated logs: `logs/app-{date}.log`
- Compressed archives after rotation
- 30-day retention policy

Log levels: DEBUG, INFO, WARNING, ERROR

## Development

### Code Style
- Uses comma-first parameter formatting
- Type annotations throughout
- Pydantic models for validation
- Static methods where appropriate

### Testing

```bash
# Run tests
pytest app/tests/

# Test API endpoints
python -m pytest app/tests/test_api.py -v
```

### Adding New Models

1. Update `MODEL_NAME` in configuration
2. Modify prediction logic in `app/prediction/model.py` if needed
3. Test with sample images
4. Update documentation

### Training Custom Models

The `app/training/` directory provides utilities for:
- Dataset preparation
- Model training
- Model evaluation
- Export for deployment

## Error Handling

The API provides detailed error messages:

- **400**: Invalid image format or corrupted file
- **422**: Invalid request format
- **500**: Model loading or prediction errors

Debug mode (`DEBUG=True`) provides full tracebacks.

## Performance

- Model loading happens at startup (cached)
- Images processed in-memory
- Automatic resizing for optimal performance
- Support for batch processing (future enhancement)

## Docker Support

```dockerfile
# Example Dockerfile usage
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "run.py"]
```

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [PIL/Pillow Documentation](https://pillow.readthedocs.io/)
