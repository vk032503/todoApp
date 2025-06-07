#!/usr/bin/env python3
"""
MCP Server Runner for Todo Application

This script starts the MCP server that allows AI assistants to interact
with the todo application through the Model Context Protocol.
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

def check_database():
    """Check if the database exists and is accessible"""
    db_path = project_root / "todos.db"
    if not db_path.exists():
        print("Warning: Database file 'todos.db' not found.", file=sys.stderr)
        print("Make sure the FastAPI backend has been run at least once to create the database.", file=sys.stderr)
        return False
    return True

if __name__ == "__main__":
    print("🚀 Starting Todo MCP Server...", file=sys.stderr)
    print("📍 This server provides AI assistants access to your todo data", file=sys.stderr)
    print("🔧 Make sure your FastAPI backend has been run to create the database", file=sys.stderr)
    print("-" * 60, file=sys.stderr)
    
    # Setup logging
    setup_logging()
    
    # Check database
    if not check_database():
        print("⚠️  Database not found, but continuing anyway...", file=sys.stderr)
    
    try:
        # Run the MCP server
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 MCP Server stopped by user", file=sys.stderr)
    except Exception as e:
        print(f"❌ Error running MCP server: {e}", file=sys.stderr)
        sys.exit(1)
