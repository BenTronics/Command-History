import unittest

import sys
sys.path.append("..")
from src import cmd_history

buf_size = 5

cmd_hist = cmd_history.CMD_History(buf_size)

class Test(unittest.TestCase):
    def test_empty_read(self):
        super().assertEqual(cmd_hist.read_forward(), "")
    
    def test_add_item(self):
        tmp_list_read = ["-"] * buf_size
        tmp_list_write = ["-"] * buf_size
        cmd_hist.clear()
        # add items until the buffer is full
        for i in range(buf_size):
            cmd_hist.add_item(str(i))
            tmp_list_write[i] = str(i)
        for i in range(buf_size, 0):
            tmp_list_read[i] = cmd_hist.read_backward()
        super().assertEqual(tmp_list_write, tmp_list_read)
    
    def test_add_item_buffer_overrun(self):
        tmp_list_read = ["-"] * buf_size
        tmp_list_write = ["-"] * buf_size
        cmd_hist.clear()
        # add more items than the buffer can hold
        for i in range(buf_size // 2):
           tmp_list_write[i] = str(i)
           cmd_hist.add_item(str(i))
        for i in range(buf_size // 2, 0):
            tmp_list_read[i] = cmd_hist.read_backward()
        super().assertEqual(tmp_list_write, tmp_list_read) 

    def test_read_backwards(self):
        tmp_list_read = []
        tmp_list_write = []
        cmd_hist.clear()
        for i in range(buf_size):
            cmd_hist.add_item(str(i))
            tmp_list_write.append(str(i))
        # read backwards
        for i in range(buf_size):
            tmp_list_read.append(cmd_hist.read_backward())
        super().assertEqual(tmp_list_read, tmp_list_write)
        
    def test_read_forward(self):
        tmp_list_read = []
        tmp_list_write = []
        cmd_hist.clear()
        # read forward
        tmp_list_read = []
        tmp_list_write.reverse()
        for i in range(buf_size):
            tmp_list_read.append(cmd_hist.read_backward())
        super().assertEqual(tmp_list_read, tmp_list_write)
         
    def test_reset_pos(self):
        tmp_list_read = []
        tmp_list_write = []
        cmd_hist.clear()
        # add items until the buffer is full
        for i in range(buf_size):
            cmd_hist.add_item(str(i))
            tmp_list_write.append(str(i))
        for i in range(buf_size // 2, 0):
            tmp_list_read.append(cmd_hist.read_backward())
        cmd_hist.reset_read_pos()
        super().assertEqual(cmd_hist.read_backward(), "")
        super().assertEqual(cmd_hist.read_forward(), "")

if __name__ == "__main__":
    unittest.main()