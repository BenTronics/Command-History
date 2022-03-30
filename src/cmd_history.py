class CMD_History():
    def __init__(self, size):
        self.buf_size = size
        self.buf = [""] * self.buf_size
        self.w_ptr = 0
        self.r_ptr = 0
        self.num_of_read_back = 0
        self.num_of_read_forward = 0
        self.num_of_items = 0
        self.index_of_last_added = 0
        self.state = "add_item"

    def add_item(self, item):
        if item == self.buf[self.w_ptr-1]:
            return
        self.num_of_items += 1
        if self.num_of_items >= self.buf_size:
            self.num_of_items = self.buf_size
        self.buf[self.w_ptr] = item
        self.index_of_last_added = self.w_ptr
        self.r_ptr = self.w_ptr
        self.num_of_read_back = 0
        self.w_ptr += 1
        if self.w_ptr >= self.buf_size:
            self.w_ptr = 0
        self.state = "add_item"

    def read_forward(self):
        r = ""
        if self.state == "add_item":
            return ""
        elif self.state == "forward":
            if self.r_ptr != self.index_of_last_added:
                self.r_ptr += 1
                self.num_of_read_forward += 1
                if self.r_ptr >= self.buf_size:
                    self.r_ptr = 0
        elif self.state == "backward":
            self.r_ptr += 1
            if self.r_ptr >= self.buf_size:
                self.r_ptr = 0
        r = self.buf[self.r_ptr]
        self.state = "forward"
        return r
    
    def read_backward(self):
        r = ""
        tmp_r_ptr = 0
        tmp_r_ptr = self.r_ptr
        if self.state == "add_item":
            pass
        elif self.state == "backward":
            tmp_r_ptr -= 1
            if tmp_r_ptr < 0:
                tmp_r_ptr = self.buf_size-1
            if self.buf[tmp_r_ptr] == "":
                return self.buf[self.r_ptr]
            if self.num_of_read_back < self.buf_size-1:
                self.num_of_read_back += 1
                self.r_ptr -= 1
                if self.r_ptr < 0:
                    self.r_ptr = self.buf_size-1
        elif self.state == "forward":
            tmp_r_ptr -= 1
            if tmp_r_ptr < 0:
                tmp_r_ptr = self.buf_size-1
            if self.buf[tmp_r_ptr] == "":
                return self.buf[self.r_ptr]
            self.r_ptr -= 1
            if self.r_ptr < 0:
                self.r_ptr = self.buf_size-1
            self.num_of_read_back -= self.num_of_read_forward
        r = self.buf[self.r_ptr]
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