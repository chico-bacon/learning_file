#!/bin/bash

echo "==============================RANKING MELHOR BASH=========================="
ARQUIVO="/etc/passwd"
RESULTADO1=$(grep -c /bin/sh $ARQUIVO)
RESULTADO2=$(grep -c /bin/bash $ARQUIVO)
echo ""
echo "/bin.sh => $RESULTADO1 usuarios."
echo ""
echo "/bin/.bash => $RESULTADO2 usuarios."
