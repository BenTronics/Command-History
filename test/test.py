from distutils.log import debug
import unittest

import logging
logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG, format="[{levelname}] {message}", style="{")

import sys
sys.path.append("..")
from src import cmd_history

buf_size = 5

cmd_hist = cmd_history.CMD_History(buf_size)

class Test(unittest.TestCase):
    def test_empty_read(self):
        logging.info("test_empty_read")
        r = cmd_hist.read_forward()
        logging.debug(f"return value: {r}")
        self.assertEqual(r, "")
    
    def test_add_item(self):
        logging.info("test_add_item")
        tmp_list_write = ["0", "1", "2", "3", "4"]
        cmd_hist.clear()
        # add items until the buffer is full
        for elem in tmp_list_write:
            cmd_hist.add_item(elem)
            logging.debug(f"write item: {elem}, buffer: {cmd_hist.buf}")
        self.assertEqual(tmp_list_write, cmd_hist.buf)
    
    def test_buffer_overflow(self):
        logging.info("test_buffer_overflow")
        tmp_list_write = ["0", "1", "2", "3", "4", "5", "6"]
        exspection = ["5", "6", "2", "3", "4"]
        cmd_hist.clear()
        # add more items than the buffer can hold
        for elem in tmp_list_write:
           cmd_hist.add_item(elem)
           logging.debug(f"write item: {elem}, buffer: {cmd_hist.buf}")
        self.assertEqual(cmd_hist.buf, exspection) 

    def test_read_backwards(self):
        logging.info("test_read_backwards")
        tmp_list_read = ["-"] * buf_size
        exspection = ["6", "5", "4", "3", "2"]
        cmd_hist.clear()
        # add more items than the buffer can hold
        for i in range(buf_size + 2):
           cmd_hist.add_item(str(i))
           logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
        for i in range(buf_size):
            logging.debug(f"r_pointer pos: {cmd_hist.r_ptr}")
            tmp_list_read[i] = cmd_hist.read_backward()
            logging.debug(f"read item: {tmp_list_read[i]}")
        self.assertEqual(exspection, tmp_list_read)
        
    def test_read_forward(self):
        logging.info("test_read_forward")
        tmp_list_read = ["-"] * buf_size
        exspection = ["6", "2", "3", "4", "5"]
        empty_read = ""
        cmd_hist.clear()
        # add more items than the buffer can hold
        for i in range(buf_size + 2):
           cmd_hist.add_item(str(i))
           logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
        # read all elements backwards
        for i in range(buf_size):
            cmd_hist.read_backward()
        for i in range(buf_size):
            tmp_list_read[i] = cmd_hist.read_forward()
            logging.debug(f"read item: {tmp_list_read[i]}")
        self.assertEqual(exspection, tmp_list_read)
         
    def test_reset_pos(self):
        cmd_hist.clear()
        # add items until the buffer overrun
        for i in range(buf_size+2):
            cmd_hist.add_item(str(i))
        # change r_ptr position
        for i in range(buf_size):
            cmd_hist.read_backward()
        cmd_hist.reset_read_pos()
        self.assertEqual(cmd_hist.read_backward(), "6")
        cmd_hist.reset_read_pos()
        self.assertEqual(cmd_hist.read_forward(), "6")

    def test_two_times_item(self):
        logging.info("test_two_times_item")
        exspection = ["0", "1", "2", "3", "4"]
        cmd_hist.clear()
        for i in range(buf_size):
            cmd_hist.add_item(str(i))
            logging.debug(f"writr item: {str(i)}, buffer: {cmd_hist.buf}")
            cmd_hist.add_item(str(i))
            logging.debug(f"writr item: {str(i)}, buffer: {cmd_hist.buf}")
        self.assertEqual(cmd_hist.buf, exspection)


if __name__ == "__main__":
    unittest.main()