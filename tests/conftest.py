import os
import pytest

from reportconverter.junit_converter import JunitConverter


@pytest.fixture()
def junit_xml_reports():
    return "tests/resources/"


@pytest.fixture()
def json_report_from_junit_xml(junit_xml_reports):
    files = os.listdir(junit_xml_reports)

    def _specify_report(report_name):
        for f in files:
            with open(junit_xml_reports + report_name + ".xml", "r") as report_xml:
                report_xml_contents = report_xml.read()

            junit_converter = JunitConverter()
            json_obj = junit_converter.convert(report_xml_contents)

        return json_obj

    yield _specify_report
