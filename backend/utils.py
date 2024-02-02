import subprocess
import re


def get_external_ip():
    try:
        result = subprocess.check_output(["curl", "ifconfig.me"])
        external_ip = result.decode("utf-8").strip()
        return external_ip
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


def get_public_IPv4_DNS(ip):
    try:
        result = subprocess.check_output(["dig", "-x", ip], universal_newlines=True)
        regex = r"((?:[a-zA-Z0-9-]+\.){2,}[a-zA-Z0-9-]+\.amazonaws\.com)"
        match = re.search(regex, result)
        if match:
            return match.group(1)
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
