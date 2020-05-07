#import unittest
import wilight
import asyncio
import unittest
from aiounittest import async_test

from wilight import create_wilight_connection

class WiLightProtocolTestCase(unittest.TestCase):

    @async_test
    async def test_0102(self):
        client = await create_wilight_connection(
            device_id="WL000000000306",
            host="10.0.1.137",
            port=46000,
            model="0102",
            config_ex="11100010",
            disconnect_callback=None,
            reconnect_callback=None,
            loop=None,
            timeout=10,
            reconnect_interval=15,
            keep_alive_interval=50,
        )

        for i in range(0, 3):
            index = format(i, 'x')
            result = await client.turn_on(index)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), True)
            #await asyncio.sleep(2)
            result = await client.turn_off(index)
            #print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), False)
            #await asyncio.sleep(2)


if __name__ == '__main__':
    unittest.main()
