from .parser import LuaBytecodeReader

class LuaDecompiler:
    def __init__(self, filepath):
        self.reader = LuaBytecodeReader(filepath)
        self.reader.read_file()

    def decompile(self):
        header = self.reader.read_header()
        lua_version = header['version']
        # demo đơn giản: chỉ xuất header
        output = f"-- Lua {lua_version} bytecode decompiled\n"
        output += "-- Full decompilation not implemented in demo\n"
        return output
