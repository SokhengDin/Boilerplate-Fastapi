# Backend API Template

A comprehensive FastAPI backend template with PostgreSQL 17, authentication, and modern Python development practices.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL 17** - Advanced database with Docker Compose setup
- **JWT Authentication** - Secure token-based authentication with refresh tokens
- **SQLAlchemy** - Modern ORM with mapped_column and type annotations
- **Pydantic Settings** - Environment-based configuration management
- **Loguru** - Advanced logging with rotation and compression
- **Docker Compose** - Complete development environment setup

## Project Structure

```
backend/
├── app/
│   ├── core/
│   │   ├── config.py          # Application configuration
│   │   ├── logger.py          # Logging setup
│   │   └── security.py        # JWT and password utilities
│   ├── database/
│   │   ├── __init__.py        # Database session management
│   │   ├── models/            # Database models
│   │   └── schemas/           # Pydantic schemas
│   ├── routes/
│   │   └── v1/
│   │       └── handlers/      # API endpoints
│   ├── services/              # Business logic
│   └── middleware/            # Custom middleware
├── logs/                      # Application logs
├── docker-compose.yml         # Database setup
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
└── README.md                  # This file
```

## Quick Start

### 1. Start Database Services

```bash
# Start PostgreSQL 17
docker-compose up -d

# Check services are running
docker-compose ps
```

### 2. Setup API Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the API

```bash
# Development mode
python main.py

# Or with uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## Services

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Database**: PostgreSQL 17 on port 5432
- **Adminer**: Database admin on http://localhost:8080

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - User logout

### Users
- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

## Environment Variables

### Docker Compose (.env)
```bash
POSTGRES_DB=backend_db
POSTGRES_USER=backend_user
POSTGRES_PASSWORD=backend_pass_2024
POSTGRES_PORT=5432
ADMINER_PORT=8080
```

### API Configuration
Configuration is managed through `app/core/config.py` using pydantic-settings:

```python
PROJECT_NAME=Backend API
DEBUG=True
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://backend_user:backend_pass_2024@localhost:5432/backend_db
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

## Database

The application uses PostgreSQL 17 with automatic table creation on startup. Database migrations are handled automatically through SQLAlchemy.

### Models
- **User**: User accounts with authentication
- **Token**: JWT token blacklist for logout

## Logging

Logs are configured with Loguru and include:
- Console output with colors
- Current log file: `logs/app.log`
- Daily rotated logs: `logs/app-{date}.log`
- Compressed archives after rotation
- 30-day retention policy

## Security

- Password hashing with bcrypt
- JWT tokens with expiration
- Token blacklist for secure logout
- CORS configuration
- Environment-based secrets

## Development

### Code Style
- Uses comma-first parameter formatting
- Static methods for services
- Type annotations throughout
- Pydantic models for validation

### Testing
```bash
# Run tests
pytest app/tests/
```

### Linting
```bash
# Format code
black .
isort .

# Check code quality
flake8 .
mypy .
```

## Docker Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f postgres

# Reset database
docker-compose down -v
docker-compose up -d
```

## Contributing

1. Follow the existing code style
2. Add tests for new features
3. Update documentation as needed
4. Use static methods for service classes

## License

MIT License