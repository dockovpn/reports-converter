import json

from reportconverter.base_converter import BaseConverter
from reportconverter.junit_converter import JunitConverter
from reportconverter.status_reader import StatusReader

junit_format = "junit"

converters = {
    junit_format: JunitConverter()
}


def get_converter(input_format: str):
    converter: BaseConverter = converters[input_format]
    return converter


def convert_report(input_file_path: str, output_file_path: str, input_format: str, output_status: bool = False):
    with open(input_file_path, "r") as input_file:
        xml_str = input_file.read()

    cicd_json = convert_report_to_cicd_format(xml_str, input_format)
    cicd_json_str = json.dumps(cicd_json)

    with open(output_file_path, "w") as output_file:
        output_file.write(cicd_json_str)

    if output_status:
        status_reader = StatusReader()
        print(status_reader.read_status(cicd_json))


def convert_report_to_cicd_format(xml_str: str, input_format: str) -> dict:
    converter: BaseConverter = get_converter(input_format)
    return converter.convert(xml_str)
