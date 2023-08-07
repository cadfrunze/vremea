ora: int = 9
print(ora)


def test():
    global ora
    ora = 10
    print(f"ora din functie este: {ora}")


test()
print(f"ora din afara functiei este: {ora}")
