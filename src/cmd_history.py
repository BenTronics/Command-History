class CMD_History():
    def __init__(self, size):
        self.buf_size = size
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0
        self.num_of_read_back = 0
        self.num_of_read_forward = 0
        self.num_of_items = 0
        self.state = "idle"

    def add_item(self, item):
        if item == self.buf[self.w_ptr-1]:
            return
        self.num_of_items += 1
        if self.num_of_items >= self.buf_size:
            self.num_of_items = self.buf_size
        self.buf[self.w_ptr] = item
        self.r_ptr = self.w_ptr
        self.w_ptr += 1
        if self.w_ptr >= self.buf_size:
            self.w_ptr = 0

    def read_forward(self):
        if self.state == "backward":
            self.r_ptr += 2
            if self.r_ptr >= self.buf_size:
                self.r_ptr = 0
        r = self.buf[self.r_ptr]
        if self.num_of_read_back > self.num_of_read_forward:
            self.num_of_read_forward += 1
        if self.num_of_read_back > self.num_of_read_forward:
            self.r_ptr += 1
            if self.r_ptr >= self.buf_size:
                self.r_ptr = 0
        self.state = "forward"
        return r
    
    def read_backward(self):
        r = self.buf[self.r_ptr]
        if self.num_of_read_back < self.num_of_items:
            self.num_of_read_back += 1
        if self.num_of_read_back < self.num_of_items:
            self.r_ptr -= 1
            if self.r_ptr < 0:
                self.r_ptr = self.buf_size - 1
        self.state = "backward"
        return r

    def clear(self):
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0
        self.num_of_items = 0
        self.num_of_read_back = 0
        self.num_of_read_forward = 0
        self.state = "idle"