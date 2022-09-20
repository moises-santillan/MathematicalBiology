# Instructions to install *Julia* in AWS studiolab


After starting and opening your project, open a terminal and type the following  to download *Julia*'s files:
```
wget https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.1-linux-x86_64.tar.gz
```

Then, you need to expand the downloaded file by typing:
```
tar -xvzf julia-1.8.1-linux-x86_64.tar.gz
```

Erase the compressed file to save space:
```
rm julia-1.8.1-linux-x86_64.tar.gz
```

Move the expanded directory containing *Julia*'s files to the right place:
```
mv julia-1.8.1 .local/share
```

Add a line to *.bashrc* file so linux knows where to fine *Julia*'s executable file:
```
echo 'export PATH="$HOME/.local/share/julia-1.8.1/bin/:$PATH"' | cat >> .bashrc 
```

Close the current terminal an open a new one so that file .bashrc is executed. Then, open *Julia*:
```
julia
```

Within *Julia* load *Pkg* package:
```
using Pkg
```

Use *Pkg* to add package *IJulia*, which allows *Julia* to interact with *Jupyter*
```
Pkg.add("IJulia")
```

Load *IJulia* to create *Juñia*'s *Jupyter* kernel:
```
using IJulia
```

Exit *Julia*:
```
exit()
```

Within the linux command window run the following command to copy *Julia*'s kernel to the correct place:
```
cp -r .local/share/jupyter/kernels/julia-1.8 .conda/envs/default/share/jupyter/kernels/
```

You should be able now to open, create, and run *Jupyter* notebooks with *Julia*.