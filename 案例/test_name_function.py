import unittest
import name_function


class NamesTestCase(unittest.TestCase):
    """测试name_function"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name=name_function.get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')


unittest.main()


