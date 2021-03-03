import argparse
import sys

from reportconverter.base_converter import BaseConverter
from reportconverter.junit_converter import JunitConverter

junit_format = "junit"

converters = {
    junit_format: JunitConverter()
}


def get_converter(input_format: str):
    converter: BaseConverter = converters[input_format]
    return converter


def convert_report(input_file_path: str, output_file_path: str, input_format: str):
    with open(input_file_path, "r") as input_file:
        xml_str = input_file.read()

    cicd_json_str = convert_report_to_cicd_format(xml_str, input_format)

    with open(output_file_path, "w") as output_file:
        output_file.write(cicd_json_str)


def convert_report_to_cicd_format(json_str: str, input_format: str):
    converter: BaseConverter = get_converter(input_format)
    return converter.convert(json_str)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file containing XML report.")
    parser.add_argument("output_file", type=str, help="Out file where resulting JSON report will be written to.")
    parser.add_argument("--input-format",
                        choices=[junit_format],
                        default=junit_format,
                        type=str,
                        help="Format of the input file")
    args = parser.parse_args()
    convert_report(args.input_file, args.output_file, args.input_format)


if __name__ == '__main__':
    sys.exit(main())
