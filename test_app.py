from app import greet

def test_greet():
  assert greet("Darshan") == "Hello, Darshan"
  assert greet("World") == "Hello, World"
