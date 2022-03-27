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
        cmd_hist.clear()
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
        exspection = ["2", "3", "4", "5", "6"]
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

    def test_two_times_item(self):
        logging.info("test_two_times_item")
        exspection = ["5", "6", "2", "3", "4"]
        cmd_hist.clear()
        for i in range(buf_size + 2):
            cmd_hist.add_item(str(i))
            logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
            cmd_hist.add_item(str(i))
            logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
        self.assertEqual(cmd_hist.buf, exspection)
    
    def test_block_backward(self):
        logging.info("test_block_backward")
        cmd_hist.clear()
        r = ""
        # fill buffer
        for i in range(2):
            cmd_hist.add_item(str(i))
            logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
            logging.debug(f"number of items in buf: {cmd_hist.num_of_items}")
        # read buffer
        for i in range(2):
            r = cmd_hist.read_backward()
            logging.debug(f"read item: {r}")
            logging.debug(f"num of readback: {cmd_hist.num_of_read_back}")
        logging.debug(f"r_ptr {cmd_hist.r_ptr}")
        r = cmd_hist.read_backward()
        logging.debug(f"read item: {r}")
        logging.debug(f"num of readback: {cmd_hist.num_of_read_back}")
        self.assertEqual(r, "0")
    
    def test_block_forward(self):
        logging.info("test_block_forward")
        cmd_hist.clear()
        r = ""
        # fill buffer
        for i in range(3):
            cmd_hist.add_item(str(i))
            logging.debug(f"write item: {str(i)}, buffer: {cmd_hist.buf}")
            logging.debug(f"number of items in buf: {cmd_hist.num_of_items}")
        # read buffer backward
        for i in range(3):
            r = cmd_hist.read_backward()
            logging.debug(f"read (backward) item: {r}")
            logging.debug(f"num of readback: {cmd_hist.num_of_read_back}")
        # read forward
        for i in range(3):
            r = cmd_hist.read_forward()
            logging.debug(f"read (forward) item: {r}")
        logging.debug(f"r_ptr {cmd_hist.r_ptr}")
        r = cmd_hist.read_forward()
        logging.debug(f"read (forward) item: {r}")
        logging.debug(f"num of readback: {cmd_hist.num_of_read_back}")
        self.assertEqual(r, "2")
    
    def test_use_case(self):
        logging.info("test_use_case")
        cmd_hist.clear()
        r = ""
        # try to read empty buffer
        r = cmd_hist.read_backward()
        logging.debug(f"arrow up: {r}")
        self.assertEqual(r, "")
        r = cmd_hist.read_forward()
        logging.debug(f"arrow down: {r}")
        self.assertEqual(r, "")
        # fill the buffer with 3 elements
        for i in range(3):
            cmd_hist.add_item("CMD" + str(i))
        logging.debug(f"buf: {cmd_hist.buf}")
        # read 2 elements backwards and 1 forward
        r = cmd_hist.read_backward()
        logging.debug(f"arrow up: {r}")
        r = cmd_hist.read_backward()
        logging.debug(f"arrow up: {r}")
        r = cmd_hist.read_forward()
        logging.debug(f"arrow down: {r}")
        r = cmd_hist.read_forward()
        logging.debug(f"arrow down: {r}")
        # add 2 items
        # read 2 elements backwards and 1 forward
        # add 3 items
        # read 3 elements backwards and 4 forward


if __name__ == "__main__":
    unittest.main()