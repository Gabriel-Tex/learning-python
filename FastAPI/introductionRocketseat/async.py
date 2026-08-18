import asyncio # como funciona essa biblioteca?

async def task(name, duration):
    print(f"Tarefa [{name}] inicializando...")
    await asyncio.sleep(duration) # por que o sleep deve esperar?
    print(f"Tarefa [{name}] finalizada.")

async def main():
    await asyncio.gather( # como funciona o gather?
        task(1, 3),
        task(2, 6)
    )
    await task(3, 4)

if __name__ == "__main__": # pra que isso serve?
    asyncio.run(main())
