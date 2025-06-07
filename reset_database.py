#!/usr/bin/env python3
"""
Reset Database Script
This script will delete the existing database and create a new one with the updated schema.
"""

import os
import sys

def reset_database():
    """Reset the database by deleting the old file"""
    db_file = "todos.db"
    
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"✅ Successfully deleted old database: {db_file}")
        except Exception as e:
            print(f"❌ Error deleting database: {e}")
            return False
    else:
        print(f"ℹ️  Database file {db_file} doesn't exist")
    
    print("✅ Database reset complete!")
    print("🚀 Now restart the backend server to create a new database with the updated schema")
    print("   The default user VK25 with password 'Ready2g@' will be created automatically")
    
    return True

if __name__ == "__main__":
    print("🔄 Resetting Todo Database...")
    print("=" * 50)
    
    if reset_database():
        print("\n📋 Next Steps:")
        print("1. Stop the backend server (Ctrl+C)")
        print("2. Run: python run_backend.py")
        print("3. Visit http://localhost:3000")
        print("4. Login with: VK25 / Ready2g@")
    else:
        print("\n❌ Database reset failed!")
        sys.exit(1)
