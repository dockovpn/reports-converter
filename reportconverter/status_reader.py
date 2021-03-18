from reportconverter.statuses import Status


class StatusReader(object):

    def read_status(self, cicd_json: dict) -> str:
        if any(self.__is_testsuite_failing(testsuite) for testsuite in cicd_json["testsuites"]):
            return Status.FAILING

        return Status.PASSING

    def __is_testsuite_failing(self, testsuite: dict) -> bool:
        if testsuite["errors"] != 0 or testsuite["failures"] != 0:
            return True

        return False
