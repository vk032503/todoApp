# MCP Server for Todo Application

This directory contains a Model Context Protocol (MCP) server that allows AI assistants to interact with your todo application data.

## 🤖 What is MCP?

Model Context Protocol (MCP) is a standard that allows AI assistants to securely access and interact with external data sources and tools. This MCP server provides AI assistants with the ability to:

- Create, read, update, and delete todos
- Search and filter todos
- Get todo statistics
- Mark todos as complete/incomplete

## 🚀 Quick Start

### 1. Install Dependencies

The MCP dependencies are already included in your `requirements.txt`. If you need to install them separately:

```bash
# Activate your virtual environment
myvenv\Scripts\activate

# Install MCP
pip install mcp
```

### 2. Test the MCP Tools

```bash
# Test the MCP tools functionality
python mcp_server/test_tools.py
```

### 3. Run the MCP Server

```bash
# Start the MCP server
python run_mcp_server.py
```

## 🛠️ Available Tools

The MCP server provides the following tools for AI assistants:

### Core Todo Operations

1. **`list_todos`** - List todos with filtering and pagination
   - Parameters: `limit`, `skip`, `filter_completed`, `search_term`

2. **`get_todo`** - Get a specific todo by ID
   - Parameters: `todo_id`

3. **`create_todo`** - Create a new todo
   - Parameters: `title`, `description` (optional)

4. **`update_todo`** - Update an existing todo
   - Parameters: `todo_id`, `title` (optional), `description` (optional), `completed` (optional)

5. **`delete_todo`** - Delete a todo
   - Parameters: `todo_id`

### Convenience Operations

6. **`mark_todo_complete`** - Mark a todo as complete
   - Parameters: `todo_id`

7. **`mark_todo_incomplete`** - Mark a todo as incomplete
   - Parameters: `todo_id`

8. **`search_todos`** - Search todos by title and description
   - Parameters: `search_term`, `limit` (optional)

9. **`get_active_todos`** - Get all incomplete todos
   - Parameters: `limit` (optional)

10. **`get_completed_todos`** - Get all completed todos
    - Parameters: `limit` (optional)

### Analytics

11. **`get_todo_statistics`** - Get todo statistics
    - Returns: total, completed, active counts and completion rate

## 📋 Example Usage

Here are some example interactions an AI assistant could have with your todo data:

### Creating Todos
```json
{
  "tool": "create_todo",
  "arguments": {
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, and fruits"
  }
}
```

### Searching Todos
```json
{
  "tool": "search_todos",
  "arguments": {
    "search_term": "groceries",
    "limit": 10
  }
}
```

### Getting Statistics
```json
{
  "tool": "get_todo_statistics",
  "arguments": {}
}
```

## 🔧 Configuration

### MCP Client Configuration

To use this MCP server with an AI assistant, add this configuration to your MCP client:

```json
{
  "mcpServers": {
    "todo-server": {
      "command": "python",
      "args": ["run_mcp_server.py"],
      "cwd": "/path/to/your/todo/app",
      "env": {
        "PYTHONPATH": "."
      }
    }
  }
}
```

### Environment Variables

The MCP server uses the same database as your FastAPI backend:

- `DATABASE_URL` - Database connection string (default: `sqlite:///./todos.db`)

## 🔒 Security

The MCP server:
- Only accesses the local SQLite database
- Does not expose any network endpoints
- Runs in the same environment as your application
- Uses the same database permissions as your FastAPI backend

## 🧪 Testing

Run the test script to verify everything works:

```bash
python mcp_server/test_tools.py
```

This will:
1. Test database connectivity
2. Create a test todo
3. Perform various operations
4. Clean up test data

## 📁 File Structure

```
mcp_server/
├── __init__.py          # Package initialization
├── server.py            # Main MCP server implementation
├── todo_tools.py        # Todo operation tools
└── test_tools.py        # Test script

run_mcp_server.py        # MCP server runner script
mcp_config.json          # Example MCP client configuration
```

## 🔗 Integration with Your App

The MCP server integrates seamlessly with your existing todo application:

- **Database**: Uses the same SQLite database as your FastAPI backend
- **Models**: Uses the same SQLAlchemy models and schemas
- **Operations**: Uses the same CRUD operations as your API

This means any changes made through the MCP server will be immediately visible in your web application, and vice versa.

## 🚨 Troubleshooting

### Database Not Found
If you get a database error, make sure:
1. Your FastAPI backend has been run at least once to create the database
2. The `todos.db` file exists in your project root

### Import Errors
If you get import errors:
1. Make sure you're running from the project root directory
2. Ensure your virtual environment is activated
3. Check that all dependencies are installed

### MCP Connection Issues
If AI assistants can't connect:
1. Verify the MCP server is running
2. Check the MCP client configuration
3. Ensure the correct Python path and working directory

## 📚 Learn More

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 🎯 Next Steps

With the MCP server running, AI assistants can now:
- Help you manage your todos through natural language
- Analyze your productivity patterns
- Suggest todo organization strategies
- Automate todo management tasks

Try asking an AI assistant to "show me my active todos" or "create a todo for tomorrow's meeting"!
