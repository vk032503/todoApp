# Quick Reference Guide - Todo App

This is a quick reference for common commands and troubleshooting when working with your todo application.

## 🚀 Starting the Application

### Start Backend
```bash
# Navigate to project folder
cd "C:\Users\YourName\Desktop\Todo App"

# Activate virtual environment
myvenv\Scripts\activate

# Start backend server
python run_backend.py
```

### Start Frontend
```bash
# In a new terminal, navigate to project folder
cd "C:\Users\YourName\Desktop\Todo App"

# Start frontend server
npm run dev
```

### Start MCP Server (Optional)
```bash
# In a third terminal, navigate to project folder
cd "C:\Users\YourName\Desktop\Todo App"

# Activate virtual environment
myvenv\Scripts\activate

# Start MCP server
python run_mcp_server.py
```

## 🔗 Important URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Alternative Docs**: http://localhost:8000/redoc

## 📦 Package Management

### Python Dependencies
```bash
# Install new Python package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

### JavaScript Dependencies
```bash
# Install new npm package
npm install package_name

# Install development dependency
npm install --save-dev package_name

# Install all dependencies
npm install
```

## 🛠️ Common Commands

### Database Operations
```bash
# Reset database (delete todos.db file)
del todos.db

# The database will be recreated when you restart the backend
```

### Testing
```bash
# Test MCP tools
python mcp_server/test_tools.py

# Test backend API (if you have tests)
pytest

# Check frontend for errors
npm run lint
```

### Building for Production
```bash
# Build frontend for production
npm run build

# Start production frontend
npm start
```

## 🐛 Troubleshooting

### Backend Issues

**Error: "Module not found"**
```bash
# Make sure virtual environment is activated
myvenv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Error: "Port already in use"**
```bash
# Kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

### Frontend Issues

**Error: "Command not found: npm"**
- Reinstall Node.js from https://nodejs.org
- Make sure to check "Add to PATH" during installation

**Error: "Module not found"**
```bash
# Delete node_modules and reinstall
rmdir /s node_modules
del package-lock.json
npm install
```

**Error: "Port 3000 already in use"**
```bash
# Kill process using port 3000
netstat -ano | findstr :3000
taskkill /PID <process_id> /F
```

### MCP Issues

**Error: "Cannot import mcp_server"**
```bash
# Make sure you're in the project root directory
# Make sure virtual environment is activated
myvenv\Scripts\activate

# Reinstall MCP
pip install mcp
```

## 📁 File Locations

### Configuration Files
- `package.json` - Frontend dependencies
- `requirements.txt` - Backend dependencies
- `tsconfig.json` - TypeScript configuration
- `tailwind.config.js` - Styling configuration

### Main Application Files
- `backend/main.py` - Backend API
- `src/app/page.tsx` - Frontend main page
- `mcp_server/server.py` - MCP server

### Database
- `todos.db` - SQLite database (created automatically)

## 🔄 Development Workflow

### Adding a New Feature

1. **Backend Changes**:
   - Update `backend/schemas.py` for new data structures
   - Update `backend/crud.py` for new database operations
   - Update `backend/main.py` for new API endpoints

2. **Frontend Changes**:
   - Update `src/types/todo.ts` for TypeScript types
   - Update `src/services/api.ts` for API calls
   - Create/update components in `src/components/`

3. **MCP Changes**:
   - Update `mcp_server/todo_tools.py` for new MCP tools
   - Update `mcp_server/server.py` to register new tools

### Testing Changes

1. Test backend: Visit http://localhost:8000/docs
2. Test frontend: Visit http://localhost:3000
3. Test MCP: Run `python mcp_server/test_tools.py`

## 🆘 Getting Help

### Check Logs
- Backend logs: Visible in the terminal running `python run_backend.py`
- Frontend logs: Visible in the terminal running `npm run dev`
- MCP logs: Check `mcp_server.log` file

### Common Solutions
1. **Restart everything**: Stop all servers and start them again
2. **Clear cache**: Delete `node_modules`, `.next`, and reinstall
3. **Check ports**: Make sure no other applications are using ports 3000 or 8000
4. **Virtual environment**: Always activate before running Python commands

### Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 📝 Notes

- Always activate the virtual environment before running Python commands
- Keep the backend running when using the frontend
- The database file (`todos.db`) is created automatically
- Changes to the code will automatically reload the servers (hot reload)
- Use `Ctrl+C` to stop any running server
