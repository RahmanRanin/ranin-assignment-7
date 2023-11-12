def process_text(file_path):
    unique_words = []
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                
                if word not in unique_words:
                    unique_words.append(word)

    unique_words.sort()
    print(unique_words)

def main():
    romeo_file_path = 'path/to/your/romeo.txt'  
    process_text(romeo_file_path)

if __name__ == "__main__":
    main()
