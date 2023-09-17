#!/bin/bash
versao_script="1.0"
# Função para verificar a atualização no arquivo JSON
verificar_atualizacao() {
    # Coloque aqui o caminho completo para o seu arquivo JSON
    arquivo_json="arquivo.json"

    # Faça o download do novo arquivo JSON (substitua a URL pelo seu link)
    wget -q -O novo_json.json https://raw.githubusercontent.com/Interceptv/scanny/main/update.json


    # Obtenha a versão do JSON
    versao_json=$(jq -r '.update' novo_json.json)
    
    linkupdate=$(jq -r '.linkupdate' novo_json.json)

    # Verifique se a versão do JSON é diferente da versão do script
    if [[ "$versao_json" != "$versao_script" ]]; then
        echo "Uma nova versão esta disponível!"
        # Atualize o arquivo local
        
        
        
        
        rm -r update.sh
        
        echo "Updating...."
        
        sleep 5
        
        wget "$linkupdate" && chmod 777 update.sh && ./update.sh
        
        mv novo_json.json "$arquivo_json"
    else
        echo "Seu script esta na versão mais recente."
        # Não há atualização, você pode optar por não fazer nada aqui ou adicionar outra lógica.
    fi

    # Remova o arquivo temporário
    rm -f novo_json.json
}

# Função para exibir o menu
exibir_menu() {
    clear
    echo "===== Menu ====="
    echo "Versão do Script: $versao_script"
    echo "1. Verificar Atualização"
    echo "3. Sair"
    echo "================"
}

# Loop principal
while true; do
    exibir_menu
    read -p "Escolha uma opção: " opcao

    case $opcao in
        1)
            verificar_atualizacao
            ;;
        2)
            # Coloque aqui a lógica para a segunda opção do menu
            ;;
        3)
            echo "Saindo do script."
            exit 0
            ;;
        *)
            echo "Opção inválida. Tente novamente."
            ;;
    esac

    read -p "Pressione Enter para continuar..."
done
