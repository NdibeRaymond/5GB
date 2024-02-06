from pathlib import Path

main_file = Path('./0_100MB.zip')
root = Path('./')

def delete_files():
    for file in root.glob('*.zip'):
        if file.name != main_file.name:
            file.unlink()
            print(f'{file.name} deleted')

def create_files(range):
    for i in range:
        file = root / f'{i}_100MB.zip'
        file.write_bytes(main_file.read_bytes())
        print(f'{file.name} created')

delete_files()
create_files(range(0, 50))
