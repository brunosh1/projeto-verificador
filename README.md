Verificador de Status de Sites
Esse projeto foi criado para praticar e aplicar conhecimentos de Python, HTML, CSS e JavaScript de forma integrada. A ideia é simples: verificar se alguns sites estão online e mostrar essa informação tanto no terminal quanto em uma página da web.

O que esse projeto faz
Lê uma lista de sites definida por você (no arquivo sites.txt).

Verifica se cada um está acessível (se responde com status 200 ou erro).

Mostra os resultados no terminal e grava tudo em um arquivo chamado monitoramento.log.

Gera também um arquivo resultados.json com os dados organizados.

Exibe essas informações de forma visual e colorida em uma página HTML.

Permite que você digite uma URL na página e veja se ela está online.

Por que esse projeto é interessante
Quis criar algo prático e que ao mesmo tempo me ajudasse a entender melhor:

Como fazer requisições HTTP em Python (com a biblioteca requests)

Como ler e gravar arquivos de texto e JSON

Como montar uma interface web com HTML e CSS

Como usar JavaScript para interatividade na página

Como exibir dados atualizados direto no navegador

Além disso, é um projeto leve, útil e fácil de testar no dia a dia.

Como usar
Baixe o projeto (ou clone pelo GitHub).

Instale a biblioteca requests com o comando pip install requests.

No arquivo sites.txt, adicione os sites que quer monitorar (um por linha).

Execute o script verificador.py. Ele vai mostrar os resultados e criar os arquivos monitoramento.log e resultados.json.

Para visualizar os dados no navegador, execute um servidor local com python -m http.server e abra o endereço http://localhost:8000.

Obs: se você abrir o arquivo index.html com duplo clique, o navegador pode bloquear a leitura do JSON por segurança. Por isso o uso do servidor local é recomendado.

Estrutura do projeto
verificador.py — script Python que verifica os sites

sites.txt — lista com os sites que serão verificados

monitoramento.log — log com o status e a hora de cada verificação

resultados.json — arquivo com os resultados formatados em JSON

index.html — página web para exibir os dados

style.css — estilos para a página

Possíveis melhorias no futuro
Criar uma versão com Flask para tornar o projeto totalmente web.

Rodar a verificação automaticamente a cada X minutos.

Enviar e-mails ou alertas se algum site estiver fora do ar.

Adicionar filtros e buscas na página.

Considerações finais
Esse projeto foi uma forma de unir o aprendizado de backend com frontend, com uma aplicação real e simples. Foi ótimo para fixar os conceitos de programação, estrutura de arquivos e interação com a web. Ainda pode crescer bastante com melhorias futuras.

Se quiser ver o código ou colaborar, fique à vontade!
