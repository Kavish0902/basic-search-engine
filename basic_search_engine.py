import os

def search_files(keyword, directory):
    results = []
    
    # Iterate through each file in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Only search in text files
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    if keyword.lower() in line.lower():  # Case insensitive search
                        results.append(f"{filename} (Line {line_number}): {line.strip()}")
    
    return results

def main():
    directory = input("Enter the directory path containing your text files: ")
    keyword = input("Enter the keyword to search for: ")
    
    if not os.path.exists(directory):
        print("The specified directory does not exist.")
        return
    
    results = search_files(keyword, directory)
    
    if results:
        print(f"\nFound {len(results)} result(s):\n")
        for result in results:
            print(result)
    else:
        print("\nNo results found.")

if __name__ == "__main__":
    main()
