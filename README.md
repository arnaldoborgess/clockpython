# Clockpython - Criando um super relógio em python

## A intenção desse projeto é melhorar o aprendizado e utilizar na prática da linguagem de programação python de uma forma criativa e divertida, enquanto estuda a linguagem mais a fundo se desafiando e aprendendo

### Código Linha a Linha

Projeto feito em python utilizando um tkinter interface (entre outros que vou colocar aqui)

A ideia que se baseia em criar inicialmente uma aplicação de relógio depois um alarme na linguagem python que vai tocar e falar a hora de tempos em tempos de acordo com o que é programado pelo usuário. Fazer tudo passo a passo futuramente minha ideia é incrementar um mapa ou relógio para dizer a localização e a previsão do tempo também.

## Início do Projeto

### Criação do Relógio - Código Linha a Linha Relógio

1.Importa o pacote tkinter que é uma interface visual em python.

`import tkinter as tk`

2.Importa o módulo datatime, ele fornece módulo como classes para manipulação de dados e horas.

`import datetime`

3.Importando o módulo locale que acessa o banco de dados e funcionalidade locais POSIX(é uma família de normas definidas pelo IEEE(Instituto de Engenheiros Elétricos e Eletrônicos) para manutenção de compatibilidade entre sistemas operacionais em PT-PT).

`import locale`

5.Define a localidade de todas as categorias para configuração do usuário padrão.

`locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')`

7.Classe Principal do código.

`class TelaPrincipal`

8.Declara a função `def` construtora para criar o objeto da classe `self` nome do primeiro parâmetro do método, `master` é o local onde o objeto será posicionado.

`def __init__(self, master)`

9.Aqui digo que essa é minha tela principal (Janela dos Pais).

`def __init__(self, master):`

10.Implementa uma caixa de exibição onde pode-se colocar texto ou imagens.

`self.relogio_digital = tk.Label`

11.Implementando na tela uma fonte (Arial, 26) onde o `fg` (especifica a cor da fonte) e `bg` (a cor do fundo exibido atrás como etiqueta)

`self.tela, font=('Arial', 26), fg='green', bg = 'Black')`

12.Implementa o relógio digital: `pady` espaço extra adicionado acima e abaixo do texto dentro do widget, `padax` espaço extra adicionado à esquerda e à direita do texto dentro do widget.

`self.relogio_digital.pack(pady=30, padx=30)`

13.Implementa o parâmetro do método hora.

`self.hora()`

15.Declara a função hora.

`self.hora()`

16.Combina uma data com a hora, onde `now()` retorna uma data e hora local.

`agora = datetime.datetime.now()`

17.Criar uma string representando o tempo sob o controle de uma string de formatação explícita.

`self.relogio_digital['text'] = agora.strftime('%A, %d %B %Y\n%H:%M:%S')`

18.Retorna o tempo com o valor da hora.

`self.tela.after(1000, self.hora)`

20.Inicializará o widget tcl.tk.

`janela_raiz = tk.Tk()`

21.Inicializará a janela principal.

`TelaPrincipal(janela_raiz)`

22.Executa a janela em loop.

`janela_raiz.mainloop()`

## Criação do Alarme - Código linha a linha

1.Permite que o código leia a hora e o minuto do computador.

`from time import localtime`

2.Permite que o código leia arquivos de mídia

`from pygame import mixer`

4.Pede ao usuário entrar com o valor da hora.

`hora = int(input('Coloque a Hora: '))`

5.Pede para o usuário entrar com o valor do minuto.

`minuto = int(input('Coloque o Minuto: '))`

7.Inicia o loop.

`while True:`

8.Aqui diz se local for igual a hora e local for igual a minuto.

`if localtime().tm_hour == hora and localtime().tm_min == minuto:`

9.Imprima na tela 'HORA DE ACORDAR'.

`print('HORA DE ACORDAR')`

10.Inicia o módulo de carregamento de mídia.

`mixer.init()`

11.Carrega a mídia com endereço especificado.

`mixer.music.load("endereço do arquivo")`

12.Inicia a mídia.

`mixer.music.play()`

13.Finaliza a interação e o script continua a sua execução.

`break`

>Referências:

* Interface Python para Tcl/Tk — documentação Python 3.9.9 - docs.python.org - tkinter
* Python - Rótulo Tkinter - tutorialspoint.com - (tutorialspoint.com)
* datetime — Tipos básicos de data e hora. - <https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior>
