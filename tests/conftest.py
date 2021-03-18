import pytest

from reportconverter.junit_converter import JunitConverter
from reportconverter.status_reader import StatusReader


@pytest.fixture(scope="session")
def junit_xml_reports():
    return "tests/resources/junit/"


@pytest.fixture(scope="session")
def junit_converter():
    return JunitConverter()


@pytest.fixture(scope="session")
def status_reader():
    return StatusReader()


@pytest.fixture(scope="session")
def json_report_from_junit_xml(junit_xml_reports, junit_converter):

    def _specify_report(report_name):
        with open(junit_xml_reports + report_name + ".xml", "r") as report_xml:
            report_xml_contents = report_xml.read()

        return junit_converter.convert(report_xml_contents)

    yield _specify_report


@pytest.fixture(scope="session")
def status_from_report(json_report_from_junit_xml, status_reader):

    def _read_status(report_name):
        return status_reader.read_status(json_report_from_junit_xml(report_name))

    yield _read_status
