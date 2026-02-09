"""
Database initialization script for Phase III Todo AI Chatbot
Creates all tables based on new SQLModel models
"""

from backend.database.v2_connection import engine
from backend.models.v2.models import Task, Conversation, Message


def init_db():
    """
    Initialize the database by creating all tables
    """
    print("Initializing Phase III Todo AI Chatbot database...")
    Task.metadata.create_all(bind=engine)
    Conversation.metadata.create_all(bind=engine)
    Message.metadata.create_all(bind=engine)
    print("Database initialized successfully!")
    print("Tables created: tasks, conversations, messages")
    print("All persistent state will live in the database as per Phase III constitution.")


if __name__ == "__main__":
    init_db()