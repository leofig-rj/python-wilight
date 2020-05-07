#import unittest
import wilight
import asyncio
import unittest
from aiounittest import async_test

from wilight import create_wilight_connection

class WiLightProtocolTestCase(unittest.TestCase):

    @async_test
    async def test_0103(self):
        client = await create_wilight_connection(
            device_id="WL000000000333",
            host="10.0.1.151",
            port=46000,
            model="0103",
            config_ex="10",
            disconnect_callback=None,
            reconnect_callback=None,
            loop=None,
            timeout=10,
            reconnect_interval=15,
            keep_alive_interval=50,
        )

        for i in range(0, 1):
            index = format(i, 'x')

            result = await client.cover_command(index, "open")
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("motor_state"), "opening")
            #await asyncio.sleep(2)
            result = await client.cover_command(index, "stop")
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("motor_state"), "stopped")
            #await asyncio.sleep(2)
            result = await client.cover_command(index, "close")
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("motor_state"), "closing")
            #await asyncio.sleep(2)

            position = 0
            result = await client.set_cover_position(index, position)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("position_target"), position)
            #await asyncio.sleep(2)
            position = 255
            result = await client.set_cover_position(index, position)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("position_target"), position)
            #await asyncio.sleep(2)

if __name__ == '__main__':
    unittest.main()
