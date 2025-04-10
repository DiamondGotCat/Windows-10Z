export MAMBA_ROOT_PREFIX="/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda"
__mamba_setup="$("/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda/bin/mamba" shell hook --shell posix 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda/bin/mamba"  # Fallback on help from mamba activate
fi
unset __mamba_setup
