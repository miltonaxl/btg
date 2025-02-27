# BTG - FastAPI con Arquitectura Hexagonal

## 📌 Introducción

BTG es una API RESTful basada en FastAPI que sigue los principios de Arquitectura Hexagonal. El proyecto está diseñado para ser escalable, mantenible y fácil de probar, utilizando MongoDB como base de datos.

## 🚀 Características

- **FastAPI** para servicios web de alto rendimiento.
- **MongoDB** para almacenamiento de datos flexible y escalable.
- **Arquitectura Hexagonal** para modularidad y mantenibilidad.
- **Pydantic** para validación y serialización de datos.
- **Inyección de Dependencias** para mejorar la capacidad de prueba.
- **Soporte para Docker** para despliegues en contenedores.
- **Pre-commit Hooks** para formateo y linting automático del código.
- **Pruebas Unitarias y E2E** con Pytest.

## 🔧 Instalación

### **1️⃣ Clonar el Repositorio**

```bash
git clone https://github.com/yourusername/btg.git
cd btg
```

### **2️⃣ Configurar un Entorno Virtual**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **3️⃣ Instalar Dependencias**

```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar Variables de Entorno**

Renombra `.env.example` a `.env` y actualiza las variables necesarias:

```ini
MONGO_URI=mongodb://localhost:27017
MONGO_DB=btg_db
```

### **5️⃣ Ejecutar la Aplicación**

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: [http://localhost:8000](http://localhost:8000)

---

## 📂 Estructura del Proyecto

```plaintext
btg/
├── src/
│   ├── api/               # API entry points (REST)
│   │   ├── routers/       # Organized routes per module
│   │   │   ├── funds.py
│   │   │   ├── transactions.py
│   │   │   ├── users.py
│   │   │   ├── balances.py
│   │   │   ├── routers.py  # controlling all router for only one import to main.py
│   │   ├── __init__.py
│   ├── core/              # Core configuration and dependencies
│   │   ├── shared/
│   │   |    ├── decorators/
│   │   |    |  ├── validate_schemas # validate all schemas per attributes
│   │   ├── config.py         # Environment variables
│   │   ├── database.py       # MongoDB connection
│   │   ├── dependencies.py   # Dependency injection
│   │   ├── seeder.bash   # Execute all seeder that found inside the project
│   ├── domains/           # Business logic separated by domain
│   │   ├── funds/
│   │   │   ├── models.py       # Database models
│   │   │   ├── schemas.py      # Pydantic validation
│   │   │   ├── repository.py   # Database access (MongoDB)
│   │   │   ├── service.py      # Business logic
│   │   │   ├── use_cases.py    # Specific use cases
│   │   ├── transactions/
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── repository.py
│   │   │   ├── service.py
│   │   │   ├── use_cases.py
│   │   ├── balances/       # New module for handling user balances
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   ├── repository.py
│   │   │   ├── service.py
│   │   │   ├── use_cases.py
│   ├── adapters/          # External integrations (Emails, Notifications)
│   │   ├── email_service.py
│   │   ├── sms_service.py
│   │   ├── notification_adapter.py
│   ├── middlewares/       # New middleware layer
│   │   ├── ip_validation.py    # validate if ip coming for set user in request
|   |   ├── validate_resource.py    # Middleware to check if user exist
│   ├── tests/             # Unit and integration tests
│   │   ├── unit/
│   │   ├── e2e/
│   ├── main.py            # FastAPI entry point
│   ├── __init__.py
├── Dockerfile             # Docker container setup
├── requirements.txt       # Project dependencies
├── pytest.ini             # Test configuration
├── .env                   # Environment variables (MongoDB, API Keys)
├── .gitignore             # Ignore unnecessary files in Git
├── .pre-commit-config.yaml  # Pre-commit hooks for linting and formatting
├── pyproject.toml         # Configuration for tools like Black, Ruff, isort
├── README.md              # Project documentation
```
