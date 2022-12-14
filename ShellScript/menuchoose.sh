#!/bin/bash

OPCAO=0
while [ $OPCAO -ne 4 ]
do
  echo "=============================MENU DE OPÇÕES============================"
  echo ""
  echo "[ 1 ] Exibir status da utilização das partições do sistema\n[ 2 ] Exibir relação de usuarios logados\n[ 3 ] Exibir data/hora\n[ 4 ] Sair"
  echo ""
  echo ""
  read -p "Digite sua opção: " OPCAO
  if [ $OPCAO -eq 1 ]
  then
  echo "================STATUS DE PARTIÇÕES==================="
  echo ""
  df -h
  elif [ $OPCAO -eq 2 ]
  then
    echo "================USUARIOS LOGADOS==================="
    echo ""
    RESULTADO=$(who)
    echo ""
  elif [ $OPCAO -eq 3 ]
  then
    echo "=================HORARIO ATUAL====================="
    HORARIO=$(date +%H:%M)
    DATA=$(date +%D)
    echo "Horario: $HORARIO"
    echo "Data atual: $DATA"
  else
    echo ""
    echo "OPÇÃO INVÁLIDA!!!"
    echo ""
fi
done
echo ""
echo "TCHAU!"
