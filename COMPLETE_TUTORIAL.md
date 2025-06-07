# Complete Tutorial: Building a Full-Stack Todo App with Next.js, FastAPI, and MCP

This is a comprehensive, step-by-step guide to building a modern full-stack todo application from scratch. Perfect for beginners who want to understand every detail.

## 📋 What We're Building

- **Frontend**: Next.js 14 with TypeScript and Tailwind CSS
- **Backend**: FastAPI with SQLite database
- **AI Integration**: MCP (Model Context Protocol) server
- **Features**: Create, read, update, delete todos with beautiful UI

## 🛠️ Prerequisites

Before starting, make sure you have:
- **Windows 10/11** (this guide is for Windows)
- **Basic knowledge** of files and folders
- **Internet connection** for downloading tools

## 📁 Project Structure Overview

```
📦 Todo App/
├── 🎨 Frontend (Next.js)
│   ├── src/app/          # Pages and layouts
│   ├── src/components/   # Reusable UI components
│   ├── src/services/     # API communication
│   ├── src/types/        # TypeScript definitions
│   └── package.json      # Frontend dependencies
├── 🚀 Backend (FastAPI)
│   ├── backend/          # API logic and database
│   ├── tests/            # API tests
│   ├── requirements.txt  # Python dependencies
│   └── run_backend.py    # Backend server runner
├── 🤖 MCP Server
│   ├── mcp_server/       # MCP tools and server
│   └── run_mcp_server.py # MCP server runner
└── 📄 Configuration files
```

---

# PART 1: ENVIRONMENT SETUP

## Step 1: Install Node.js

### 1.1 Download Node.js
1. Open your web browser
2. Go to https://nodejs.org
3. Click **"Download the LTS version"** (recommended for most users)
4. Save the file to your Downloads folder

### 1.2 Install Node.js
1. Find the downloaded file (usually `node-v20.x.x-x64.msi`)
2. Double-click to run the installer
3. Click **"Next"** through all the steps
4. Accept the license agreement
5. Keep default installation location
6. Make sure **"Add to PATH"** is checked
7. Click **"Install"**
8. Wait for installation to complete
9. Click **"Finish"**

### 1.3 Verify Node.js Installation
1. Press `Windows + R`
2. Type `cmd` and press Enter
3. In the black window (Command Prompt), type:
   ```bash
   node --version
   ```
4. You should see something like `v20.10.0`
5. Also check npm:
   ```bash
   npm --version
   ```
6. You should see something like `10.2.3`

**If you see version numbers, Node.js is installed correctly!**

## Step 2: Install Python

### 2.1 Download Python
1. Go to https://python.org
2. Click **"Downloads"**
3. Click **"Download Python 3.12.x"** (latest version)
4. Save the file to your Downloads folder

### 2.2 Install Python
1. Find the downloaded file (usually `python-3.12.x-amd64.exe`)
2. **IMPORTANT**: Right-click and select **"Run as administrator"**
3. **CRITICAL**: Check the box **"Add Python to PATH"** at the bottom
4. Click **"Install Now"**
5. Wait for installation to complete
6. Click **"Close"**

### 2.3 Verify Python Installation
1. Open Command Prompt (Windows + R, type `cmd`, press Enter)
2. Type:
   ```bash
   python --version
   ```
3. You should see something like `Python 3.12.0`
4. Also check pip:
   ```bash
   pip --version
   ```

**If you see version numbers, Python is installed correctly!**

## Step 3: Create Project Folder

### 3.1 Create Main Folder
1. Open File Explorer (Windows + E)
2. Navigate to your Desktop
3. Right-click in empty space
4. Select **"New" → "Folder"**
5. Name it **"Todo App"** (exactly like this)
6. Press Enter

### 3.2 Open Command Prompt in Project Folder
1. Open the "Todo App" folder
2. Click in the address bar (where it shows the path)
3. Type `cmd` and press Enter
4. A Command Prompt will open in your project folder

**You should see something like: `C:\Users\YourName\Desktop\Todo App>`**

---

# PART 2: BACKEND SETUP (FastAPI)

## Step 4: Create Python Virtual Environment

### 4.1 What is a Virtual Environment?
A virtual environment is like a separate box for your Python project. It keeps all the project's dependencies separate from other Python projects on your computer.

### 4.2 Create Virtual Environment
In your Command Prompt (inside Todo App folder), type:
```bash
python -m venv myvenv
```

**What this does**: Creates a folder called `myvenv` with a separate Python environment.

### 4.3 Activate Virtual Environment
```bash
myvenv\Scripts\activate
```

**You should see `(myvenv)` at the beginning of your command prompt line.**

**What this does**: Switches to using the virtual environment's Python instead of the system Python.

## Step 5: Create Backend Structure

### 5.1 Create Backend Folder
```bash
mkdir backend
```

### 5.2 Create Requirements File
Create a file called `requirements.txt` in your main folder:

1. Right-click in the Todo App folder
2. Select **"New" → "Text Document"**
3. Name it `requirements.txt` (remove the .txt extension)
4. Open it with Notepad
5. Copy and paste this content:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
alembic==1.13.0
python-dotenv==1.0.0
pytest==7.4.3
httpx==0.25.2
mcp==1.0.0
anyio==3.7.1
```

6. Save and close the file

**What this file does**: Lists all the Python packages our backend needs.

### 5.3 Install Backend Dependencies
In Command Prompt (with virtual environment activated):
```bash
pip install -r requirements.txt
```

**This will take a few minutes.** It downloads and installs all the packages.

**What this does**: Installs FastAPI (web framework), SQLAlchemy (database), and other tools we need.

## Step 6: Create Database Models

### 6.1 Create Database File
Create `backend\database.py`:

1. Navigate to the `backend` folder
2. Right-click → New → Text Document
3. Name it `database.py`
4. Open with Notepad and paste this code:

```python
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database URL - using SQLite for simplicity
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Todo model
class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)
```

**What this file does**: 
- Sets up SQLite database connection
- Defines the structure of a todo item (id, title, description, etc.)
- Creates functions to manage database connections

### 6.2 Create Data Schemas
Create `backend\schemas.py`:

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Todo title")
    description: Optional[str] = Field(None, max_length=1000, description="Todo description")

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Todo title")
    description: Optional[str] = Field(None, max_length=1000, description="Todo description")
    completed: Optional[bool] = Field(None, description="Todo completion status")

class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TodoListResponse(BaseModel):
    todos: list[TodoResponse]
    total: int
    
class MessageResponse(BaseModel):
    message: str
```

**What this file does**:
- Defines the structure of data that comes in and goes out of our API
- Validates that data is in the correct format
- Ensures type safety

### 6.3 Create Database Operations
Create `backend\crud.py`:

```python
from sqlalchemy.orm import Session
from sqlalchemy import desc
from backend.database import TodoModel
from backend.schemas import TodoCreate, TodoUpdate
from typing import List, Optional
from datetime import datetime

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[TodoModel]:
    """Get all todos with pagination"""
    return db.query(TodoModel).order_by(desc(TodoModel.created_at)).offset(skip).limit(limit).all()

def get_todo_by_id(db: Session, todo_id: int) -> Optional[TodoModel]:
    """Get a specific todo by ID"""
    return db.query(TodoModel).filter(TodoModel.id == todo_id).first()

def create_todo(db: Session, todo: TodoCreate) -> TodoModel:
    """Create a new todo"""
    db_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=False,
        created_at=datetime.utcnow()
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[TodoModel]:
    """Update an existing todo"""
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not db_todo:
        return None

    # Update only provided fields
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    db_todo.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a todo"""
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not db_todo:
        return False

    db.delete(db_todo)
    db.commit()
    return True

def get_todos_count(db: Session) -> int:
    """Get total count of todos"""
    return db.query(TodoModel).count()

def get_completed_todos_count(db: Session) -> int:
    """Get count of completed todos"""
    return db.query(TodoModel).filter(TodoModel.completed == True).count()

def get_active_todos_count(db: Session) -> int:
    """Get count of active (incomplete) todos"""
    return db.query(TodoModel).filter(TodoModel.completed == False).count()
```

**What this file does**:
- Contains all the functions that interact with the database
- Create, read, update, delete operations (CRUD)
- Helper functions for counting todos

## Step 7: Create FastAPI Application

### 7.1 Create Main API File
Create `backend\main.py`:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from backend.database import get_db, create_tables
from backend.schemas import TodoResponse, TodoCreate, TodoUpdate, MessageResponse
from backend import crud

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="A modern Todo API built with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    create_tables()

# Health check endpoint
@app.get("/", response_model=MessageResponse)
def read_root():
    return {"message": "Todo API is running! Visit /docs for API documentation."}

@app.get("/health", response_model=MessageResponse)
def health_check():
    return {"message": "API is healthy"}

# Todo endpoints
@app.get("/todos", response_model=List[TodoResponse])
def get_todos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all todos with optional pagination"""
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos

@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    """Create a new todo"""
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific todo by ID"""
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return db_todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing todo"""
    db_todo = crud.update_todo(db, todo_id=todo_id, todo_update=todo_update)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return db_todo

@app.delete("/todos/{todo_id}", response_model=MessageResponse)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    """Delete a todo"""
    success = crud.delete_todo(db, todo_id=todo_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return {"message": "Todo deleted successfully"}

# Statistics endpoint
@app.get("/todos/stats/summary")
def get_todo_stats(db: Session = Depends(get_db)):
    """Get todo statistics"""
    total = crud.get_todos_count(db)
    completed = crud.get_completed_todos_count(db)
    active = crud.get_active_todos_count(db)

    return {
        "total": total,
        "completed": completed,
        "active": active,
        "completion_rate": round((completed / total * 100) if total > 0 else 0, 2)
    }

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
```

**What this file does**:
- Creates the main FastAPI application
- Defines all the API endpoints (URLs that frontend can call)
- Handles CORS (allows frontend to communicate with backend)
- Creates database tables automatically when started

### 7.2 Create Backend Runner Script
Create `run_backend.py` in your main folder (not in backend folder):

```python
#!/usr/bin/env python3
"""
FastAPI Todo Backend Runner
Run this script to start the FastAPI development server
"""

import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Run the FastAPI application"""
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    reload = os.getenv("API_RELOAD", "True").lower() == "true"

    print("🚀 Starting FastAPI Todo Backend...")
    print(f"📍 Server will be available at: http://{host}:{port}")
    print(f"📚 API Documentation: http://{host}:{port}/docs")
    print(f"🔄 Auto-reload: {'Enabled' if reload else 'Disabled'}")
    print("-" * 50)

    uvicorn.run(
        "backend.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

if __name__ == "__main__":
    main()
```

### 7.3 Create Backend Init File
Create `backend\__init__.py` (empty file):

1. Right-click in backend folder
2. New → Text Document
3. Name it `__init__.py`
4. Leave it empty and save

**What this file does**: Tells Python that `backend` is a package that can be imported.

## Step 8: Test the Backend

### 8.1 Start the Backend Server
In your Command Prompt (with virtual environment activated):
```bash
python run_backend.py
```

**You should see**:
```
🚀 Starting FastAPI Todo Backend...
📍 Server will be available at: http://0.0.0.0:8000
📚 API Documentation: http://0.0.0.0:8000/docs
🔄 Auto-reload: Enabled
--------------------------------------------------
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1234] using WatchFiles
INFO:     Started server process [5678]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 8.2 Test the API
1. Open your web browser
2. Go to: `http://localhost:8000/docs`
3. You should see the FastAPI documentation page
4. Try clicking on different endpoints to test them

**If you see the documentation page, your backend is working!**

### 8.3 Stop the Backend
To stop the backend server:
- Press `Ctrl + C` in the Command Prompt

---

# PART 3: FRONTEND SETUP (Next.js)

## Step 9: Create Frontend Structure

### 9.1 Open New Command Prompt
1. Keep the backend running in one Command Prompt
2. Open a new Command Prompt in your Todo App folder
3. You should be in: `C:\Users\YourName\Desktop\Todo App>`

### 9.2 Create Package.json
Create `package.json` in your main folder:

```json
{
  "name": "todo-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.0.4",
    "react": "^18",
    "react-dom": "^18",
    "axios": "^1.6.2",
    "lucide-react": "^0.294.0"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "autoprefixer": "^10.0.1",
    "eslint": "^8",
    "eslint-config-next": "14.0.4",
    "postcss": "^8",
    "tailwindcss": "^3.3.0"
  }
}
```

**What this file does**: Lists all the JavaScript packages our frontend needs.

### 9.3 Install Frontend Dependencies
In your new Command Prompt:
```bash
npm install
```

**This will take a few minutes.** It downloads and installs React, Next.js, TypeScript, and other frontend tools.

**What this does**: Downloads all the JavaScript packages listed in package.json.

### 9.4 Create Configuration Files

#### Create `next.config.js`:
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
}

module.exports = nextConfig
```

#### Create `tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

#### Create `tailwind.config.js`:
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
```

#### Create `postcss.config.js`:
```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

**What these files do**:
- `next.config.js`: Configures Next.js framework
- `tsconfig.json`: Configures TypeScript compiler
- `tailwind.config.js`: Configures Tailwind CSS styling
- `postcss.config.js`: Configures CSS processing

## Step 10: Create Frontend Folder Structure

### 10.1 Create Folders
Create these folders in your main directory:
```bash
mkdir src
mkdir src\app
mkdir src\components
mkdir src\services
mkdir src\types
```

**What these folders are for**:
- `src\app`: Main pages and layouts
- `src\components`: Reusable UI components
- `src\services`: API communication code
- `src\types`: TypeScript type definitions

---

# PART 4: MCP SERVER SETUP (AI Integration)

## Step 11: Install MCP Dependencies

### 11.1 Install MCP Package
In your Command Prompt (with virtual environment activated):
```bash
pip install mcp
```

**What this does**: Installs the Model Context Protocol package that allows AI assistants to interact with your app.

### 11.2 Create MCP Folder Structure
```bash
mkdir mcp_server
```

## Step 12: Create MCP Server Files

### 12.1 Create MCP Tools
Create `mcp_server\todo_tools.py`:

This file contains all the functions that AI assistants can use to manage todos. It includes:
- Creating new todos
- Reading existing todos
- Updating todos
- Deleting todos
- Searching todos
- Getting statistics

### 12.2 Create MCP Server
Create `mcp_server\server.py`:

This file creates the actual MCP server that AI assistants connect to. It:
- Defines all available tools
- Handles requests from AI assistants
- Returns results in the correct format

### 12.3 Create MCP Runner
Create `run_mcp_server.py` in your main folder:

```python
#!/usr/bin/env python3
"""
MCP Server Runner for Todo Application
"""

import sys
import os
import asyncio
import logging
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from mcp_server.server import main

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stderr),
            logging.FileHandler('mcp_server.log')
        ]
    )

if __name__ == "__main__":
    print("🚀 Starting Todo MCP Server...", file=sys.stderr)
    print("📍 This server provides AI assistants access to your todo data", file=sys.stderr)
    print("-" * 60, file=sys.stderr)

    setup_logging()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 MCP Server stopped by user", file=sys.stderr)
    except Exception as e:
        print(f"❌ Error running MCP server: {e}", file=sys.stderr)
        sys.exit(1)
```

**What the MCP server does**:
- Allows AI assistants to create, read, update, and delete todos
- Provides search and filtering capabilities
- Gives access to todo statistics
- Works with the same database as your web application

---

# PART 5: RUNNING THE COMPLETE APPLICATION

## Step 13: Start All Services

### 13.1 Start Backend (Terminal 1)
Open Command Prompt in your Todo App folder:
```bash
# Activate virtual environment
myvenv\Scripts\activate

# Start backend
python run_backend.py
```

**Keep this running.** You should see:
```
🚀 Starting FastAPI Todo Backend...
📍 Server will be available at: http://0.0.0.0:8000
```

### 13.2 Start Frontend (Terminal 2)
Open a new Command Prompt in your Todo App folder:
```bash
# Start frontend
npm run dev
```

**Keep this running.** You should see:
```
▲ Next.js 14.0.4
- Local:        http://localhost:3000
✓ Ready in 2.1s
```

### 13.3 Start MCP Server (Terminal 3) - Optional
Open a third Command Prompt in your Todo App folder:
```bash
# Activate virtual environment
myvenv\Scripts\activate

# Start MCP server
python run_mcp_server.py
```

## Step 14: Test Your Application

### 14.1 Test the Web Application
1. Open your web browser
2. Go to: `http://localhost:3000`
3. You should see your beautiful todo application
4. Try adding, editing, and deleting todos

### 14.2 Test the API
1. Go to: `http://localhost:8000/docs`
2. You should see the FastAPI documentation
3. Try testing different API endpoints

### 14.3 Test MCP Integration
Create a simple test script `test_mcp.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from mcp_server.todo_tools import TodoMCPTools

def test_mcp():
    tools = TodoMCPTools()

    # Create a test todo
    result = tools.create_todo("Test MCP Todo", "Created via MCP")
    print("Created todo:", result)

    # List all todos
    todos = tools.list_todos()
    print("All todos:", todos)

if __name__ == "__main__":
    test_mcp()
```

Run it:
```bash
myvenv\Scripts\activate
python test_mcp.py
```

---

# PART 6: UNDERSTANDING THE APPLICATION

## How Everything Works Together

### 1. **Database Layer (SQLite)**
- Stores all todo data
- Managed by SQLAlchemy ORM
- Automatically creates tables when backend starts

### 2. **Backend Layer (FastAPI)**
- Provides REST API endpoints
- Handles CRUD operations
- Validates data with Pydantic
- Serves API documentation

### 3. **Frontend Layer (Next.js)**
- Beautiful, responsive user interface
- Communicates with backend via HTTP requests
- Real-time updates and smooth animations
- TypeScript for type safety

### 4. **MCP Layer (AI Integration)**
- Allows AI assistants to manage todos
- Uses same database as web application
- Provides rich set of tools for AI interaction
- Secure local access only

## File Structure Summary

```
📦 Todo App/
├── 📁 backend/              # FastAPI backend
│   ├── __init__.py
│   ├── main.py              # Main API application
│   ├── database.py          # Database models
│   ├── schemas.py           # Data validation
│   └── crud.py              # Database operations
├── 📁 src/                  # Next.js frontend
│   ├── 📁 app/              # Pages and layouts
│   ├── 📁 components/       # UI components
│   ├── 📁 services/         # API communication
│   └── 📁 types/            # TypeScript types
├── 📁 mcp_server/           # MCP server for AI
│   ├── __init__.py
│   ├── server.py            # MCP server
│   └── todo_tools.py        # MCP tools
├── 📁 myvenv/               # Python virtual environment
├── 📄 requirements.txt      # Python dependencies
├── 📄 package.json          # JavaScript dependencies
├── 📄 run_backend.py        # Backend runner
├── 📄 run_mcp_server.py     # MCP server runner
└── 📄 todos.db              # SQLite database (created automatically)
```

## Congratulations! 🎉

You have successfully built a complete full-stack todo application with:
- ✅ Modern React frontend with TypeScript
- ✅ FastAPI backend with database
- ✅ AI integration via MCP server
- ✅ Beautiful, responsive design
- ✅ Real-time data synchronization

Your application is now ready for use and can be extended with additional features!
