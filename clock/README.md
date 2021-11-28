# Clockpython - Criando um super relógio em python

## A intenção desse projeto é melhorar o aprendizado e utilizar na prática da linguagem de programação python de uma forma criativa e divertida, enquanto estuda a linguagem mais a fundo se desafiando e aprendendo

### Código Linha a Linha

Projeto feito em python utilizando um tkinter interface (entre outros que vou colocar aqui)

A ideia que se baseia em criar inicialmente uma aplicação de relógio depois um alarme na linguagem python que vai tocar e falar a hora de tempos em tempos de acordo com o que é programado pelo usuário. Fazer tudo passo a passo futuramente minha ideia é incrementar um mapa ou relógio para dizer a localização e a previsão do tempo também.

## Início do Projeto

### Criação do Relógio - Código Linha a Linha

1.importa o pacote tkinter que é uma interface visual em python.

`import tkinter as tk`

2.importa o módulo datatime, ele fornece módulo como classes para manipulação de dados e horas.

`import datetime`

3.importando o módulo locale que acessa o banco de dados e funcionalidade locais POSIX(é uma família de normas definidas pelo IEEE(Instituto de Engenheiros Elétricos e Eletrônicos) para manutenção de compatibilidade entre sistemas operacionais em PT-PT).

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

15.Delara a função hora.

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

22.Bloqueia qualquer código até que a janela seja fechada

`janela_raiz.mainloop()`

>Referências:

- Interface Python para Tcl/Tk — documentação Python 3.9.9 - docs.python.org - tkinter
- Python - Rótulo Tkinter - tutorialspoint.com - (tutorialspoint.com)
- datetime — Tipos básicos de data e hora. - <https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior>
