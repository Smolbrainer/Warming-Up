import python_weather

import os
import asyncio

async def getWeatherData() -> None: 
    location = str(input("Whats the location? "))
    async with python_weather.Client(unit=python_weather.METRIC) as client: #Basically making a temporary variable client
        weather = await client.get(location)
    print(f"The temperature today is {weather.temperature} °C")
    print(f"It feels like {weather.feels_like} °C")
    for daily in weather:
        print(daily)
        for hourly in daily:
            print(hourly)
    print(weather)
  

if __name__ == '__main__': #checks that the script is being run directly. 
    if os.name == 'nt': #nt is the name used by python to represent windows operating system
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) #sets the event policy for asyncio on windows
        #By setting the event loop policy to WindowsSelectorEventLoopPolicy()
        #You ensure that the code uses the selector-based event loop, which can handle asynchronous I/O operations more efficiently on Windows.
        #Basically some defaul code that is written if you are using asyncio



asyncio.run(getWeatherData())