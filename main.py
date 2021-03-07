import argparse
import sys

from reportconverter.report_converter import junit_format, convert_report


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
