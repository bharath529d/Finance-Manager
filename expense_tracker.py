print("This is expense tracker module.")
print("Will be available soon...")
print("This will take about 2 months I think so")

def log_expense(add_expense):
    def wrapper(*args, **kwargs):
        print("Logging expense...")
        result = add_expense(*args, **kwargs)
        print(f"Expense logged")
        return result
    return wrapper

@log_expense
def add_expense(name,amt):
    print(f"Expense added: {name} - {amt}")


add_expense("Food", 100)