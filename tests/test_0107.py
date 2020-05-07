#import unittest
import wilight
import asyncio
import unittest
from aiounittest import async_test

from wilight import create_wilight_connection

class WiLightProtocolTestCase(unittest.TestCase):

    @async_test
    async def test_0107(self):
        client = await create_wilight_connection(
            device_id="WL000000000333",
            host="10.0.1.151",
            port=46000,
            model="0107",
            config_ex="00010",
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
            print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), True)
            await asyncio.sleep(2)
            result = await client.turn_off(index)
            print(f"result {result}")
            self.assertEqual(result.get(index, None).get("on"), False)
            await asyncio.sleep(2)

        for i in range(0, 1):
            index = format(i, 'x')
            brightness = 20
            result = await client.set_brightness(index, brightness)
            print(f"result {result}")
            self.assertEqual(result.get(index, None).get("brightness"), brightness)
            await asyncio.sleep(2)
            brightness = 255
            result = await client.set_brightness(index, brightness)
            print(f"result {result}")
            #self.assertEqual(result.get(index, None).get("brightness"), brightness)
            await asyncio.sleep(2)

        for i in range(0, 1):
            index = format(i, 'x')
            hue = 254
            saturation = 100
            result = await client.set_hs_color(index, hue, saturation)
            print(f"result {result}")
            hue_error = result.get(index, None).get("hue") - hue
            if hue_error < 0 :
                hue_error = -hue_error
            self.assertLessEqual(hue_error, 1)
            saturation_error = result.get(index, None).get("saturation") - saturation
            if saturation_error < 0 :
                saturation_error = -saturation_error
            self.assertLessEqual(saturation_error, 1)
            await asyncio.sleep(2)
            hue = 127
            saturation = 50
            result = await client.set_hs_color(index, hue, saturation)
            print(f"result {result}")
            hue_error = result.get(index, None).get("hue") - hue
            if hue_error < 0 :
                hue_error = -hue_error
            self.assertLessEqual(hue_error, 1)
            saturation_error = result.get(index, None).get("saturation") - saturation
            if saturation_error < 0 :
                saturation_error = -saturation_error
            self.assertLessEqual(saturation_error, 1)
            await asyncio.sleep(2)

        for i in range(0, 1):
            index = format(i, 'x')
            hue = 254
            saturation = 100
            brightness = 127
            result = await client.set_hsb_color(index, hue, saturation, brightness)
            print(f"result {result}")
            hue_error = result.get(index, None).get("hue") - hue
            if hue_error < 0 :
                hue_error = -hue_error
            self.assertLessEqual(hue_error, 1)
            saturation_error = result.get(index, None).get("saturation") - saturation
            if saturation_error < 0 :
                saturation_error = -saturation_error
            self.assertLessEqual(saturation_error, 1)
            self.assertEqual(result.get(index, None).get("brightness"), brightness)
            await asyncio.sleep(2)
            hue = 64
            saturation = 80
            brightness = 255
            result = await client.set_hsb_color(index, hue, saturation, brightness)
            print(f"result {result}")
            hue_error = result.get(index, None).get("hue") - hue
            if hue_error < 0 :
                hue_error = -hue_error
            self.assertLessEqual(hue_error, 1)
            saturation_error = result.get(index, None).get("saturation") - saturation
            if saturation_error < 0 :
                saturation_error = -saturation_error
            self.assertLessEqual(saturation_error, 1)
            self.assertEqual(result.get(index, None).get("brightness"), brightness)
            #await asyncio.sleep(2)

if __name__ == '__main__':
    unittest.main()
