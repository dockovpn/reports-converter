from reportconverter.statuses import Status


def test_status_from_plain_report(status_from_report):
    status = status_from_report("plain_report_all_pass")

    assert status == Status.PASSING


def test_status_from_report_with_failure(status_from_report):
    status = status_from_report("plain_report_1_ok_1_failure")

    assert status == Status.FAILING


def test_status_from_report_merged(status_from_report):
    status = status_from_report("merged_report_all_pass")

    assert status == Status.PASSING
