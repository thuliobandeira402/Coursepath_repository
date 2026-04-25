import textwrap
from others.tradutor import *
from others.utils import *
from time import sleep

artigo_01_metodologia = {
    "title" : "The Craft of Scientific Writing",
    "authors": "Michael Alley",
    "introduction": """O texto apresenta uma abordagem prática e estruturada para a escrita científica, enfatizando que
comunicar ideias com clareza é tão importante quanto ter boas ideias. O autor argumenta que muitos textos técnicos
falham não por falta de conteúdo, mas por má organização e excesso de complexidade desnecessária. Dessa forma, ele
propõe princípios fundamentais para tornar a escrita mais acessível e eficiente.

Um dos pontos centrais do material é a importância de colocar a informação mais relevante em posições estratégicas
dentro da frase, especialmente no início e no final. Isso ocorre porque os leitores tendem a lembrar mais dessas
partes. Assim, estruturar frases com foco no leitor é essencial para melhorar a compreensão.

O autor também critica o uso excessivo de linguagem passiva e termos vagos, que tornam o texto distante e difícil de
interpretar. Em vez disso, recomenda o uso de verbos fortes e diretos, além de construções mais simples. Essa
abordagem reduz ambiguidades e torna o texto mais dinâmico.

Outro aspecto importante abordado é a organização em níveis: palavras, frases, parágrafos e documento completo.
Cada nível deve ter coerência interna e contribuir para o objetivo geral do texto. Parágrafos, por exemplo, devem
começar com uma ideia principal clara, seguida de explicações e exemplos.

O material também enfatiza a importância de revisar e reescrever. A primeira versão de um texto raramente é a melhor,
e o processo de revisão é essencial para eliminar redundâncias, melhorar a clareza e ajustar a estrutura.

Além disso, o autor destaca que escrever bem é uma habilidade que pode ser aprendida e desenvolvida com prática. Ele
desmistifica a ideia de que bons escritores nascem prontos, mostrando que técnicas específicas podem melhorar
significativamente a qualidade da comunicação.

Outro ponto relevante é o foco no leitor. O texto deve ser construído pensando em quem vai ler, antecipando dúvidas
e dificuldades. Isso implica explicar conceitos de forma progressiva e evitar assumir conhecimento prévio excessivo.

O autor também discute o uso adequado de exemplos e analogias, que ajudam a tornar conceitos complexos mais
compreensíveis. Esses recursos são especialmente úteis em áreas técnicas, onde a abstração pode dificultar o
entendimento.

Por fim, o material conclui que a escrita científica eficaz depende de clareza, organização e intenção. Ao aplicar
esses princípios, é possível transformar textos técnicos em ferramentas reais de comunicação, facilitando o
aprendizado e a disseminação do conhecimento.""",
    "link": "https://textbookheaven.org/pdf/The%20Craft%20of%20Scientific%20Writing.pdf"
}



artigo_02_metodologia = {
    "title": "The Science of Scientific Writing",
    "authors": "George D. Gopen",
    "introduction": """O artigo propõe uma análise detalhada de como os leitores interpretam textos científicos,
baseando-se em princípios cognitivos e linguísticos. A ideia central é que a clareza na escrita depende não apenas
do que é dito, mas de como a informação é estruturada.

Os autores introduzem o conceito de expectativas do leitor, mostrando que quem lê um texto científico espera
encontrar certas informações em posições específicas. Quando essas expectativas são quebradas, a compreensão se
torna mais difícil, mesmo que o conteúdo esteja correto.

Um dos principais pontos discutidos é a importância do sujeito e do verbo na frase. O leitor naturalmente associa
o sujeito ao "personagem" principal e o verbo à ação. Portanto, alinhar esses elementos com o conteúdo mais
importante melhora significativamente a clareza.

O artigo também destaca a relevância da chamada "energia da frase", que está relacionada à posição das informações
mais importantes. Colocar ideias-chave no final da frase aumenta o impacto e facilita a retenção.

Outro aspecto abordado é a coesão entre frases. O texto deve fluir de forma lógica, com cada frase conectando-se
naturalmente à anterior. Isso pode ser feito por meio da repetição controlada de termos ou da progressão temática.

Os autores também criticam o uso excessivo de nominalizações, que transformam verbos em substantivos e tornam o
texto mais pesado. Esse tipo de construção reduz a clareza e dificulta a leitura.

Além disso, o artigo enfatiza a importância de revisar o texto com foco no leitor, e não no autor. Isso significa
avaliar se a estrutura facilita a compreensão, em vez de apenas verificar a correção gramatical.

Outro ponto importante é a distinção entre informação conhecida e nova. A informação conhecida deve aparecer no
início da frase, enquanto a nova deve vir no final. Essa organização facilita o processamento cognitivo.

O texto também aborda como pequenas mudanças estruturais podem ter grande impacto na clareza, mostrando exemplos
práticos de reescrita de frases.

Por fim, o artigo conclui que escrever bem em ciência é uma questão de entender como as pessoas leem. Ao alinhar
a estrutura do texto com os processos cognitivos do leitor, é possível comunicar ideias complexas de forma muito
mais eficaz.""",
    "link": "https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing"
}



artigo_01_algebra_linear = {
    "title": "Introduction to Linear Algebra",
    "authors": "Gilbert Strang",
    "introduction": """O material apresenta uma introdução abrangente à álgebra linear, com foco em construir uma
compreensão sólida e intuitiva dos conceitos fundamentais que sustentam grande parte da computação moderna. Diferente
de abordagens puramente algorítmicas, o autor enfatiza o entendimento conceitual, mostrando não apenas como resolver
problemas, mas por que os métodos funcionam. Essa abordagem é especialmente importante para estudantes iniciantes,
pois evita a memorização mecânica e promove o raciocínio matemático.

O curso começa com sistemas de equações lineares, que são apresentados como uma forma de modelar diversos problemas
do mundo real. A partir disso, introduz-se o conceito de matrizes como uma ferramenta eficiente para representar e
resolver esses sistemas. Essa conexão entre representação e solução é essencial para compreender como a matemática
é aplicada na computação.

Um dos pilares do material é o conceito de vetor, explorado tanto do ponto de vista geométrico quanto algébrico.
Vetores são apresentados como objetos que representam direção e magnitude, permitindo modelar fenômenos em diferentes
dimensões. Essa dualidade ajuda os alunos a desenvolverem uma intuição visual e analítica simultaneamente.

O autor também explora operações com matrizes, incluindo multiplicação, transposição e inversão, destacando suas
propriedades e aplicações. Essas operações são fundamentais em áreas como computação gráfica, onde transformações
espaciais são realizadas por meio de matrizes, e em aprendizado de máquina, onde dados são frequentemente
representados matricialmente.

Outro conceito central é o de espaço vetorial, que generaliza a ideia de vetores para contextos mais abstratos.
Essa generalização permite compreender estruturas matemáticas mais complexas e preparar o estudante para tópicos
avançados. A noção de independência linear, base e dimensão também é introduzida, sendo essencial para entender a
estrutura dos espaços.

O material também aborda transformações lineares, que são funções que preservam a estrutura dos espaços vetoriais.
Essas transformações são representadas por matrizes, estabelecendo uma conexão direta entre funções e operações
matriciais. Essa ideia é fundamental em diversas aplicações computacionais.

Além disso, são discutidos autovalores e autovetores, conceitos que permitem analisar o comportamento de
transformações lineares. Esses conceitos são amplamente utilizados em áreas como processamento de sinais, análise
de dados e inteligência artificial.

Outro ponto importante é a ênfase na interpretação geométrica dos conceitos. Em vez de tratar a álgebra linear
apenas como manipulação simbólica, o autor mostra como visualizar os resultados, o que facilita a compreensão.

O material também incentiva o uso de exemplos e aplicações práticas, mostrando como a álgebra linear está presente
em problemas reais. Isso ajuda a aumentar o engajamento dos estudantes e a relevância do conteúdo.

Por fim, o curso conclui que a álgebra linear é uma das ferramentas mais importantes da ciência da computação,
sendo essencial para áreas como gráficos computacionais, machine learning e ciência de dados. Ao desenvolver uma
base sólida nesses conceitos, o estudante estará melhor preparado para enfrentar desafios mais avançados.""",
    "link": "https://math.mit.edu/~gs/linearalgebra/ila6/Introduction%20to%20Linear%20Algebra%206th%20edition_02.pdf"
}



artigo_02_algebra_linear = {
    "title": "Interactive Linear Algebra",
    "authors": "Dan Margalit",
    "introduction": """O material propõe uma abordagem inovadora para o ensino de álgebra linear, utilizando
interatividade como ferramenta central para facilitar a compreensão de conceitos abstratos. Em vez de depender
exclusivamente de texto e fórmulas, o conteúdo incorpora elementos visuais e dinâmicos que permitem aos estudantes
explorar os conceitos de forma prática.

O curso começa com os fundamentos, como vetores e operações básicas, apresentando-os de maneira intuitiva. Os
vetores são frequentemente ilustrados graficamente, permitindo que os alunos visualizem operações como soma e
multiplicação por escalar. Essa abordagem ajuda a construir uma base sólida de entendimento.

Um dos principais diferenciais do material é o uso de visualizações interativas. Por meio dessas ferramentas, os
estudantes podem manipular elementos matemáticos e observar os resultados em tempo real. Isso transforma o
aprendizado em uma experiência ativa, em vez de passiva.

O texto também aborda matrizes e sistemas lineares, explicando detalhadamente como representar e resolver
problemas. A interatividade permite que os alunos experimentem diferentes métodos e compreendam melhor os
resultados.

Outro aspecto importante é a ênfase na intuição. O material evita linguagem excessivamente formal nos estágios
iniciais, focando em explicações claras e acessíveis. Isso é especialmente útil para iniciantes que ainda não
estão familiarizados com o rigor matemático.

Além disso, o curso inclui exercícios interativos que permitem aos estudantes testar seu conhecimento
imediatamente. Esse feedback instantâneo é fundamental para o aprendizado, pois ajuda a identificar erros e
reforçar conceitos.

O material também cobre tópicos mais avançados, como transformações lineares, determinantes e autovalores,
mantendo a abordagem visual sempre que possível. Isso facilita a compreensão de conceitos que normalmente são
considerados difíceis.

Outro ponto relevante é a organização didática do conteúdo. Os tópicos são apresentados de forma progressiva,
garantindo que cada novo conceito se baseie no anterior. Isso reduz a sobrecarga cognitiva e melhora a retenção.

O uso de exemplos práticos também é um destaque, conectando teoria e aplicação. Os estudantes conseguem ver como
os conceitos são utilizados em contextos reais, o que aumenta a motivação.

Além disso, o material incentiva a exploração independente, permitindo que os alunos avancem no seu próprio ritmo.
Essa flexibilidade é importante para acomodar diferentes estilos de aprendizado.

Por fim, o curso conclui que a interatividade é uma ferramenta poderosa no ensino da matemática, especialmente em
áreas abstratas como a álgebra linear. Ao tornar o aprendizado mais visual e dinâmico, o material contribui para
uma compreensão mais profunda e duradoura.""",
    "link": "https://textbooks.math.gatech.edu/ila/"
}



artigo_01_fundamentos_computacionais = {
    "title": "Algorithms",
    "authors": "Jeff Erickson",
    "introduction": """O livro de Jeff Erickson apresenta uma abordagem profunda e pedagógica sobre o projeto e a 
análise de algoritmos, posicionando-se como uma das alternativas mais robustas ao clássico texto de Cormen. O autor 
defende que o aprendizado de algoritmos não deve ser uma simples memorização de receitas, mas sim o desenvolvimento 
de uma habilidade de resolução de problemas complexos. Ao longo da obra, ele prioriza a clareza narrativa e a intuição 
matemática, explicando não apenas como um algoritmo funciona, mas o porquê de sua existência e as nuances de sua efici-
ência. Um dos grandes diferenciais do material é a forma como trata a recursão e o backtracking, servindo como base 
sólida para tópicos mais avançados, como a programação dinâmica. Erickson consegue desmistificar temas densos através 
de uma linguagem acessível e exemplos que desafiam a lógica do estudante de forma progressiva. Além disso, o texto 
enfatiza a modelagem de problemas reais em abstrações computacionais, garantindo que o leitor consiga aplicar a teoria 
em contextos práticos de engenharia de software. A estrutura do livro é pensada para o ensino moderno, focando em 
conceitos que permanecem relevantes independentemente das linguagens de programação da moda. Por fim, o autor 
disponibiliza uma vasta coleção de exercícios que estimulam o pensamento crítico e a prova de corretude, elementos 
essenciais para qualquer cientista da computação em formação.
Por fim, o material conclui que o estudo de algoritmos não é apenas sobre aprender técnicas, mas sobre desenvolver
uma forma de pensar que permite resolver problemas de maneira eficiente e elegante.""",
    "link": "https://jeffe.cs.illinois.edu/teaching/algorithms/"
}



artigo_02_fundamentos_computacionais = {
    "title": "CS50 Notes",
    "authors": "David J. Malan",
    "introduction": """O material apresenta uma introdução acessível e abrangente aos fundamentos da ciência da
computação, com foco na resolução de problemas e no desenvolvimento do pensamento computacional. A proposta é
ensinar conceitos complexos de forma simples e intuitiva.

O curso começa com a ideia de algoritmo, explicando como dividir problemas em etapas menores e mais gerenciáveis.
Essa habilidade é essencial para qualquer área da computação.

O material também introduz estruturas de dados básicas, como arrays e listas, mostrando como organizar informações
de forma eficiente.

Outro ponto importante é a introdução à programação, utilizando linguagens como C e Python. O foco não está apenas
na sintaxe, mas na lógica por trás dos programas.

O curso também aborda conceitos como memória, ponteiros e gerenciamento de recursos, ajudando os estudantes a
entender o funcionamento interno dos programas.

Além disso, são apresentados conceitos de abstração, que permitem simplificar problemas complexos.

O material enfatiza o aprendizado prático, com exercícios e projetos que incentivam a aplicação dos conceitos.

Outro aspecto relevante é a abordagem didática, que utiliza exemplos do cotidiano para explicar conceitos
técnicos.

O curso também incentiva a persistência e a resolução de problemas, mostrando que erros fazem parte do processo
de aprendizado.

Além disso, são exploradas áreas como criptografia, web e bancos de dados, oferecendo uma visão ampla da
computação.

O material também destaca a importância da ética na computação.

Por fim, conclui que a base sólida em conceitos fundamentais é essencial para o crescimento na área de
tecnologia.""",
    "link": "https://cs50.harvard.edu/x/"
}



artigo_01_elementos_sistemas = {
    "title": "The Elements of Computing Systems",
    "authors": "Noam Nisan, Shimon Schocken",
    "introduction": """O material apresenta uma abordagem profundamente estruturada para o entendimento de sistemas
computacionais, com a proposta de ensinar como um computador funciona desde seus componentes mais básicos até a
execução de software de alto nível. A ideia central do curso é desmistificar o funcionamento dos computadores,
mostrando que sistemas complexos podem ser compreendidos a partir da composição de elementos simples.

O conteúdo inicia com portas lógicas fundamentais, como AND, OR e NOT, que são apresentadas como os blocos básicos
da computação digital. A partir dessas estruturas simples, os autores demonstram como construir circuitos mais
complexos, como multiplexadores, somadores e registradores. Essa progressão ajuda os estudantes a entenderem como
operações lógicas podem ser combinadas para realizar tarefas computacionais.

Um dos aspectos mais relevantes do material é a construção incremental de um computador completo. Os estudantes
não apenas aprendem a teoria, mas também implementam cada componente, o que proporciona uma compreensão prática e
concreta. Essa abordagem "de baixo para cima" permite que os alunos visualizem claramente como cada camada
contribui para o sistema final.

O curso também aborda a arquitetura de computadores, incluindo a construção de uma CPU funcional. Os conceitos de
unidade lógica e aritmética (ALU), registradores e controle são explorados em detalhes, mostrando como instruções
são executadas internamente.

Outro ponto importante é o estudo da memória, incluindo RAM e armazenamento. O material explica como dados são
armazenados e recuperados, além de discutir limitações e trade-offs de diferentes tipos de memória.

Além do hardware, o curso avança para níveis mais altos de abstração, introduzindo linguagem de máquina e assembly.
Os estudantes aprendem como instruções de baixo nível controlam o hardware diretamente, estabelecendo uma ponte
entre hardware e software.

O material também inclui a construção de um compilador simples e um sistema operacional básico, permitindo que os
alunos compreendam como programas de alto nível são traduzidos e executados.

Outro aspecto relevante é a integração entre teoria e prática. Cada conceito apresentado é acompanhado de um
projeto, o que reforça o aprendizado e promove uma compreensão mais profunda.

O curso enfatiza o pensamento sistêmico, mostrando como diferentes componentes interagem para formar um sistema
funcional. Essa visão é essencial para compreender sistemas complexos na computação.

Além disso, o material incentiva a autonomia do estudante, permitindo que ele construa seu próprio entendimento
por meio da experimentação.

Por fim, o texto conclui que compreender os fundamentos dos sistemas computacionais é essencial para qualquer
profissional da área de tecnologia. Ao dominar esses conceitos, o estudante desenvolve uma visão completa do
funcionamento dos computadores, o que facilita o aprendizado de tópicos mais avançados.""",
    "link": "https://www.nand2tetris.org/"
}



artigo_02_elementos_sistemas = {
    "title": "Computer Organization and Architecture",
    "authors": "OpenStax / Archive",
    "introduction": """Esta alternativa oferece uma exploração detalhada sobre a estrutura interna dos computadores, 
conectando o mundo abstrato do software ao funcionamento físico do hardware. O conteúdo aborda a jornada de uma instrução
desde o momento em que é escrita em uma linguagem de alto nível até ser executada por circuitos eletrônicos. O foco principal 
reside na compreensão da arquitetura do processador, onde são discutidos os ciclos de busca, decodificação e execução, 
além da importância da unidade lógica e aritmética. O texto também explora profundamente a hierarquia de memória, explican-
do como a cache, a RAM e o armazenamento secundário trabalham em conjunto para equilibrar velocidade e custo. Outro ponto
central é a discussão sobre o paralelismo e o pipelining, técnicas fundamentais que permitem que os computadores modernos
processem múltiplas tarefas simultaneamente, aumentando drasticamente a performance. Ao utilizar os materiais de Patterson
disponíveis no Archive.org em conjunto com os textos da OpenStax, o estudante tem acesso a uma visão histórica e técnica 
da evolução das arquiteturas RISC e CISC. O material também dedica espaço para explicar a entrada e saída de dados, 
detalhando como periféricos se comunicam com o núcleo do sistema. Em última análise, a obra prepara o leitor para entender
as limitações físicas da computação e como otimizar o software para extrair o máximo do hardware disponível, sendo essencial
para quem deseja atuar em sistemas de baixo nível ou alto desempenho.""",
    "link": "https://archive.org/details/computer-organization-and-design-fifth-edition-the-hardware-software-interface-by-hennessy_202211"
}



artigo_01_sistemas_informacao = {
    "title": "Management Information Systems",
    "authors": "OpenStax",
    "introduction": """O capítulo dedicado aos Sistemas de Informação Gerenciais (SIG) na plataforma OpenStax apresenta a tecnologia 
como um pilar estratégico indispensável para o sucesso das organizações contemporâneas. O texto argumenta que a informação é um dos 
ativos mais valiosos de uma empresa e que saber gerenciá-la define a vantagem competitiva no mercado global. A abordagem foca em como 
os sistemas capturam, processam e distribuem dados para apoiar a tomada de decisão em todos os níveis hierárquicos, desde o operacional 
até o executivo. O autor detalha os componentes essenciais de um SIG, que incluem não apenas hardware e software, mas principalmente as 
pessoas e os processos que dão sentido à tecnologia. Discute-se amplamente o impacto da computação em nuvem, do Big Data e da inteligência 
artificial, mostrando como essas inovações permitem que as empresas identifiquem tendências de consumo e otimizem cadeias de suprimentos. Além disso, 
o material aborda a questão crítica da segurança cibernética e da ética, alertando sobre os riscos de vazamento de dados e a importância da conformidade 
com regulamentações de privacidade. Ao analisar casos de uso, o texto demonstra que a implementação de um sistema de informação não é apenas um desafio técnico, 
mas uma mudança cultural que exige planejamento e visão de negócios. O resumo conclui que o domínio das ferramentas de TI, quando alinhado aos objetivos corporativos, 
transforma dados brutos em inteligência estratégica, permitindo que gestores enfrentem a incerteza com muito mais segurança e precisão.""",
    "link": "https://open.umn.edu/opentextbooks/textbooks/management-information-systems"
}



artigo_02_sistemas_informacao = {
    "title": "Principles of Information Systems",
    "authors": "Ralph Stair",
    "introduction": """O material apresenta os princípios fundamentais dos sistemas de informação, com foco em como
dados são transformados em conhecimento útil para organizações. O autor busca fornecer uma base sólida para
entender o papel da tecnologia na gestão da informação.

O conteúdo começa explorando os componentes de um sistema de informação, incluindo hardware, software, dados,
pessoas e processos. Essa abordagem mostra que sistemas são estruturas complexas e interdependentes.

Um dos conceitos centrais é a transformação de dados em informação e, posteriormente, em conhecimento. O autor
explica como esse processo agrega valor e apoia decisões estratégicas.

O texto também aborda o papel da tecnologia da informação nas organizações, destacando como ela pode melhorar
eficiência, produtividade e inovação.

Outro ponto importante é a gestão de recursos de informação, que envolve planejamento, controle e uso adequado
dos dados.

O material também discute sistemas empresariais, como ERP e CRM, que integram diferentes áreas de uma
organização.

Além disso, são abordados aspectos de segurança da informação, incluindo proteção contra ameaças e gerenciamento
de riscos.

O texto também enfatiza a importância da qualidade da informação, mostrando que dados incorretos podem levar a
decisões equivocadas.

Outro aspecto relevante é o uso de sistemas para suporte à decisão, permitindo análises mais precisas e rápidas.

O material também aborda tendências tecnológicas, como computação em nuvem e big data, que estão transformando
os sistemas de informação.

Além disso, são discutidos aspectos éticos e sociais, incluindo privacidade e uso responsável da tecnologia.

O conteúdo incentiva uma visão crítica sobre o uso da tecnologia, destacando seus benefícios e desafios.

Por fim, o texto conclui que os sistemas de informação são fundamentais para o sucesso organizacional, e que
compreender seus princípios é essencial para profissionais de qualquer área ligada à tecnologia e gestão.""",
    "link": "https://archive.org/details/principlesofinfo0000stai_k3y9"
}





def artigos_01_metodologia():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_metodologia['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_metodologia['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                    ARTIGO: {artigo_01_metodologia['title']}                                 |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_metodologia['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_metodologia['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def artigos_02_metodologia():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_metodologia['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_metodologia['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                   ARTIGO: {artigo_02_metodologia['title']}                                |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_metodologia['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_metodologia['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def artigos_01_algebra_linear():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_algebra_linear['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_algebra_linear['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                    ARTIGO: {artigo_01_algebra_linear['title']}                                  |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_algebra_linear['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_algebra_linear['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m ")
            sleep(2)
            limpar_tela()
            break


def artigos_02_algebra_linear():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_algebra_linear['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_algebra_linear['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                      ARTIGO: {artigo_02_algebra_linear['title']}                                   |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_algebra_linear['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_algebra_linear['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m ")
            sleep(2)
            limpar_tela()
            break


def artigos_01_fundamentos_computacionais():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_fundamentos_computacionais['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_fundamentos_computacionais['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                              ARTIGO: {artigo_01_fundamentos_computacionais['title']}                                            |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_fundamentos_computacionais['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_fundamentos_computacionais['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m ")
            sleep(2)
            limpar_tela()
            break


def artigos_02_fundamentos_computacionais():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_fundamentos_computacionais['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_fundamentos_computacionais['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                                ARTIGO: {artigo_02_fundamentos_computacionais['title']}                                          |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_fundamentos_computacionais['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_fundamentos_computacionais['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m ")
            sleep(2)
            limpar_tela()
            break


def artigos_01_elementos_sistemas():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_elementos_sistemas['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_elementos_sistemas['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                    ARTIGO: {artigo_01_elementos_sistemas['title']}                               |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_elementos_sistemas['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_elementos_sistemas['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m ")
            sleep(2)
            limpar_tela()
            break


def artigos_02_elementos_sistemas():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_elementos_sistemas['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_elementos_sistemas['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                ARTIGO: {artigo_02_elementos_sistemas['title']}                              |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_elementos_sistemas['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_elementos_sistemas['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def artigos_01_sistemas_informacao():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_sistemas_informacao['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_sistemas_informacao['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                    ARTIGO: {artigo_01_sistemas_informacao['title']}                                  |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_sistemas_informacao['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_sistemas_informacao['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def artigos_02_sistemas_informacao():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_sistemas_informacao['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_sistemas_informacao['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                                   ARTIGO: {artigo_02_sistemas_informacao['title']}                                |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_sistemas_informacao['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_sistemas_informacao['link']}""")
        print("\033[1;36m=\033[0m"*110)
        variable_options_articles(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if in_portuguese == True and escolha == "1":
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "1":
            in_portuguese = True
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break