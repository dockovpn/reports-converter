import xml.dom.minidom

from reportconverter.converter.base_converter import BaseConverter


class JunitConverter(BaseConverter):

    def convert(self, input_file_contents: str) -> dict:
        doc = xml.dom.minidom.parseString(input_file_contents)
        testsuites = doc.getElementsByTagName("testsuite")

        reports = []

        for testsuit in testsuites:
            testcase_reports = []

            testcases = testsuit.getElementsByTagName("testcase")

            for testcase in testcases:
                failures = testcase.getElementsByTagName("failure")
                failure_data = None
                for failure in failures:
                    failure_data = failure.firstChild.data

                testcase_report = {
                    "classname": testcase.getAttribute("classname"),
                    "name": testcase.getAttribute("name"),
                    "time": testcase.getAttribute("time"),
                    "passes": len(testcase.getElementsByTagName("failure")) == 0,
                    "skipped": len(testcase.getElementsByTagName("skipped")) != 0,
                    "failure": failure_data
                }

                testcase_reports.append(testcase_report)

            report = {
                "name": testsuit.getAttribute("name"),
                "tests": int(testsuit.getAttribute("tests")),
                "failures": int(testsuit.getAttribute("failures")),
                "errors": int(testsuit.getAttribute("errors")),
                "skipped": int(testsuit.getAttribute("skipped")),
                "time": testsuit.getAttribute("time"),
                "timestamp": testsuit.getAttribute("timestamp"),
                "testcases": testcase_reports
            }

            reports.append(report)

        reports_json = {
            "testsuites": reports
        }

        return reports_json
