Template Directory Overview

  📁 backend/ - Backend API Template

  Complete FastAPI + PostgreSQL backend with authentication

  Core Structure:
  - app/core/ - Configuration, logging, security utilities
  - app/database/ - Models, schemas, database session management
  - app/routes/v1/handlers/ - API endpoints for auth & users
  - app/services/ - Business logic layer
  - docker-compose.yml - PostgreSQL 17 setup
  - Dockerfile - Container configuration

  📁 ml-app/ - ML Application Template

  FastAPI + HuggingFace ML API for image classification

  Core Structure:
  - app/core/ - Configuration, logging
  - app/prediction/ - ML model and inference logic
  - app/utils/ - Image processing utilities
  - app/dataset/ - Dataset handling utilities
  - app/training/ - Model training utilities
  - main.py + run.py - Application entry points

  🔧 Both Templates Include:

  - Documentation: Comprehensive README.md files
  - Environment: .env configuration with pydantic-settings
  - Logging: Loguru with rotation and compression
  - Dependencies: Complete requirements.txt
  - Git: Proper .gitignore files
  - Code Style: Comma-first formatting, type annotations

  🚀 Ready for Use:

  - Backend: Full CRUD API with JWT auth, database models, Docker setup
  - ML App: Image classification API with HuggingFace integration
  - Production Ready: Error handling, logging, configuration management
  - Extensible: Clear structure for adding new features

  Both templates follow modern Python development practices and can serve as solid foundations for new
   projects.