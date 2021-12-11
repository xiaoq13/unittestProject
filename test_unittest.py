import unittest

class test_unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_1_add(self):
        num1=1
        num2=2
        num3=num1+num2
        print("add",num3)

    def test_2_sub(self):
        num1=10
        num2=2
        num3=num1-num2
        print('sub',num3)

    def test_3_mul(self):
        num1=2
        num2=5
        num3=num1*num2
        print("mul",num3)


    def test_4_div(self):
        num1=15
        num2=3
        num3=num1/num2
        print("div",num3)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

if __name__=='__main__':
    #方法一：一次添加一个用例
    # suite=unittest.TestSuite()
    # suite.addTest(test_unittest('test_1_add'))
    # suite.addTest(test_unittest('test_3_mul'))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)

    #方法二：一次添加多个用例
    testcases=[test_unittest("test_2_sub"),test_unittest("test_4_div")]
    suite=unittest.TestSuite()
    suite.addTests(testcases)
    runner=unittest.TextTestRunner()
    runner.run(suite)