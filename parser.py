import struct

class LuaBytecodeReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.pos = 0

    def read_file(self):
        with open(self.filepath, "rb") as f:
            self.data = f.read()
        self.pos = 0

    def read_bytes(self, n):
        result = self.data[self.pos:self.pos+n]
        self.pos += n
        return result

    def read_byte(self):
        return self.read_bytes(1)[0]

    def read_int(self):
        return struct.unpack("<I", self.read_bytes(4))[0]

    def read_size_t(self):
        return self.read_int()  # đơn giản: giả định size_t = 4 bytes

    def read_string(self):
        size = self.read_size_t()
        if size == 0:
            return ""
        return self.read_bytes(size-1).decode('utf-8')  # bỏ byte null cuối

    def read_header(self):
        signature = self.read_bytes(4)
        if signature != b'\x1bLua':
            raise ValueError("Không phải file Lua bytecode")
        version = self.read_byte()
        format_version = self.read_byte()
        endianness = self.read_byte()
        int_size = self.read_byte()
        size_t_size = self.read_byte()
        instruction_size = self.read_byte()
        lua_integer_size = self.read_byte()
        lua_number_size = self.read_byte()
        integral_flag = self.read_byte()
        return {
            "version": version,
            "format_version": format_version,
            "endianness": endianness,
            "int_size": int_size,
        }
