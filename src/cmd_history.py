class CMD_History():
    def __init__(self, size):
        self.buf_size = size
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0

    def add_item(self, item):
        if item == self.buf[self.w_ptr-1]:
            return
        self.buf[self.w_ptr] = item
        self.r_ptr = self.w_ptr
        self.w_ptr += 1
        if self.w_ptr >= self.buf_size:
            self.w_ptr = 0
        print(f"add item> {self.buf}")

    def read_forward(self):
        r = self.buf[self.r_ptr]
        self.r_ptr += 1
        if self.r_ptr >= self.buf_size:
            self.r_ptr = 0
        print(f"read forward> {r}")
        return r
    
    def read_backward(self):
        r = self.buf[self.r_ptr]
        self.r_ptr -= 1
        if self.r_ptr < 0:
            self.r_ptr = self.buf_size - 1
        print(f"read backward> {r}")
        return r

    def reset_read_pos(self):
        self.r_ptr = self.w_ptr - 1
        if self.r_ptr < 0:
            self.r_ptr = 0

    def clear(self):
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0