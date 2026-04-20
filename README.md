Overview
A Financial Trade simulator to create and analyse trades based on market rates, which will help generate new reports, such as Anna reports, MTM reports, and PNL backtesting reports.

Done steps 
A trade platform with:
- Custom session-authenticated users using email or username.
- BCrypt-backed password hashing through Django password hashers.
- `Entity`, `Portfolio`, `Counterparty`, `CCP`, `FCM`, and `LegalAgreement` apps.
- DRF `APIView` endpoints without routers/viewsets.
- Local pre-commit hooks for Ruff and Black.

## Run with Docker

```bash
chmod +x scripts/dev       # First time only
  ./scripts/dev up
  ./scripts/dev restart

Windows CMD:
  scripts\dev_up.bat
  scripts\dev_restart.bat

Tip: Add scripts to your PATH by creating a symlink or adding to .bashrc:
export PATH="$PATH:/c/Users/admin/projects/Fintech/FinTech-Backend/scripts"
```

The compose file reads Docker and Django configuration from `.env`. Copy `.env.example` to `.env` if you need to recreate it.

## API quick start

Register:

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"admin@example.com\",\"username\":\"admin\",\"firstname\":\"Admin\",\"lastname\":\"User\",\"password\":\"password123\"}"
```

Login:

```bash
curl -i -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"admin@example.com\",\"password\":\"password123\"}"
```

The login endpoint returns:

```json
{"message": "logged in"}
```

## Development

```bash
pip install -r requirements.txt
pre-commit install
pre-commit run --all-files
```

Core API routes are available under `/api/entities/`, `/api/portfolios/`, `/api/counterparties/`, `/api/ccps/`, `/api/fcms/`, and `/api/legal-agreements/`.
