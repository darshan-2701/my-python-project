def greet(name):
  """ Returns a greeting."""
  return f"Hello, {name}"

def farewell(name):
  """ Returns a farewell."""
  return f"Goodbye, {name}"

if __name__ == "__main__":
  name = input("Enter your name: ")
  print(greet(name))
  print(farewell(name))
