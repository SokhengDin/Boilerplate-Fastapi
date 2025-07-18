# Python Project Templates

A collection of production-ready Python project templates for modern development.

## 📁 Backend API Template
**Location**: `backend/`

Complete FastAPI + PostgreSQL backend with authentication and modern development practices.

### Features
- **FastAPI** with async/await patterns
- **PostgreSQL 17** with Docker Compose
- **JWT Authentication** with refresh tokens
- **SQLAlchemy** with modern type annotations
- **Loguru** advanced logging with rotation
- **Pydantic Settings** for configuration

### Structure
```
backend/
├── app/
│   ├── core/           # Configuration, logging, security
│   ├── database/       # Models, schemas, session management
│   ├── routes/v1/      # API endpoints and handlers
│   ├── services/       # Business logic layer
│   └── middleware/     # Custom middleware
├── docker-compose.yml  # PostgreSQL 17 setup
├── Dockerfile         # Container configuration
└── README.md          # Detailed documentation
```

### Quick Start
```bash
cd backend/
docker-compose up -d
pip install -r requirements.txt
python main.py
```

## 📁 ML Application Template
**Location**: `ml-app/`

FastAPI + HuggingFace ML API for image classification with extensible architecture.

### Features
- **FastAPI** for ML API endpoints
- **HuggingFace Transformers** integration
- **Image Processing** with PIL/Pillow
- **Multi-format Support** (upload + base64)
- **Configurable Models** via environment
- **Production Logging** with Loguru

### Structure
```
ml-app/
├── app/
│   ├── core/           # Configuration, logging
│   ├── prediction/     # ML model and inference
│   ├── utils/          # Image processing utilities
│   ├── dataset/        # Dataset handling
│   └── training/       # Model training utilities
├── main.py            # FastAPI application
├── run.py             # Application runner
└── README.md          # Detailed documentation
```

### Quick Start
```bash
cd ml-app/
pip install -r requirements.txt
cp .env.example .env
python run.py
```

## 🔧 Shared Features

### Development Standards
- **Comma-first parameter formatting** for readability
- **Type annotations** throughout codebase
- **Static methods** for service classes
- **Pydantic models** for validation
- **Comprehensive error handling**

### Production Ready
- **Environment Configuration** with pydantic-settings
- **Advanced Logging** with Loguru (rotation, compression)
- **Docker Support** with proper containerization
- **Git Integration** with comprehensive .gitignore
- **Testing Structure** with pytest support
- **Documentation** with detailed README files

### Code Quality
- **Linting** with black, isort, flake8
- **Type Checking** with mypy
- **Security** best practices
- **Performance** optimization patterns

## 🚀 Usage

### Backend Template
Perfect for:
- REST APIs with database persistence
- User authentication systems
- CRUD applications
- Microservices architecture

### ML Template
Perfect for:
- Computer vision APIs
- Model serving endpoints
- Image classification services
- AI/ML microservices

## 📖 Documentation

Each template includes:
- Comprehensive setup instructions
- API endpoint documentation
- Configuration guides
- Development workflows
- Deployment instructions

## 🤝 Contributing

1. Follow existing code style
2. Add tests for new features
3. Update documentation
4. Use static methods for services
5. Maintain type annotations

## 📄 License
 Use freely for personal and commercial projects.
