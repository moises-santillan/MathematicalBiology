```
wget https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.1-linux-x86_64.tar.gz
```

```
tar -xvzf julia-1.8.1-linux-x86_64.tar.gz
```

```
rm julia-1.8.1-linux-x86_64.tar.gz
```

```
mv julia-1.8.1 .local/share
```

```
echo 'export PATH="$HOME/.local/share/julia-1.8.1/bin/:$PATH"' | cat >> .bashrc 
```

```
julia
```

```
using Pkg
```

```
Pkg.add("IJulia")
```

```
using IJulia
```

```
exit()
```

```
cp -r .local/share/jupyter/kernels/julia-1.8 .conda/envs/default/share/jupyter/kernels/
```