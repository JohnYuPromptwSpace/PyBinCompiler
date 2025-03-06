# 🏗️ PyBinCompiler

**PyBinCompiler** is a binary-to-Python compiler that translates binary-encoded text into executable Python scripts. It allows users to run compiled code directly or save it as a Python file.

## 📌 Features
- ✅ Convert **binary-encoded text** into Python source code.
- ✅ **Run** compiled code instantly.
- ✅ **Save** compiled Python code as a `.py` file.
- ✅ **Error handling** for missing or invalid arguments.
- ✅ Supports **custom file naming** for output.

---

## 🚀 Usage

### **Command Format**
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py <run?> <make file?> <TargetFileName>.txt <FileName>.py```

### **Arguments:**
| Argument | Type | Description |
|----------|------|-------------|
| `<run?>` | `bool` | If `True`, executes the compiled code immediately. If `False`, the code is not executed. |
| `<make file?>` | `bool` | If `True`, saves the compiled code as a `.py` file. If `False`, no file is created. |
| `<TargetFileName>.txt` | `str` | The name of the text file containing binary code. |
| `<FileName>.py` | `str (optional)` | The name of the output Python file (if `<make file?>` is `True`). Defaults to `"untitled.py"` if not specified. |

---

## 🔹 Example Usage

### ✅ Explanation:
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py help
```


### ✅ Run compiled code but do not save:
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True False my_binary.txt
```

### ✅ Save compiled code as a `.py` file but do not run:
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py False True my_binary.txt output.py
```

### ✅ Run compiled code and save it as a `.py` file:
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True True my_binary.txt output.py
```

### ❌ Missing arguments (will cause an error):
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True True
```
**Error:** `"Missing file argument. Please provide a valid .txt file."`

---

## 📂 Project Structure

```
📦 PyBinCompiler
 ┣ 📂 toolchain
 ┃ ┣ 📂 PyBinCompiler_v0.1
 ┃ ┃ ┣ 📜 PyBinCompiler_v0.1.py # Main compiler script
 ┃ ┃ ┣ 📜 PyBinCompiler Version 0.1 Standard # Binary Code Information
 ┣ 📂 build # Compiled Python files
 ┣ 📜 README.MD # Documentation
```

---

## ⚠️ Exception Handling
PyBinCompiler includes built-in exception handling for various cases:

| Exception | Condition |
|-----------|-----------|
| `InvalidRunOptionError` | `<run?>` must be `True` or `False`. |
| `InvalidMakeFileOptionError` | `<make file?>` must be `True` or `False`. |
| `MissingFileError` | No input `.txt` file provided. |
| `PathNotFoundError` | The specified file path does not exist. |
| `InvalidKeywordError` | The binary code contains an invalid sequence. |0
| `LengthValidationError` | Binary code length is not a multiple of 7. |

---

## 🛠 Installation
To use PyBinCompiler, clone the repository:
```bash
git clone https://github.com/JohnYuPromptwSpace/PyBinCompiler
```

Run the compiler with:
```bash
python toolchain/PyBinCompiler_v0.1/PyBinCompiler_v0.1.py True True my_binary.txt output.py
```

---

## 🤝 Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a Pull Request!0

---

## 📜 License
This project is licensed under the MIT License
