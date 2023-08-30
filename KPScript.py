import os
import asyncio
import time
from datetime import datetime
from js import window
print("loaded!")
async def loadScreen():
    for i in range(101):
        rot = i * 10
        js.document.getElementById("picLoad").style.transform = f"translate(-50%, -50%) rotate({rot}deg)"
        await asyncio.sleep(1/120)
    for i in range(10, -1, -1):
        js.document.getElementById("loadscreen").style.opacity = i/10
        await asyncio.sleep(.05)
    js.document.getElementById("loadscreen").style.zIndex = -99

asyncio.ensure_future(loadScreen())


def menuTrig():
    asyncio.ensure_future(expandMenu())
      
async def expandMenu():
    print("called")
    box = js.document.getElementById("menu")
    blur = js.document.getElementById("blurBox")
          
    if box.style.height == f"150px":
        for i in range(10, -1 , -1):
              
        blur.style.backdropFilter = f"blur({i/2}px)"
        box.style.height = f"{i*15}px"
        box.style.fontSize = f"{i*2.5}px"
        await asyncio.sleep(.01)
            
        blur.style.height = "0%"

    else:
        blur.style.height = "100%"
        for i in range(11):
            blur.style.backdropFilter = f"blur({i/2}px)"
            box.style.height = f"{i*15}px"
            box.style.fontSize = f"{i*2.5}px"
            await asyncio.sleep(.01)
      
      
      
async def timeClock():
    clock = Element("clock")
    while 1:
        now = datetime.now()
        clock.element.innerText = now.strftime("%H:%M:%S")
        await asyncio.sleep(1)
        #print("test")
    asyncio.ensure_future(timeClock())

def redirectListener(link):
        print("redirect")
        asyncio.ensure_future(redirect(link))
async def redirect(link):
    window.location.href = link