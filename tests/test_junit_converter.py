
def test_converts_plain_junit_report(json_report_from_junit_xml):
    json_obj = json_report_from_junit_xml("plain_report_all_pass")
    # breakpoint()
    assert len(json_obj["testsuites"]) == 1
    testsuit = json_obj["testsuites"][0]
    assert testsuit["name"] == "TestSuite"
    assert testsuit["tests"] == 1
    assert testsuit["errors"] == 0
    assert testsuit["failures"] == 0
    assert testsuit["skipped"] == 0
    assert len(testsuit["testcases"]) == 1
    testcase = testsuit["testcases"][0]
    assert testcase["passes"] is True


def test_converts_plain_junit_report_with_1_failure(json_report_from_junit_xml):
    json_obj = json_report_from_junit_xml("plain_report_1_ok_1_failure")
    # breakpoint()
    assert len(json_obj["testsuites"]) == 1
    testsuit = json_obj["testsuites"][0]
    assert testsuit["name"] == "TestSuite"
    assert testsuit["tests"] == 2
    assert testsuit["errors"] == 0
    assert testsuit["failures"] == 1
    assert testsuit["skipped"] == 0
    assert len(testsuit["testcases"]) == 2
    testcase1 = testsuit["testcases"][0]
    assert testcase1["passes"] is True
    testcase2 = testsuit["testcases"][1]
    assert testcase2["passes"] is False


def test_converts_merged_junit_report(json_report_from_junit_xml):
    json_obj = json_report_from_junit_xml("merged_report_all_pass")
    # breakpoint()
    assert len(json_obj["testsuites"]) == 2

    testsuit1 = json_obj["testsuites"][0]
    assert testsuit1["name"] == "TestSuite1"
    assert testsuit1["tests"] == 2
    assert testsuit1["errors"] == 0
    assert testsuit1["failures"] == 0
    assert testsuit1["skipped"] == 0
    assert len(testsuit1["testcases"]) == 2
    testcase1_1 = testsuit1["testcases"][0]
    assert testcase1_1["passes"] is True
    testcase1_2 = testsuit1["testcases"][1]
    assert testcase1_2["passes"] is True

    testsuit2 = json_obj["testsuites"][1]
    assert testsuit2["name"] == "TestSuite2"
    assert testsuit2["tests"] == 1
    assert testsuit2["errors"] == 0
    assert testsuit2["failures"] == 0
    assert testsuit2["skipped"] == 0
    assert len(testsuit2["testcases"]) == 1
    testcase2_1 = testsuit2["testcases"][0]
    assert testcase2_1["passes"] is True
