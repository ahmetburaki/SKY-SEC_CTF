#sudo docker build -t <name:tag> .
#sudo docker run -p <local_port>:22 --rm --security-opt seccomp=unconfined -d --name rop-ctf -i <name:tag>


FROM ubuntu:22.04
ENV LC_CTYPE C.UTF-8
ENV DEBIAN_FRONTEND=interactive

RUN dpkg --add-architecture i386 && \
apt-get update && \
apt-get install -y build-essential jq strace ltrace openssh-server hexedit curl wget nano rubygems gcc dnsutils netcat gcc-multilib net-tools vim gdb gdb-multiarch python3 python3-pip python3-dev libssl-dev libffi-dev wget git make procps libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:amd64 libncurses5:amd64 libstdc++6:amd64 && \
mkdir tools && cd tools && \
git clone https://github.com/JonathanSalwan/ROPgadget

RUN apt-get install -y systemctl

RUN useradd -d /home/skysec/ -m -p skysec -s /bin/bash skysec
RUN echo "skysec:skysec" | chpasswd

WORKDIR /

COPY flag .

RUN chown root:root /flag && chmod 400 /flag

WORKDIR /home/skysec

COPY PWN-BOF.c .

RUN gcc -fPIE -pie -fstack-protector-all PWN-BOF.c -o challenge && chown root:root challenge && \
chmod u+s challenge && rm -rf PWN-BOF.c

USER skysec

RUN python3 -m pip install pwntools keystone-engine unicorn capstone

USER root

RUN echo "root:orada_burada_dolasan_adam" | chpasswd

RUN mkdir /var/run/sshd && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "export VISIBLE=now" >> /etc/profile


EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]