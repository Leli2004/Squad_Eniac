## Orientações para exercícios e desafio (em squad)
## Semana 5

### Exercícios API
#### Consumo de API com Flask

O seriado Rick and Morty é um desenho animado americano de comédia e ficção científica criado por Justin Roiland e Dan Harmon para o bloco de programação noturno Adult Swim, exibido no canal Cartoon Network. A série acompanha as perigosas aventuras do cientista louco Rick e seu neto Morty, que divide seu tempo entre a vida familiar e viagens interdimensionais. A série é inspirada em Back to the Future e Doctor Who.

A API do Rick and Morty é uma API pública que contém informações sobre os personagens da série. A documentação da API pode ser encontrada em: https://rickandmortyapi.com/documentation/#rest

DEFINIÇÕES:
- A API possui três endpoints: um para listar os personagens, um para listar as localizações e dimensões e um para listar os episódios. Durante
a aula, utilizamos apenas o endpoint de personagens. 

- O objetivo deste exercício é adicionar novas funcionalidades ao projeto. Você deverá adicionar uma página para listar as localizações e os
episódios, além de melhorar a página de perfil do personagem.

Para isso, você deverá: 
1. Criar uma nova rota para listar as localizações. A rota deverá ser acessível através do caminho /locations. A página deverá ser renderizada através do template locations.html. A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão. A tabela deverá conter um link para a página de perfil da localização

2. Criar uma nova rota para listar os episódios. A rota deverá ser acessível através do caminho /episodes. A página deverá ser renderizada através do template episodes.html. A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código. A tabela deverá conter um link para a página de perfil do episodio.

3. Criar uma nova rota para exibir o perfil da localização. A rota deverá ser acessível através do caminho /location/<id>. A página deverá ser renderizada através do template location.html. A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os  ersonagens que aparecem na localização. A lista deverá conter um link para a página de perfil do personagem.

4. Criar uma nova rota para exibir o perfil do episódio. A rota deverá ser acessível através do caminho /episode/<id>. A página deverá
ser renderizada através do template episode.html. A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que aparecem no episódio. A lista deverá conter um link para a página de perfil do personagem.

5. Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. As informações de origem, localização e episódios em que o personagem aparece devem conter um link para a página de perfil da localização.


### Desafio Rick and Morty

#### Sobre a apresentação:
A apresentação terá 5 minutos de duração para cada squad e ao menos duas integrantes devem apresentar, mas todas precisam participar da resolução dos exercícios. Uma das integrantes também deve compartilhar a tela para apresentar com  o desafio do Google Colab ou slide. 
Sugerimos que realizem um ensaio previamente e façam a melhor gestão do tempo. 

Vocês devem explicar na apresentação:
1. A lógica utilizada para a solução do desafio;
2. Explicar como a squad se organizou;
3. As facilidades e dificuldades encontradas no desenvolvimento do desafio.

A explicação do código não precisa ser 'linha a linha', mas pode ser por 'blocos'.

Data: 01/03
Horário: 19h00

FORMULÁRIO DE ENTREGA
- A squad deve indicar dentro do formulário disponibilizado os nomes das responsáveis pela solução do desafio.
- Dentro deste mesmo formulário será necessário incluir um link do GitHub que contenha todo o desafio solucionado pela squad e o vídeo de  presentação do desafio.
- A squad deve responder o formulário até às 19h do dia 01 demarço. Após o envio, o desafio não poderá ser atualizado.
- Link: https://forms.gle/ofm4qypDkAZfhFBB7