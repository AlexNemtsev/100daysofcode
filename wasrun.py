class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        try:
            self.setUp()
        except:
            result.testFailed()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    def __init__(self, name) -> None:
        TestCase.__init__(self, name)

    def testMethod(self):
        self.log = self.log + 'testMethod '

    def setUp(self):
        self.log = 'setUp '

    def tearDown(self):
        self.log = self.log + 'tearDown '

    def testBrokenMethod(self):
        raise Exception


class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = + 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return f'{self.runCount} run, {self.errorCount} failed'


class TestCaseTest(TestCase):
    def setUp(self):
        raise Exception

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert('setUp testMethod tearDown ' == test.log)

    def testResult(self):
        test = WasRun('testMethod')
        result = test.run()
        assert('1 run, 0 failed' == result.summary())

    def testBrokenMethod(self):
        test = WasRun('testBrokenMethod')
        result = test.run()
        assert('1 run, 1 failed' == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert('1 run, 1 failed' == result.summary())


TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()
TestCaseTest('testBrokenMethod').run()
