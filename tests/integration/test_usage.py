import logging
import time

from start_end_logging.start_end_logging import log_start, log_end, init_logging

log = logging.getLogger(__name__)


def test_usage():
    init_logging("../logs", "log.log")
    log_start("main process", log)
    log_start("preparing something", log)
    time.sleep(0.15)
    log_end()
    log_start("preparing something other", log)
    time.sleep(0.05)
    log_end()
    time.sleep(0.25)
    log_end()
