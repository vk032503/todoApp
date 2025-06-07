#!/usr/bin/env python3
"""
Add 10,000 random todos for user VK25
"""

import sys
import os
import random
from datetime import datetime, timedelta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import SessionLocal
from backend.models import TodoModel, UserModel

# Random todo templates
TODO_TEMPLATES = [
    # Work tasks
    ("Complete project proposal", "Finish the quarterly project proposal and submit to management"),
    ("Team meeting at {time}", "Attend weekly team standup meeting to discuss progress"),
    ("Review code changes", "Review and approve pending pull requests from team members"),
    ("Update documentation", "Update project documentation with latest changes"),
    ("Client call at {time}", "Schedule and conduct client check-in call"),
    ("Prepare presentation", "Create slides for upcoming stakeholder presentation"),
    ("Bug fix: Issue #{num}", "Investigate and fix reported bug in the system"),
    ("Deploy to production", "Deploy latest changes to production environment"),
    ("Database backup", "Perform scheduled database backup and verification"),
    ("Security audit", "Conduct monthly security audit and update protocols"),
    
    # Personal tasks
    ("Grocery shopping", "Buy groceries for the week including fruits and vegetables"),
    ("Doctor appointment at {time}", "Annual health checkup with family doctor"),
    ("Gym workout", "Complete 45-minute workout session at the gym"),
    ("Call {person}", "Catch up with family member or friend"),
    ("Pay bills", "Pay monthly utilities and credit card bills"),
    ("Car maintenance", "Schedule oil change and tire rotation"),
    ("Book vacation", "Research and book summer vacation destination"),
    ("Read book: {book}", "Continue reading current book for 30 minutes"),
    ("Meal prep", "Prepare healthy meals for the upcoming week"),
    ("Clean house", "Deep clean living room and kitchen areas"),
    
    # Learning tasks
    ("Study {subject}", "Spend 1 hour studying new programming language or skill"),
    ("Online course", "Complete next module of online certification course"),
    ("Practice coding", "Solve 3 algorithm problems on coding platform"),
    ("Watch tutorial", "Watch educational video about new technology"),
    ("Write blog post", "Write technical blog post about recent project"),
    ("Learn new tool", "Explore and learn new development tool or framework"),
    ("Attend webinar", "Join industry webinar about latest trends"),
    ("Read documentation", "Study official documentation for new library"),
    ("Code review", "Review open source project code for learning"),
    ("Practice presentation", "Practice public speaking with recorded session"),
    
    # Health & Fitness
    ("Morning run", "30-minute jog around the neighborhood"),
    ("Yoga session", "Complete 20-minute yoga routine for flexibility"),
    ("Drink water", "Ensure drinking 8 glasses of water throughout the day"),
    ("Meditation", "10-minute mindfulness meditation session"),
    ("Stretch break", "Take 5-minute stretch break from desk work"),
    ("Healthy lunch", "Prepare nutritious lunch with vegetables and protein"),
    ("Sleep schedule", "Go to bed by 10 PM for better sleep quality"),
    ("Walk meeting", "Take walking meeting instead of sitting in office"),
    ("Vitamin check", "Take daily vitamins and supplements"),
    ("Posture check", "Monitor and correct sitting posture every hour"),
]

# Random data for templates
TIMES = ["9:00 AM", "10:30 AM", "2:00 PM", "3:30 PM", "4:00 PM", "11:00 AM", "1:00 PM"]
PEOPLE = ["Mom", "Dad", "Sarah", "John", "Mike", "Lisa", "Tom", "Anna", "David", "Emma"]
BOOKS = ["Python Tricks", "Clean Code", "The Pragmatic Programmer", "Design Patterns", "Atomic Habits"]
SUBJECTS = ["Python", "JavaScript", "React", "SQL", "Machine Learning", "DevOps", "Cloud Computing"]
NUMBERS = range(1001, 9999)

def generate_random_todo():
    """Generate a random todo item"""
    title_template, description = random.choice(TODO_TEMPLATES)
    
    # Replace placeholders in title
    title = title_template
    if "{time}" in title:
        title = title.replace("{time}", random.choice(TIMES))
    if "{person}" in title:
        title = title.replace("{person}", random.choice(PEOPLE))
    if "{book}" in title:
        title = title.replace("{book}", random.choice(BOOKS))
    if "{subject}" in title:
        title = title.replace("{subject}", random.choice(SUBJECTS))
    if "{num}" in title:
        title = title.replace("{num}", str(random.choice(NUMBERS)))
    
    # Random completion status (70% incomplete, 30% complete)
    completed = random.random() < 0.3
    
    # Random creation time (within last 30 days)
    days_ago = random.randint(0, 30)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)
    created_at = datetime.utcnow() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
    
    return {
        "title": title,
        "description": description,
        "completed": completed,
        "created_at": created_at,
        "updated_at": created_at
    }

def add_bulk_todos():
    """Add 10,000 random todos for VK25"""
    db = SessionLocal()
    
    try:
        # Find user VK25
        user = db.query(UserModel).filter(UserModel.username == "VK25").first()
        
        if not user:
            print("❌ User VK25 not found!")
            return
            
        print(f"✅ Found user: {user.username} (ID: {user.id})")
        
        # Check current todo count
        current_count = db.query(TodoModel).filter(TodoModel.owner_id == user.id).count()
        print(f"📊 Current todos for {user.username}: {current_count}")
        
        print("🚀 Starting to generate 10,000 random todos...")
        print("⏳ This may take a few minutes...")
        
        # Generate todos in batches for better performance
        batch_size = 1000
        total_todos = 10000
        
        for batch_num in range(0, total_todos, batch_size):
            batch_todos = []
            
            for i in range(batch_size):
                if batch_num + i >= total_todos:
                    break
                    
                todo_data = generate_random_todo()
                todo = TodoModel(
                    title=todo_data["title"],
                    description=todo_data["description"],
                    completed=todo_data["completed"],
                    owner_id=user.id,
                    created_at=todo_data["created_at"],
                    updated_at=todo_data["updated_at"]
                )
                batch_todos.append(todo)
            
            # Add batch to database
            db.add_all(batch_todos)
            db.commit()
            
            completed = batch_num + len(batch_todos)
            progress = (completed / total_todos) * 100
            print(f"📝 Progress: {completed:,}/{total_todos:,} todos ({progress:.1f}%)")
        
        # Final count
        final_count = db.query(TodoModel).filter(TodoModel.owner_id == user.id).count()
        added_count = final_count - current_count
        
        print("\n✅ Bulk todo creation completed!")
        print(f"📊 Previous count: {current_count:,}")
        print(f"📊 Added: {added_count:,}")
        print(f"📊 Total todos for {user.username}: {final_count:,}")
        
        # Show some statistics
        completed_todos = db.query(TodoModel).filter(
            TodoModel.owner_id == user.id,
            TodoModel.completed == True
        ).count()
        
        active_todos = final_count - completed_todos
        completion_rate = (completed_todos / final_count * 100) if final_count > 0 else 0
        
        print(f"✅ Completed todos: {completed_todos:,}")
        print(f"⏳ Active todos: {active_todos:,}")
        print(f"📈 Completion rate: {completion_rate:.1f}%")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🎯 Random Todo Generator for VK25")
    print("=" * 50)
    print("⚠️  Adding 10,000 random todos to VK25's account...")
    add_bulk_todos()
