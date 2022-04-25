class TestCase:
    def __init__(self, name) -> None:
        self.name = name
    def setUp(self):
        pass
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasSetUp = True
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True

    def setUp(self):
        self.wasSetUp = True
        self.wasRun = False

class TestCaseTest(TestCase):
    def __init__(self, name) -> None:
        super().__init__(name)

    def testRunning(self):
        test = WasRun('testMethod')
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test = WasRun('testMethod')
        test.run()
        assert(test.wasSetUp)

TestCaseTest('testRunning').run()
TestCaseTest('testSetUp').run()