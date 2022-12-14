#!/bin/bash

USUARIO=''
ARQUIVO1="/home/"
ARQUIVO2="/etc/passwd"

read -p "Informe o nome do usuario: " USUARIO

RESULTADO1=$(ls $ARQUIVO1 |grep -i $USUARIO)
RESULTADO2=$(cat $ARQUIVO2 |grep -i $USUARIO)

if [ -z $RESULTADO1 ]
then
echo "o usuario $USUARIO NÃO existe"
else
echo "O usuario $USUARIO existe"
fi

if [ -z $RESULTADO2 ]
then
echo "o usuario $USUARIO NÃO existe"
else
echo "O usuario $USUARIO existe"
fi

echo $RESULTADO1
echo $RESULTADO2
