import platform
import os

def get_processor_info():
    print("\n=== Processor Information ===")
    
    # Basic CPU information
    print("\n1. Basic CPU Info:")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    
    # CPU architecture
    print("\n2. CPU Architecture:")
    print(f"Architecture: {platform.architecture()}")
    print(f"Machine: {platform.machine()}")
    
    # Try to get CPU information from /proc/cpuinfo on Linux
    if platform.system() == "Linux":
        try:
            with open("/proc/cpuinfo", "r") as f:
                cpuinfo = f.readlines()
            
            print("\n3. Detailed CPU Information:")
            for line in cpuinfo:
                if "model name" in line:
                    print(f"CPU Model: {line.split(':')[1].strip()}")
                    break
                
            core_count = 0
            for line in cpuinfo:
                if "processor" in line:
                    core_count += 1
            print(f"Number of Cores: {core_count}")
                    
        except Exception as e:
            print(f"Could not read detailed CPU info: {e}")

if __name__ == "__main__":
    try:
        get_processor_info()
    except Exception as e:
        print(f"An error occurred: {e}")