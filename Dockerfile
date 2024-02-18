FROM python:3.10

# codeというディレクトリを作成し、そこを作業フォルダとする
WORKDIR /code

# mecabの導入
RUN apt-get -y update && \
  apt-get -y upgrade && \
  apt-get install -y mecab && \
  apt-get install -y libmecab-dev && \
  apt-get install -y mecab-ipadic-utf8 && \
  apt-get install -y git && \
  apt-get install -y make && \
  apt-get install -y curl && \
  apt-get install -y xz-utils && \
  apt-get install -y file && \
  apt-get install -y sudo

# mecab-ipadic-NEologdのインストール
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
  cd mecab-ipadic-neologd && \
  ./bin/install-mecab-ipadic-neologd -n -y && \
  echo dicdir = `mecab-config --dicdir`"/mecab-ipadic-neologd">/etc/mecabrc && \
  sudo cp /etc/mecabrc /usr/local/etc && \
  cd ..

# requirements.txtをcode内に移動
COPY requirements.txt requirements.txt
# requirements.txtの中のライブラリをinstallする
RUN pip install -U pip
RUN pip install -r requirements.txt
# すべてのファイルをcode内にマウントする。
COPY . .

# $PORTを指定しないと動かないので注意
CMD gunicorn -b 0.0.0.0:$PORT app:app --log-file=-
