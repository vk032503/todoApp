#!/usr/bin/env python3
"""
Migration script to add google_id column to users table
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import SessionLocal, engine
from sqlalchemy import text

def add_google_id_column():
    """Add google_id column to users table"""
    db = SessionLocal()
    
    try:
        print("🔄 Adding google_id column to users table...")
        
        # Check if column already exists
        result = db.execute(text("""
            SELECT COUNT(*) as count 
            FROM pragma_table_info('users') 
            WHERE name='google_id'
        """))
        
        column_exists = result.fetchone()[0] > 0
        
        if column_exists:
            print("✅ google_id column already exists!")
            return
        
        # Add the column (without UNIQUE constraint for SQLite compatibility)
        db.execute(text("""
            ALTER TABLE users
            ADD COLUMN google_id VARCHAR(255)
        """))

        # Create unique index separately
        db.execute(text("""
            CREATE UNIQUE INDEX IF NOT EXISTS idx_users_google_id
            ON users(google_id)
            WHERE google_id IS NOT NULL
        """))
        
        db.commit()
        print("✅ Successfully added google_id column to users table!")
        
        # Verify the column was added
        result = db.execute(text("""
            SELECT COUNT(*) as count 
            FROM pragma_table_info('users') 
            WHERE name='google_id'
        """))
        
        if result.fetchone()[0] > 0:
            print("✅ Column verification successful!")
        else:
            print("❌ Column verification failed!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_google_id_column()
