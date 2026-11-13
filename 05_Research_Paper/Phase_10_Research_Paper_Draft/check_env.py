import sys
import shutil

print("Python:", sys.version)
print("soffice:", shutil.which("soffice"))

try:
    import win32com.client
    print("win32com available")
except ImportError:
    print("win32com NOT available")

try:
    import docx
    print("python-docx available")
except ImportError:
    print("python-docx NOT available")

try:
    import reportlab
    print("reportlab available")
except ImportError:
    print("reportlab NOT available")
