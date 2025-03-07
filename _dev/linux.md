

**Fish**

```sh
sudo add-apt-repository ppa:fish-shell/release-4
sudo apt update
sudo apt install fish
```

将 Fish 添加到系统认可的 Shell 列表:

```sh
# 查看 Fish 的安装路径（通常为 /usr/bin/fish）
which fish

# 将路径添加到 /etc/shells
echo /usr/bin/fish | sudo tee -a /etc/shells
```

设置 Fish 为默认 Shell:

```sh
chsh -s /usr/bin/fish
```


**just**

```sh
curl -LSfs https://just.systems/install.sh | sh -s -- --to /usr/local/bin
```



**Miniconda**

```sh
wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh
```

初始化 Conda

```sh
conda init "$(basename "${SHELL}")"

# conda init bash
# conda init fish
```
