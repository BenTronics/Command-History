class CMD_History():
    def __init__(self, size):
        self._buf_size = size
        self._buf = [""] * self._buf_size
        self._w_ptr = 0
        self._r_ptr = 0
        self._num_of_read_back = 0
        self._num_of_read_forward = 0
        self._num_of_items = 0
        self._index_of_last_added = 0
        self._state = "add_item"

    def add_item(self, item):
        if item == self._buf[self._w_ptr-1]:
            return
        self._num_of_items += 1
        if self._num_of_items >= self._buf_size:
            self._num_of_items = self._buf_size
        self._buf[self._w_ptr] = item
        self._index_of_last_added = self._w_ptr
        self._r_ptr = self._w_ptr
        self._num_of_read_back = 0
        self._w_ptr += 1
        if self._w_ptr >= self._buf_size:
            self._w_ptr = 0
        self._state = "add_item"

    def read_forward(self):
        r = ""
        if self._state == "add_item":
            return ""
        elif self._state == "forward":
            if self._r_ptr != self._index_of_last_added:
                self._num_of_read_forward += 1
                self._increment_r_ptr()
        elif self._state == "backward":
            self._increment_r_ptr()
        r = self._buf[self._r_ptr]
        self._state = "forward"
        return r
    
    def read_backward(self):
        r = ""
        tmp_r_ptr = 0
        tmp_r_ptr = self._r_ptr
        if self._state == "add_item":
            pass
        elif self._state == "backward":
            tmp_r_ptr -= 1
            if tmp_r_ptr < 0:
                tmp_r_ptr = self._buf_size-1
            if self._buf[tmp_r_ptr] == "":
                return self._buf[self._r_ptr]
            if self._num_of_read_back < self._buf_size-1:
                self._num_of_read_back += 1
                self._decrement_r_ptr()
        elif self._state == "forward":
            tmp_r_ptr -= 1
            if tmp_r_ptr < 0:
                tmp_r_ptr = self._buf_size-1
            if self._buf[tmp_r_ptr] == "":
                return self._buf[self._r_ptr]
            self._decrement_r_ptr()
            self._num_of_read_back -= self._num_of_read_forward
        r = self._buf[self._r_ptr]
        self._state = "backward"
        return r

    def clear(self):
        self._buf = [""] * self._buf_size
        self._w_ptr = 0
        self._r_ptr = 0
        self._num_of_items = 0
        self._num_of_read_back = 0
        self._num_of_read_forward = 0
        self._state = "add_item"
    
    def _increment_r_ptr(self):
        self._r_ptr += 1
        if self._r_ptr >= self._buf_size:
            self._r_ptr = 0
    
    def _decrement_r_ptr(self):
        self._r_ptr -= 1
        if self._r_ptr < 0:
            self._r_ptr = self._buf_size-1
    
