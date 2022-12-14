#!/bin/bash

OP=0
echo "=============OPERAÇÕES ARITIMÉTICAS==============="
echo ""
read -p "Digite o primeiro valor: " NUM1
echo ""
read -p "Digite o segundo valor: " NUM2
echo ""
echo "Escolha a operação que deseja fazer"
echo ""
echo "[ 1 ] Soma\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão"
echo ""
read -p "Digite sua opção: " OP
if [ $OP -eq 1 ]
then
RESULTADO=$(($NUM1+$NUM2))
elif [ $OP -eq 2 ]
then
RESULTADO=$(($NUM1-$NUM2))
elif [ $OP -eq 3 ]
then
RESULTADO=$(($NUM1*$NUM2))
elif [ $OP -eq 4 ]
then
RESULTADO=$(($NUM1/$NUM2))
else
echo "OPÇÃO INVÁLIDA!!!"
RESULTADO="NADA"
fi
echo "O resultado é $RESULTADO"

