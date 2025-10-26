from app import greet, farewell

def test_greet():
  assert greet("Darshan") == "Hello, Darshan"
  assert greet("World") == "Hello, World"

def test_farewell():
  assert farewell("Darshan") == "Goodbye, Darshan"
  assert farewell("World") == "Goodbye, World"