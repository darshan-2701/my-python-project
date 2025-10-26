def greet(name):
  """ Returns a greeting."""
  return f"Hello, {name}"

if __name__ == "__main__":
  name = input("Enter your name: ")
  print(greet(name))
