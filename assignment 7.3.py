def read_mbox(file_path):
    senders = []
    with open(file_path, 'r') as mbox_file:
        for line in mbox_file:
            if line.startswith('From '):
                
                sender = line.split()[1]
                senders.append(sender)
    return senders

def main():
    mbox_file_path = 'path/to/your/mbox/file.mbox'  
    senders = read_mbox(mbox_file_path)

    
    for sender in senders:
        print(sender)

    
    print(f'Total {len(senders)} lines were printed')

if __name__ == "__main__":
    main()
