import os

#Get the api keys for necessary services

def get_api_key(service):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # base working directory
    api_file_path = os.path.join(base_dir,"api","api.txt")
    with open(api_file_path, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0]== service:
                return parts[1].strip()
        raise ValueError(f"API key for service '{service}' not found")
