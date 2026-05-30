bank = input("Greeting: ").strip().casefold()

if "hello" in bank:
       print("$0")
elif str(bank).startswith("h"):
      print("$20")
else:
      print("$100")



