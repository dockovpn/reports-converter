import xml.dom.minidom

from reportconverter.base_converter import BaseConverter


class JunitConverter(BaseConverter):

    def convert(self, input_file_contents: str) -> dict:
        doc = xml.dom.minidom.parseString(input_file_contents)
        testsuites = doc.getElementsByTagName("testsuite")

        reports = []

        for testsuit in testsuites:
            testcase_reports = []

            testcases = testsuit.getElementsByTagName("testcase")

            for testcase in testcases:
                testcase_report = {
                    "classname": testsuit.getAttribute("name"),
                    "name": testsuit.getAttribute("name"),
                    "time": testsuit.getAttribute("time"),
                    "passes": len(testcase.getElementsByTagName("failure")) == 0,
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
