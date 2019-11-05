apt-get remove docker \
docker-engine \
docker.io

curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | apt-key add -

add-apt-repository \
"deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
$(lsb_release -cs) \
stable"

apt-get remove docker \
docker-engine \
docker.io

apt-get install docker-ce

cat>/etc/docker/daemon.json<<EOF
{
    "registry-mirrors": [
        "http://af4d232c.m.daocloud.io"
    ],
    "insecure-registries": []
}
EOF

service docker restart

groupadd docker
usermod -aG docker $USER

docker run hello-world