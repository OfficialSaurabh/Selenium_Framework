from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    # @data( ("JavaScript for beginners", "1025 1256 1256", "1020", "10"),("Learn Python 3 from scratch", "20", "1220", "20"))
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, ccnum, ccexp, cccvv):
        self.courses.clickAllCourse()
        self.courses.enterCourseName(course_name)
        self.courses.selectCourseToEnroll(course_name)
        self.courses.enrollCourse(num=ccnum, exp=ccexp, cvv=cccvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnroll", result, "Enroll Failed Verification")
