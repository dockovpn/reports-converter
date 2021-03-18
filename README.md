# Report Converter

A tool that converts test reports from different frameworks into unified 
[CICD Pipeline](https://github.com/alekslitvinenk/cicd) format. At the moment tool supports only JUnit reports format
but there plans to add more. Also, the tool can analyze resulting JSON and provide quick summary in the form of the 
following statements: PASSING, FAILING or N/A

## Usage
From tool's help documentation:
```shell
usage: main.py [-h] [--input-format {junit}] [--status] input_file output_file

positional arguments:
  input_file            Input file containing XML report
  output_file           Out file where resulting JSON report will be written
                        to

optional arguments:
  -h, --help            show this help message and exit
  --input-format {junit}
                        Format of the input file
  --status              Boolean flag that being enabled makes the tool output
                        resulting status of the test run, i.e: passing,
                        failing or n/a
```