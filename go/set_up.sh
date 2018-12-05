#!/bin/bash -e
if [ "$#" -ne 1 ]; then
  echo "Must specify the following argument <go_version>"
  exit 1
fi

go_version=$1

echo $go_version

echo "Download Go version ${go_version} ..."
curl -O https://storage.googleapis.com/golang/go1.${go_version}.linux-amd64.tar.gz

tar -xvf go1.${go_version}.linux-amd64.tar.gz

sudo chown -R root:root ./go
sudo mv go /usr/local

cat > ~/.profile << EOF 
GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
EOF

source ~/.profile

echo "Clean up ..."
rm -r go1.${go_version}.linux-amd64.tar.gz

echo "Check install ..."
go version
