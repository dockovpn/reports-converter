from reportconverter.base_converter import BaseConverter
import xml.dom.minidom
import json


class JunitConverter(BaseConverter):

    def convert(self, input_file_contents: str) -> str:
        doc = xml.dom.minidom.parseString(input_file_contents)
        testsuites = doc.getElementsByTagName("testsuite")

        reports = []

        for testsuit in testsuites:
            print(testsuit.getAttribute("name"))

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
                "tests": testsuit.getAttribute("tests"),
                "failures": testsuit.getAttribute("failures"),
                "errors": testsuit.getAttribute("errors"),
                "skipped": testsuit.getAttribute("skipped"),
                "time": testsuit.getAttribute("time"),
                "timestamp": testsuit.getAttribute("timestamp"),
                "testcases": testcase_reports
            }

            reports.append(report)

        reports_json = {
            "testsuites": reports
        }

        return json.dumps(reports_json)
