mkdir ~/.pip

cat>~/.pip/pip.conf<<EOF
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
EOF

source ~/.pip/pip.conf