# Install blackarch common packages

This script install common packages from blackarch.

The package list comes from [BlackArch/blackarch-iso](https://github.com/BlackArch/blackarch-iso/blob/master/slim-iso/packages.x86_64)

## Prerequisite

BlackArch Linux is compatible with existing/normal Arch installations. It acts as an unofficial user repository. Below you will find instructions on how to install BlackArch in this manner.


```zsh
# Run https://blackarch.org/strap.sh as root and follow the instructions.
$ curl -O https://blackarch.org/strap.sh

# Verify the SHA1 sum
$ echo 8bfe5a569ba7d3b055077a4e5ceada94119cccef strap.sh | sha1sum -c

# Set execute bit
$ chmod +x strap.sh

# Run strap.sh
$ sudo ./strap.sh

# Enable multilib following https://wiki.archlinux.org/index.php/Official_repositories#Enabling_multilib and run:
$ sudo pacman -Syu
```

## Run

```zsh
python main.py
```

## KDE Plasma

If you wanna to generate icon for KDE Plasma, plz refer to [BlackKdeMenu](https://github.com/sakurafisch/BlackarchKdeMenu)