import asyncio
import edge_tts

async def test_tts():
    try:
        communicate = edge_tts.Communicate("Hallo, das ist ein Test", "de-DE-KatjaNeural")
        await communicate.save("test.mp3")
        print("MP3 gespeichert!")
    except Exception as e:
        print("Fehler:", e)

asyncio.run(test_tts())
