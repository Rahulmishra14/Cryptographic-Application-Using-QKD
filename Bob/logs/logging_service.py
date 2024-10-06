COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[95m', # Magenta
        'RESET': '\033[0m'      # Reset color
}

def generateLogs(message, severity='INFO'):
    color = COLORS.get(severity, COLORS['INFO'])
    reset = COLORS['RESET']
    print(f"[QKD::Alice]::--------{color}[{severity}] {message}{reset}--------")
