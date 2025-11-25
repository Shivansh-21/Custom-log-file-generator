import os
from datetime import datetime

if not os.path.exists("logs"):
    os.mkdir("logs")

log_filename = f"logs/log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt"

def write_log(level, message):
    """Writes log with timestamp and level"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level.upper()}] {message}\n"
    
    with open(log_filename, "a") as file:
        file.write(log_line)
    print("Log entry added.")

def main():
    print("\n Custom Log File Generator (AI-Grade Project) \n")
    
    while True:
        print("Enter log details below:")
        level = input("Log Level (info/warning/error/debug): ").strip().lower()
        message = input("Log Message: ").strip()
        
        if level not in ["info", "warning", "error", "debug"]:
            print("Invalid level! Please enter again.")
            continue

        write_log(level, message)

        cont = input("Do you want to add another log? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

    print(f"\n Log saved at: {log_filename}\n Logging complete.")

if __name__ == "__main__":
    main()
