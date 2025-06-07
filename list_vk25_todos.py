#!/usr/bin/env python3
"""
List all todos for user VK25
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import SessionLocal
from backend.models import TodoModel, UserModel

def list_vk25_todos():
    """List all todos for VK25"""
    db = SessionLocal()
    
    try:
        # Find user VK25
        user = db.query(UserModel).filter(UserModel.username == "VK25").first()
        
        if not user:
            print("❌ User VK25 not found!")
            return
            
        print(f"👤 User: {user.username} ({user.full_name})")
        print(f"📧 Email: {user.email}")
        print("=" * 50)
        
        # Get all todos for VK25
        todos = db.query(TodoModel).filter(TodoModel.owner_id == user.id).order_by(TodoModel.created_at.desc()).all()
        
        if not todos:
            print("📝 No todos found for VK25")
            return
            
        print(f"📊 Total todos: {len(todos)}")
        print("\n📋 Todo List:")
        print("-" * 50)
        
        for i, todo in enumerate(todos, 1):
            status = "✅" if todo.completed else "⏳"
            print(f"{i}. {status} {todo.title}")
            print(f"   📄 {todo.description}")
            print(f"   🆔 ID: {todo.id}")
            print(f"   ⏰ Created: {todo.created_at}")
            if todo.updated_at != todo.created_at:
                print(f"   🔄 Updated: {todo.updated_at}")
            print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    list_vk25_todos()
