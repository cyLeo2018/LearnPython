# Anaconda概述
- Anaconda是众多Python发行版中的一种
- 具有强大的包管理和环境管理功能
- 完美解决Python2与Python3共存的问题
- 使用conda工具进行管理,与pip功能类似但更强大
    - conda将几乎所有的工具、第三方包都当做packge对待，甚至包括python和conda自身
    
# Anaconda的安装
- [下载地址](https://www.anaconda.com/download/)
- 支持Linux、Mac、Windows
- 安装时选择python2和python3都可以，后续可以进行版本切换

# conda管理(windows)
- conda --version 显示conda版本
- pyton -V        显示python版本
- conda update -n base conda 更新conda版本
- conda update anaconda 更新anaconda版本
- conda update python 更新python版本

### conda环境管理
- 新建的虚拟环境默认在anaconda安装目录下的envs中
- conda env list 显示系统当前存在的环境,标注*的为当前激活环境
    - base环境是anaconda安装后默认生成的基本环境
- conda env remove -n env_name 删除指定的环境env_name
- conda create --name env_name python=2.7 创建虚拟环境env_name，指定python2.7版本
- conda create --name env_name package_name 创建虚拟环境同时安装指定包
- activate env_name 激活环境
    - source activate env_name (Linux)
- deactivate 关闭环境
    -- source deactivate (Linux)
- conda env export > enviroment_name.yaml 导出虚拟环境
- conda env import < enviroment_name.yaml 导入虚拟环境

### conda包管理
> conda -n env_name 指定环境进行包操作
- conda list 显示所有已安装包信息
- conda list -n env_name 显示指定环境内安装的包
- conda upgrade -all 更新所有包
- conda install package_name=package_version 安装包，指定包名和版本，默认包是安装在当前激活的环境内
- conda install -n env_name package_name 安装包到指定的环境
- conda install nb_conda 安装nb_conda用于notebook自动关联nb_conda环境 ？？
- conda remove package_name 卸载包
- conda update package_name 更新指定包
- conda search package_name 搜索指定包信息

# 设置国内镜像
- [清华大学anaconda镜像站](https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/)
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
- conda config --set show_channel_urls yes
- 命令实际是修改配置文件C:\Users\用户\.condarc (windows) ~/.condarc (Linux)

# conda配置管理
- conda config --show
- conda config --show-sources
- conda config --validate
- conda config --describe
- conda config --write-default
- conda config --get
- conda config --append
- conda config --prepend
- conda config --add 
- conda config --set
- conda config --remove
- conda config --remove-key
- conda config --stdin
