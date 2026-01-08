import subprocess

# Ejecuciones Script
cmd = [
    "powershell",
    "-Command",
    "(Get-CimInstance Win32_UserAccount -Filter \"Name='$env:USERNAME'\").FullName"
]

# Variables Globales
username = subprocess.check_output(cmd, text=True).strip()