from string import String

# test exception
strings = ["test", "50 chars for testing String class raise exceptions"]
for i in strings:
    try:
        string = String(i)
        print("Created ", string)
    except Exception:
        print("An exception occurred")
