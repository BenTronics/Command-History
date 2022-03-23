class CMD_History():
    def __init__(self, size):
        self.buf_size = size
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0

    def add_item(self, item):
        self.w_ptr += 1
        if self.w_ptr >= self.buf_size:
            self.w_ptr = 0
        self.buf[self.w_ptr] = item
        self.r_ptr = self.w_ptr

    def read_forward(self):
        return ""
    
    def read_backward(self):
        r = ""
        if self.r_ptr < 0:
            self.r_ptr = 0
        r = self.buf[self.r_ptr]
        self.r_ptr -= 1
        return r

    def reset_read_pos(self):
        pass

    def clear(self):
        pass