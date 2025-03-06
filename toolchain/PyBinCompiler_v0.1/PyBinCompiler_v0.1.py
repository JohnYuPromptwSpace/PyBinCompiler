import sys
import os
import json

class PyBinCompiler():
    TABLE = binary_to_char = {
                "0100000": "space",
                "0100001": "!",
                "0100010": '"',
                "0100011": "#",
                "0100100": "$",
                "0100101": "%",
                "0100110": "&",
                "0100111": "'",
                "0101000": "(",
                "0101001": ")",
                "0101010": "*",
                "0101011": "+",
                "0101100": ",",
                "0101101": "-",
                "0101110": ".",
                "0101111": "/",
                "0110000": "0",
                "0110001": "1",
                "0110010": "2",
                "0110011": "3",
                "0110100": "4",
                "0110101": "5",
                "0110110": "6",
                "0110111": "7",
                "0111000": "8",
                "0111001": "9",
                "0111010": ":",
                "0111011": ";",
                "0111100": "<",
                "0111101": "=",
                "0111110": ">",
                "0111111": "?",
                "1000000": "@",
                "1000001": "A",
                "1000010": "B",
                "1000011": "C",
                "1000100": "D",
                "1000101": "E",
                "1000110": "F",
                "1000111": "G",
                "1001000": "H",
                "1001001": "I",
                "1001010": "J",
                "1001011": "K",
                "1001100": "L",
                "1001101": "M",
                "1001110": "N",
                "1001111": "O",
                "1010000": "P",
                "1010001": "Q",
                "1010010": "R",
                "1010011": "S",
                "1010100": "T",
                "1010101": "U",
                "1010110": "V",
                "1010111": "W",
                "1011000": "X",
                "1011001": "Y",
                "1011010": "Z",
                "1011011": "[",
                "1011100": "\\",
                "1011101": "]",
                "1011110": "^",
                "1011111": "_",
                "1100000": "`",
                "1100001": "a",
                "1100010": "b",
                "1100011": "c",
                "1100100": "d",
                "1100101": "e",
                "1100110": "f",
                "1100111": "g",
                "1101000": "h",
                "1101001": "i",
                "1101010": "j",
                "1101011": "k",
                "1101100": "l",
                "1101101": "m",
                "1101110": "n",
                "1101111": "o",
                "1110000": "p",
                "1110001": "q",
                "1110010": "r",
                "1110011": "s",
                "1110100": "t",
                "1110101": "u",
                "1110110": "v",
                "1110111": "w",
                "1111000": "x",
                "1111001": "y",
                "1111010": "z",
                "1111011": "{",
                "1111100": "|",
                "1111101": "}",
                "1111110": "~",
                "1111111": "DEL"
            }
    
    HELP_MESSAGE = """
Hello, welcome to PyBinCompiler!

Usage:
    python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?> <make file?> <TargetFileName>.txt <FileName>.py

Arguments:
    <run?>           (bool: True | False)  
                    - If True, the compiled Python code will be executed immediately.  
                    - If False, the compiled code will not run.

    <make file?>     (bool: True | False)  
                    - If True, the compiled Python code will be saved as a .py file.  
                    - If False, no output file will be created.

    <TargetFileName>.txt  
                    - The name of the text file containing binary code.  
                    - This file should be located in the current directory.

    <FileName>.py  
                    - (Optional) The name of the output Python file if <make file?> is set to True.  
                    - If not specified, the default name "untitled.py" will be used.

Examples:
    1. Run compiled code but do not save:
    python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True False my_binary.txt

    2. Save compiled code as a file but do not run:
    python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py False True my_binary.txt output.py

    3. Run compiled code and save it as a file:
    python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True True my_binary.txt output.py

    4. Missing arguments (will cause an error):
    python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True True
"""
    
    class LengthValidationError(Exception):
        """Exception raised for invalid code length."""
        def __init__(self, length):
            self.value = length
            super().__init__(f"Invalid code length: {length}. The length must be a multiple of 7.")

    class InvalidKeywordError(Exception):
        """Exception raised for using an invalid or non-existent reserved keyword."""

        def __init__(self, keyword):
            super().__init__(f"Invalid keyword: '{keyword}'. The specified reserved keyword does not exist.")
            self.keyword = keyword
    
    class PathNotFoundError(Exception):
        """Exception raised when a specified file path does not exist."""

        def __init__(self, path):
            super().__init__(f"Path not found: '{path}'. Please check if the file exists and the path is correct.\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")
            self.path = path
        
    class MissingFileError(Exception):
        """Exception raised when the required file is missing in the command."""
        
        def __init__(self):
            super().__init__(f"Error: No file specified for compilation. Please provide a valid filename. Try typing in the following format.\n\n'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?: bool(True, False> <make file?: bool(True, False> <TargetFileName>.txt <FileName>.py'\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")

    class InvalidRunOptionError(Exception):
        """Exception raised when the 'run' option is missing or invalid."""
        
        def __init__(self, input__):
            if input__ == None:
                super().__init__(f"Error: The 'run' option must be explicitly set to True or False: None. Try typing in the following format.\n\n'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?: bool(True, False> <make file?: bool(True, False> <TargetFileName>.txt <FileName>.py'\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")
            else:
                super().__init__(f"Error: The 'run' option must be explicitly set to True or False: '{input__}'. Try typing in the following format.\n\n'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?: bool(True, False> <make file?: bool(True, False> <TargetFileName>.txt <FileName>.py'\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")
            
    class InvalidMakeFileOptionError(Exception):
        """Exception raised when the 'makeFile' option is missing or invalid."""
        
        def __init__(self, input__):
            if input__ == None:
                super().__init__(f"Error: The 'make file' option must be explicitly set to True or False: None. Try typing in the following format.\n\n'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?: bool(True, False> <make file?: bool(True, False> <TargetFileName>.txt <FileName>.py'\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")
            else:
                super().__init__(f"Error: The 'make file' option must be explicitly set to True or False: '{input__}'. Try typing in the following format.\n\n'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?: bool(True, False> <make file?: bool(True, False> <TargetFileName>.txt <FileName>.py'\n\nType 'python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help' for more.")

    def __init__(self):
        if len(sys.argv) < 2 or sys.argv[1] not in ("True", "False"):
            if sys.argv[1] == "help":
                print(PyBinCompiler.HELP_MESSAGE)
                return
            else:
                raise PyBinCompiler.InvalidRunOptionError(sys.argv[1] if len(sys.argv) > 1 else "None")

        if len(sys.argv) < 3 or sys.argv[2] not in ("True", "False"):
            raise PyBinCompiler.InvalidMakeFileOptionError(sys.argv[2] if len(sys.argv) > 2 else "None")

        if len(sys.argv) < 4:
            raise PyBinCompiler.MissingFileError()
        
        TITLE = self.setTitle()
        
        CONTENT, CONTENT_LENGTH = self.load_content()
        
        COMPILDE_CODE = self.compile(CONTENT, CONTENT_LENGTH)
        
        if bool(sys.argv[1]):
            self.runCode(COMPILDE_CODE)
            
        if bool(sys.argv[2]):
            self.writeCode(TITLE, COMPILDE_CODE)
    
    def setTitle(self):
        try:
            return sys.argv[4]
        except:
            return "untitled"
    
    def load_content(self):
        PATH = os.getcwd() + "\\" + sys.argv[3]

        try:
            with open(PATH, "r", encoding="utf-8") as file:
                content = file.read()
        except:
            raise PyBinCompiler.PathNotFoundError(PATH)

        content_length = len(content)
        
        return content, content_length

    def compile(self, CONTENT, CONTENT_LENGTH):
        if (CONTENT_LENGTH % 7):
            raise PyBinCompiler.LengthValidationError(CONTENT_LENGTH)

        CURSOR = 0  
        COMPILDE_CODE = ""

        while (CURSOR < CONTENT_LENGTH):
            CURR_KEYWORD = CONTENT[CURSOR:CURSOR+7]
            
            try:
                CURR_COMPILED_KEYWORD = PyBinCompiler.TABLE[CURR_KEYWORD]
                
                if CURR_COMPILED_KEYWORD == "space":
                    CURR_COMPILED_KEYWORD = " "
                elif CURR_COMPILED_KEYWORD == ";":
                    CURR_COMPILED_KEYWORD = "\n"
                
                COMPILDE_CODE += CURR_COMPILED_KEYWORD
            except:
                raise PyBinCompiler.InvalidKeywordError(CURR_KEYWORD)
            
            CURSOR += 7

        return COMPILDE_CODE

    def writeCode(self, TITLE, COMPILDE_CODE):
        PATH = os.getcwd() + f"\\build\\{TITLE}.py"
        DIR = os.path.dirname(PATH)

        if not os.path.exists(DIR):
            os.makedirs(DIR)
        
        with open(PATH, "w", encoding="utf-8") as file:
            file.write(COMPILDE_CODE)

        print(f"Finished compiling '{sys.argv[3]}' Made file '{TITLE}.py' at '{PATH}'")
    
    def runCode(self, COMPILDE_CODE):
        exec(json.loads(json.dumps(COMPILDE_CODE)))


if __name__ == "__main__":
    PyBinCompiler()