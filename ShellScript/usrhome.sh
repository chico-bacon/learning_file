#!/bin/bash

echo "========================HOME DOS USUARIOS==========================="
echo ""
UT=$(whoami)
DIRETORIO="/home/"

for ARQUIVO in $DIRETORIO*
do
  SAIDA=$(echo $ARQUIVO |sed -nre "s:^.*/(.*)$:\1:p")
  echo "$SAIDA => $ARQUIVO"
done
echo ""

