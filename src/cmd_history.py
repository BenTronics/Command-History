class CMD_History():
    def __init__(self, size):
        self.buf_size = size
        self.buf_size = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0

    def add_item(self, item):
        pass

    def read_forward(self):
        return ""
    
    def read_backward(self):
        return ""

    def reset_read_pos(self):
        pass

    def clear(self):
        pass