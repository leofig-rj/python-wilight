#import unittest
import wilight
import asyncio
import unittest
from aiounittest import async_test

from wilight import create_wilight_connection

class WiLightProtocolTestCase(unittest.TestCase):

    @async_test
    async def test_0104(self):
        client = await create_wilight_connection(
            device_id="WL000000000333",
            host="10.0.1.151",
            port=46000,
            model="0104",
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

            result = await client.turn_on(index)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), True)
            #await asyncio.sleep(2)
            result = await client.turn_off(index)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), False)
            #await asyncio.sleep(2)

        for i in range(1, 2):
            index = format(i, 'x')

            result = await client.turn_on(index)
            #print(f"result {result}")
            self.assertNotEqual(result.get(index, None).get("direction"), "off")
            #await asyncio.sleep(2)
            result = await client.turn_off(index)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("direction"), "off")
            #await asyncio.sleep(2)

            direction = "forward"
            result = await client.set_fan_direction(index, direction)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("direction"), direction)
            #await asyncio.sleep(2)
            direction = "reverse"
            result = await client.set_fan_direction(index, direction)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("direction"), direction)
            #await asyncio.sleep(2)

            speed = "low"
            result = await client.set_fan_speed(index, speed)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("speed"), speed)
            #await asyncio.sleep(2)
            speed = "medium"
            result = await client.set_fan_speed(index, speed)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("speed"), speed)
            #await asyncio.sleep(2)
            speed = "high"
            result = await client.set_fan_speed(index, speed)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("speed"), speed)
            #await asyncio.sleep(2)

if __name__ == '__main__':
    unittest.main()
