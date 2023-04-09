"""
https://docs.python.org/3/tutorial/inputoutput.html
https://pyformat.info
https://www.python-course.eu/python3_formatted_output.php
"""
import logging
import sys

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

if __name__ == '__main__':
    print("hello")
    print("hello %s" % "world")
    print("hello %s %d" % ("world", 1))

    world = "world"
    logger.info(f"Hello {world}")
