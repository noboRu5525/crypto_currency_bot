FROM ubuntu:latest

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y wget && \
    apt-get install -y python3 && \
    apt-get install -y vim && \
    apt-get install -y git && \
    apt-get install -y python3-pip && \
    apt-get install -y locales && \
    apt-get install -y tmux && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ロケールを設定
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# tmuxの設定ファイルをコピー
COPY tmux.conf /root/.tmux.conf

# TA-Libのビルドとインストール
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -zxvf ta-lib-0.4.0-src.tar.gz && \
    rm ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    cd .. && \
    rm -r ta-lib


# 必要なPythonライブラリをインストール
COPY requirements.txt .

# 必要なPythonパッケージのインストール
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# データの永続化のためのディレクトリ作成
RUN mkdir -p /home/ubuntu
WORKDIR /home/ubuntu

# COPY .env /home/ubuntu/.env

CMD ["bash"]


