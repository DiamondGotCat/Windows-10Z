$Env:CONDA_EXE = "/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda/bin/conda"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:_CONDA_ROOT = "/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda"
$Env:_CONDA_EXE = "/home/diamondgotcat/windows-10z/includes.chroot/etc/windows/miniconda/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $True}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs