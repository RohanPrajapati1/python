# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())


# - Call print(myfunction())
# - myfunction() → calls myinner().
# - Inside myinner:
# - Since n == 1, it runs func().lower().
# - func() is the original myfunction(), which returns "Hello Linus".
# - .lower() converts it to "hello linus".
# - That value is returned and printed.
