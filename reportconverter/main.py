import argparse
import sys


def convert_report(input_file_path: str, output_file_path: str):
    with open(input_file_path, "r") as input_file:
        xml_str = input_file.read()

    json_str = convert_xml_to_json(xml_str)
    cicd_json_str = convert_report_to_cicd_format(json_str)

    with open(output_file_path, "w") as output_file:
        output_file.write(cicd_json_str)


def convert_xml_to_json(xml_str: str):
    return "converted_json_str"


def convert_report_to_cicd_format(json_str: str):
    return "converted_report_json_str"


def main():
    junit_format = "junit"

    parser = argparse.ArgumentParser()
    parser.add_argument("input-file", type=str, help="Input file containing XML report.")
    parser.add_argument("output-file", type=str, help="Out file where resulting JSON report will be written to.")
    parser.add_argument("--input-format",
                        choices=[junit_format],
                        default=junit_format,
                        type=str, action="",
                        help="Format of the input file")
    args = parser.parse_args()
    convert_report(args.input_file, args.output_file)


if __name__ == '__main__':
    sys.exit(main())
