from reportconverter.junit_converter import JunitConverter
import json


def test_converts_plain_junit_report():
    with open("tests/resources/plain_report.xml", "r") as report_xml:
        report_xml_contents = report_xml.read()

    junit_converter = JunitConverter()
    report_json = junit_converter.convert(report_xml_contents)
    json_obj = json.loads(report_json)
    # breakpoint()
    assert len(json_obj["testsuites"]) == 1
    testsuit = json_obj["testsuites"][0]
    assert testsuit["name"] == "DummyTest"
    assert testsuit["tests"] == "1"
    assert testsuit["errors"] == "0"
    assert testsuit["failures"] == "0"
    assert testsuit["skipped"] == "0"
    assert len(testsuit["testcases"]) == 1
    testcase = testsuit["testcases"][0]
    assert testcase["passes"] is True
