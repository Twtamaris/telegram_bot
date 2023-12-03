import asyncio

async def cook_dish(dish, time_to_cook):
    print(f"Started cooking {dish}")
    await asyncio.sleep(time_to_cook)
    print(f"Finished cooking {dish}")

async def welcome_guest(name, time_to_arrive):
    await asyncio.sleep(time_to_arrive)
    print(f"Welcome, {name}!")

async def set_table():
    print("Setting the table...")
    await asyncio.sleep(2)
    print("Table set!")

async def dinner_party():
    tasks = [
        cook_dish("Pasta", 3),
        cook_dish("Salad", 2),
        welcome_guest("Alice", 1),
        welcome_guest("Bob", 4),
        set_table()
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("Preparing for the dinner party...")
    asyncio.run(dinner_party())
    print("Party started!")
