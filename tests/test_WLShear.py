"""
Example unit tests for WLShear package
"""
import unittest
import desc.wlshear

class WLShearTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'

    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.wlshear.WLShear(self.message)
        self.assertEquals(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.wlshear.WLShear)
        foo = desc.wlshear.WLShear(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
