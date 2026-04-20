# Development Scripts

Convenient scripts for managing the Docker development environment.

## Usage

### Git Bash / WSL (Recommended)

```bash
# Make the script executable (first time only)
chmod +x dev

# Commands
./dev up          # Start containers in background
./dev down        # Stop containers
./dev restart     # Restart containers
./dev build       # Build images (no cache)
./dev rebuild     # Stop, build, and start
./dev logs        # Stream logs (optionally: ./dev logs web)
./dev ps          # Show container status
./dev shell       # Open bash shell in web container
./dev migrate     # Run database migrations
./dev clean       # Remove all containers, networks, volumes
```

### Windows Command Prompt

```cmd
dev_up.bat        # Start containers in background
dev_down.bat      # Stop containers
dev_restart.bat   # Restart containers
dev_build.bat     # Build images (no cache)
dev_logs.bat      # Stream logs (optionally: dev_logs.bat web)
dev_ps.bat        # Show container status
dev_shell.bat     # Open bash shell in web container
dev_migrate.bat   # Run database migrations
dev_clean.bat     # Remove all containers, networks, volumes
```

### PowerShell

```powershell
.\dev_up.bat
.\dev_restart.bat
# etc...
```

## Quick Start

```bash
# First time setup
./dev build
./dev up

# After code changes
./dev restart

# View logs
./dev logs web

# Run migrations
./dev migrate
```
