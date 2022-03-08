import os

def main() -> None:
    with open('packages', 'r') as file:
        for line in file:
            tmp: str = ""
            for x in line:
                if x != '\n':
                    tmp += x
            os.system(f'echo "y" | sudo pacman -S {tmp}')

if __name__ == '__main__':
    main()
