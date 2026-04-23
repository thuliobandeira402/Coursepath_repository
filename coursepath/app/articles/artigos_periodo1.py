import textwrap
from others.tradutor import *
from others.utils import *
from time import sleep

artigo_01_pisi = {
    "title" : "Computação: O vetor de transformação da sociedade",
    "authors": "Avelino Francisco Zorzo, Andree Luis Alice Raabe, Christian Brackmann",
    "introduction": """A introdução do artigo apresenta a computação como uma das forças mais importantes
na transformação da sociedade contemporânea, destacando seu papel central em praticamente todas as áreas do 
conhecimento e da atividade humana. Os autores argumentam que, nas últimas décadas, o avanço tecnológico não
apenas acelerou processos existentes, mas também criou novas formas de interação social, produção econômica 
e geração de conhecimento. A computação passou de uma área técnica restrita a especialistas para um elemento 
essencial do cotidiano, presente em dispositivos móveis, sistemas de informação, redes sociais e serviços digitais
amplamente utilizados pela população.

O texto enfatiza que essa transformação não é apenas tecnológica, mas profundamente social e econômica. A digitalização
da informação e a conectividade global possibilitaram o surgimento de novos modelos de negócio, alteraram relações de
trabalho e ampliaram o acesso à informação. Nesse cenário, a computação atua como uma infraestrutura invisível que 
sustenta grande parte das atividades modernas. Ao mesmo tempo, essa dependência crescente da tecnologia exige que as 
pessoas desenvolvam novas competências para compreender e utilizar esses sistemas de forma crítica e eficiente.

Os autores também discutem a importância da formação em computação como um elemento fundamental para a cidadania 
no século XXI. Eles argumentam que não basta saber utilizar ferramentas tecnológicas; é necessário compreender os 
princípios que as sustentam, como algoritmos, lógica e organização de dados. Essa compreensão permite que os 
indivíduos não apenas consumam tecnologia, mas também participem ativamente de sua criação e evolução. Nesse 
sentido, o ensino de computação deve ir além da alfabetização digital básica, incorporando conceitos mais profundos 
que desenvolvam o pensamento crítico e a capacidade de resolução de problemas.

Por fim, o artigo destaca o papel do pensamento computacional como uma habilidade essencial para lidar com os desafios 
de uma sociedade cada vez mais complexa e orientada por dados. Ao aprender a estruturar problemas, identificar padrões 
e desenvolver soluções eficientes, os indivíduos se tornam mais preparados para atuar em diferentes contextos. Dessa 
forma, a computação é apresentada não apenas como uma área técnica, mas como um componente fundamental da formação 
educacional e do desenvolvimento social""",
    "link": "https://arxiv.org/abs/2106.11419"
}



artigo_02_pisi ={
    "title": "Computational Thinking",
    "authors": "Jeannette M. Wing",
    "introduction": """O artigo apresenta o conceito de pensamento computacional como uma 
habilidade essencial que deve ser incorporada ao conjunto de competências básicas de qualquer
indivíduo, independentemente de sua área de atuação. A autora argumenta que, assim como leitura,
escrita e aritmética, o pensamento computacional deve ser ensinado desde cedo, pois fornece uma maneira
estruturada e eficiente de resolver problemas complexos. Essa abordagem não se limita ao uso de
computadores, mas envolve um conjunto de técnicas cognitivas que podem ser aplicadas em diversas 
situações do cotidiano e em diferentes áreas do conhecimento.

Ao longo da introdução, o texto explica que o pensamento computacional envolve várias etapas importantes,
como a decomposição de problemas em partes menores e mais gerenciáveis, o reconhecimento de padrões entre
diferentes situações, a abstração de detalhes irrelevantes para focar no essencial e a construção de algoritmos
que descrevem soluções passo a passo. Esses processos permitem que problemas complexos sejam resolvidos de maneira
sistemática e replicável. Além disso, a autora destaca que esse tipo de raciocínio também considera limitações práticas,
como tempo, espaço e recursos disponíveis, o que leva à busca por soluções não apenas corretas, mas também eficientes.

Outro ponto importante discutido no texto é que o pensamento computacional complementa outras formas de raciocínio,
como o matemático e o científico, criando uma abordagem interdisciplinar para a resolução de problemas. Ele pode ser
aplicado em áreas como biologia, economia, engenharia e até nas ciências humanas, mostrando que a computação vai além
da programação. A autora também enfatiza que o desenvolvimento dessa habilidade contribui para a formação de indivíduos
mais preparados para lidar com os desafios de uma sociedade cada vez mais digital e orientada por dados.

Por fim, o artigo reforça que a disseminação do pensamento computacional é fundamental para o avanço da educação e da
inovação tecnológica. Ao ensinar as pessoas a pensar de maneira estruturada e lógica, é possível não apenas melhorar a
capacidade de resolver problemas, mas também incentivar a criatividade e a inovação. Dessa forma, o pensamento
computacional é apresentado como uma ferramenta poderosa para transformar tanto o aprendizado quanto a forma como as 
pessoas interagem com o mundo.'""",
    "link": "https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf"
}



artigo_01_fundamentos_matematicos = {
    "title": "The Simplex Geometry of Graphs",
    "authors": "Karel Devriendt, Piet Van Mieghem",
    "introduction": """O artigo propõe uma abordagem inovadora para o estudo de grafos, conectando essa área tradicional
da matemática discreta com conceitos da geometria, especificamente a geometria de simplex. Os autores partem da ideia
de que grafos, que normalmente são estudados por meio de métodos combinatórios ou algébricos, também podem ser analisados
sob uma perspectiva geométrica, o que abre novas possibilidades de interpretação e compreensão. Um simplex é uma
generalização de formas geométricas como pontos, segmentos de reta, triângulos e tetraedros, permitindo representar
estruturas em dimensões superiores.

A proposta central do artigo é representar grafos como estruturas geométricas dentro de espaços de dimensão mais alta,
onde cada vértice e cada conexão podem ser interpretados como componentes de um simplex. Essa representação permite
visualizar propriedades dos grafos de maneira mais intuitiva, facilitando a análise de características como conectividade,
caminhos e relações entre nós. Ao transformar um problema discreto em um problema geométrico, os autores mostram que é
possível utilizar ferramentas da geometria para resolver questões que seriam mais complexas em abordagens tradicionais.

Outro ponto importante discutido no artigo é a relação entre essa abordagem geométrica e conceitos já conhecidos na
teoria dos grafos, como matrizes de adjacência e espectros de grafos. Os autores demonstram que a geometria de simplex
não substitui essas abordagens, mas as complementa, oferecendo uma nova camada de interpretação. Essa integração entre
diferentes áreas da matemática é um dos principais pontos fortes do trabalho, pois permite que pesquisadores utilizem
múltiplas perspectivas para analisar o mesmo problema.

Além disso, o artigo explora como essa abordagem pode ser aplicada em áreas práticas, como análise de redes complexas,
sistemas de comunicação e modelagem de interações sociais. Em redes reais, onde as conexões entre elementos podem ser
altamente complexas, a representação geométrica pode ajudar a identificar padrões e estruturas que não são facilmente
visíveis em representações tradicionais. Isso torna a abordagem especialmente relevante para áreas como ciência de dados
e engenharia de redes.

Os autores também discutem as implicações teóricas dessa nova forma de representação, destacando que ela pode levar ao
desenvolvimento de novos algoritmos e métodos de análise. Ao reinterpretar grafos como objetos geométricos, abre-se
espaço para a aplicação de técnicas avançadas de geometria e topologia, ampliando o conjunto de ferramentas disponíveis
para pesquisadores.

Por fim, o artigo conclui que a geometria de simplex oferece uma perspectiva poderosa e complementar para o estudo de
grafos, permitindo uma compreensão mais profunda de suas propriedades. Essa abordagem não apenas enriquece a teoria dos
grafos, mas também contribui para o desenvolvimento de novas aplicações práticas, especialmente em áreas que lidam com
estruturas complexas e interconectadas.""",
    "link": "https://arxiv.org/abs/1807.06475"
}



artigo_02_fundamentos_matematicos = {
    "title": "Discrete Math with Programming: A Principled Approach",
    "authors": "Yanhong A. Liu, Matthew Castellana",
    "introduction": """O artigo apresenta uma abordagem integrada para o ensino e aprendizado de matemática discreta,
combinando conceitos matemáticos com programação de forma estruturada e orientada a princípios. Os autores argumentam
que a matemática discreta é fundamental para a ciência da computação, mas frequentemente é ensinada de maneira abstrata
e desconectada da prática, o que dificulta a compreensão dos estudantes. Para resolver esse problema, eles propõem um
método que utiliza programação como ferramenta para explorar e entender conceitos matemáticos.

A ideia central do texto é que programar pode ajudar a tornar conceitos abstratos mais concretos. Ao implementar
algoritmos e estruturas matemáticas em código, os estudantes conseguem visualizar e testar ideias, o que facilita o
aprendizado. Por exemplo, conceitos como conjuntos, relações, grafos e lógica podem ser representados e manipulados
diretamente em programas, permitindo uma compreensão mais prática e interativa.

Os autores também destacam a importância de uma abordagem baseada em princípios, em vez de simplesmente apresentar
técnicas isoladas. Isso significa ensinar os fundamentos por trás dos conceitos, como invariantes, propriedades e
relações, permitindo que os estudantes desenvolvam uma compreensão mais profunda e generalizável. Essa abordagem ajuda
a evitar a memorização mecânica e incentiva o raciocínio lógico e estruturado.

Outro aspecto importante do artigo é a integração entre teoria e prática. Em vez de tratar a matemática e a programação
como disciplinas separadas, os autores mostram como elas podem ser ensinadas de forma conjunta, reforçando uma à outra.
Essa integração é especialmente relevante para estudantes de ciência da computação, que precisam aplicar conceitos
matemáticos na resolução de problemas computacionais.

Além disso, o texto discute como essa abordagem pode melhorar a motivação dos estudantes. Ao verem aplicações práticas
dos conceitos matemáticos, os alunos tendem a se engajar mais no aprendizado. A programação permite experimentar, testar
hipóteses e observar resultados, tornando o processo mais dinâmico e interessante.

Os autores também abordam a importância de desenvolver habilidades de abstração e generalização, que são essenciais
tanto na matemática quanto na computação. Ao trabalhar com conceitos de forma estruturada, os estudantes aprendem a
identificar padrões e aplicar soluções em diferentes contextos, o que é fundamental para a resolução de problemas
complexos.

Por fim, o artigo conclui que a combinação de matemática discreta e programação oferece uma abordagem mais eficaz para
o ensino de fundamentos da computação. Ao integrar teoria e prática, essa metodologia contribui para o desenvolvimento
de habilidades essenciais, preparando melhor os estudantes para desafios acadêmicos e profissionais na área de
tecnologia.""",
    "link": "https://arxiv.org/abs/2107.01248"
}



artigo_01_principios_programacao = {
    "title": "Learning and Teaching Programming",
    "authors": "Robins, Rountree",
    "introduction": """O artigo apresenta uma análise detalhada das dificuldades enfrentadas por estudantes iniciantes
no aprendizado de programação, destacando que esse processo envolve uma mudança significativa na forma de pensar.
Diferente de outras áreas do conhecimento, a programação exige que o aluno desenvolva modelos mentais abstratos para
compreender o funcionamento do código. Muitos estudantes encontram dificuldades logo nos primeiros conceitos, como
variáveis, estruturas de controle e fluxo de execução, o que pode gerar frustração e desmotivação.

Os autores argumentam que uma das principais causas dessas dificuldades é a tendência dos alunos de tentar memorizar
soluções em vez de compreender os conceitos fundamentais. Isso leva a um aprendizado superficial, que não permite a
adaptação a novos problemas. Além disso, a natureza invisível da execução de programas dificulta a compreensão do que
realmente está acontecendo, tornando essencial o desenvolvimento de habilidades de raciocínio abstrato e lógico.

O texto também discute diferentes abordagens pedagógicas para melhorar o ensino de programação. Entre elas, destaca-se
a importância de fornecer feedback imediato, utilizar exemplos práticos e incentivar a experimentação. Os autores
defendem que os estudantes devem ser encorajados a explorar soluções, cometer erros e aprender com eles,
desenvolvendo uma compreensão mais profunda dos conceitos.

Por fim, o artigo conclui que o ensino de programação deve ser estruturado de forma a apoiar o desenvolvimento gradual
do conhecimento, levando em consideração as dificuldades específicas dos iniciantes. A combinação de métodos de ensino
adequados e prática constante é fundamental para o sucesso no aprendizado.""",
    "link": "https://www.researchgate.net/publication/200085837_Learning_and_Teaching_Programming_A_Review_and_Discussion"
}



artigo_02_principios_programacao = {
    "title": "Computing at school in the UK",
    "authors": "Simon Peyton Jones",
    "introduction": """A introdução do texto aborda a necessidade de repensar a forma como a programação é ensinada,
destacando que muitos cursos focam excessivamente na sintaxe das linguagens, em detrimento da compreensão conceitual.
O autor argumenta que essa abordagem limita o aprendizado, pois os estudantes acabam aprendendo a escrever código sem
entender profundamente os princípios que orientam a resolução de problemas.

O texto enfatiza que programar é essencialmente uma atividade de raciocínio lógico e estruturado. Isso envolve
decompor problemas, identificar padrões, abstrair detalhes irrelevantes e construir soluções claras e organizadas.
Nesse contexto, conceitos como funções, tipos de dados e estruturas de controle devem ser ensinados como ferramentas
para organizar o pensamento, e não apenas como elementos técnicos.

Outro ponto importante é a valorização da clareza e da legibilidade do código. O autor destaca que um bom programa
deve ser compreensível por outras pessoas, facilitando sua manutenção e evolução. Ele também sugere a inclusão de
práticas como testes e depuração no processo de ensino, promovendo uma abordagem mais completa e profissional.

Por fim, o texto propõe uma abordagem pedagógica que prioriza a compreensão profunda e a construção gradual do
conhecimento. Essa estratégia permite que os estudantes desenvolvam uma base sólida, tornando-se capazes de aprender
novas linguagens e tecnologias com maior facilidade ao longo do tempo.""",
    "link": "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/ComputingAtSchoolCACM.pdf"
}



artigo_01_sustentabilidade = {
    "title": "Information Ethics: Its Nature and Scope",
    "authors": "Luciano Floridi",
    "introduction": """O artigo introduz o campo da ética da informação como uma área dedicada a estudar as implicações
morais do uso e da disseminação de dados na sociedade contemporânea. O autor argumenta que, com o avanço das tecnologias
digitais, a informação se tornou um recurso central, influenciando decisões, comportamentos e estruturas sociais. Nesse
contexto, surgem novas questões éticas relacionadas à privacidade, à segurança e ao acesso à informação.

O texto propõe uma abordagem abrangente da ética da informação, considerando não apenas os seres humanos, mas também
os sistemas e ambientes informacionais como objetos de análise moral. Essa perspectiva amplia o escopo tradicional da
ética, incorporando aspectos tecnológicos e digitais que antes não eram considerados.

Além disso, o autor discute a importância de desenvolver princípios éticos que orientem o uso responsável da informação.
Isso inclui a proteção de dados pessoais, a transparência no uso de algoritmos e a promoção de acesso equitativo à
informação. Essas questões são cada vez mais relevantes em um mundo onde decisões automatizadas têm impacto
significativo na vida das pessoas.

Por fim, o artigo destaca que a ética da informação é essencial para garantir que o avanço tecnológico ocorra de forma
responsável e sustentável. Ao refletir sobre as consequências do uso da tecnologia, é possível promover uma sociedade
mais justa e equilibrada.""",
    "link": "https://philarchive.org/archive/FLOIEI"
}



artigo_02_sustentabilidade = {
    "title": "An Introduction to Complex Systems Science",
    "authors": "Yaneer Bar-Yam",
    "introduction": """O artigo introduz os fundamentos da ciência dos sistemas complexos, apresentando uma abordagem
interdisciplinar para compreender fenômenos que emergem da interação entre múltiplos componentes. O autor argumenta
que muitos dos desafios enfrentados pela ciência e pela sociedade moderna não podem ser compreendidos por meio de
análises reducionistas, que examinam partes isoladas de um sistema. Em vez disso, é necessário considerar as relações
e interações entre os componentes, pois são essas conexões que dão origem a comportamentos complexos e muitas vezes
imprevisíveis.

O texto apresenta conceitos fundamentais da teoria dos sistemas complexos, como emergência, auto-organização e não
linearidade. A emergência refere-se ao surgimento de propriedades e comportamentos no nível do sistema que não podem
ser previstos a partir do comportamento individual de seus componentes. A auto-organização descreve a capacidade de
sistemas complexos de desenvolver estruturas e padrões sem a necessidade de controle centralizado. A não linearidade,
por sua vez, indica que pequenas mudanças em um componente podem ter efeitos desproporcionais e inesperados em todo
o sistema.

O autor também discute a aplicação da ciência dos sistemas complexos em diversas áreas, como biologia, economia,
ciências sociais e tecnologia. Em cada um desses domínios, a abordagem dos sistemas complexos oferece novas formas
de compreender fenômenos que antes eram difíceis de explicar. Por exemplo, o comportamento de mercados financeiros,
a dinâmica de ecossistemas e a propagação de doenças podem ser melhor compreendidos quando analisados como sistemas
complexos.

Por fim, o artigo destaca que a ciência dos sistemas complexos representa uma mudança de paradigma na forma como
abordamos problemas científicos e sociais. Ao adotar uma perspectiva sistêmica e interdisciplinar, é possível
desenvolver modelos mais precisos e intervenções mais eficazes para lidar com os desafios da sociedade contemporânea.""",
    "link": "https://arxiv.org/pdf/1912.05088"
}



artigo_01_adm = {
    "title": "Introdução à Teoria Geral da Administração",
    "authors": "Idalberto Chiavenato",
    "introduction": """O livro apresenta de forma abrangente as principais teorias e abordagens que compõem a Teoria
Geral da Administração, desde seus primórdios até as tendências contemporâneas. O autor argumenta que a administração
é uma ciência social aplicada que busca compreender e aprimorar o funcionamento das organizações, sejam elas empresas,
instituições públicas ou entidades sem fins lucrativos. Nesse sentido, o texto oferece uma visão panorâmica das
diferentes escolas de pensamento administrativo, mostrando como cada uma contribuiu para o desenvolvimento da área.

O texto destaca que a administração surgiu como disciplina formal no início do século XX, em resposta às demandas
geradas pela Revolução Industrial. Com o crescimento das organizações e a complexidade crescente dos processos
produtivos, tornou-se necessário desenvolver métodos sistematizados de gestão. As primeiras teorias, como a
Administração Científica de Taylor e a Teoria Clássica de Fayol, buscavam aumentar a eficiência e a produtividade
por meio da racionalização do trabalho e da estruturação hierárquica das organizações.

O autor também aborda a evolução do pensamento administrativo ao longo do século XX, destacando como novas teorias
foram desenvolvidas em resposta às limitações das abordagens anteriores e às mudanças no contexto social e econômico.
A Escola das Relações Humanas, por exemplo, trouxe uma perspectiva mais humanista para a administração, enfatizando
a importância das pessoas e das relações interpessoais no ambiente organizacional. Posteriormente, abordagens
sistêmicas e contingenciais ampliaram ainda mais a compreensão das organizações como sistemas abertos e dinâmicos.

Por fim, o livro reforça que o estudo da Teoria Geral da Administração é fundamental para a formação de gestores
capazes de compreender e lidar com a complexidade das organizações modernas. Ao conhecer as diferentes teorias e
suas aplicações, os administradores desenvolvem uma base sólida para tomar decisões mais fundamentadas e eficazes
em diferentes contextos organizacionais.""",
    "link": "https://livrariapublica.com.br/livros/introducao-a-teoria-geral-da-administracao-idalberto-chiavenato/"
}



artigo_02_adm = {
    "title": "Teoria Geral da Administração",
    "authors": "Luís Moretto Neto",
    "introduction": """O livro apresenta uma introdução estruturada às principais correntes teóricas da administração,
com o objetivo de fornecer ao leitor uma base conceitual sólida para compreender o funcionamento e a gestão das
organizações. O autor parte da premissa de que a administração é uma área de conhecimento em constante evolução,
influenciada por mudanças no contexto econômico, social e tecnológico. Nesse sentido, o texto busca articular as
diferentes teorias administrativas de forma coerente e progressiva.

O texto destaca que as organizações são sistemas sociais complexos, compostos por pessoas, recursos e processos que
precisam ser coordenados de forma eficiente para atingir seus objetivos. O autor argumenta que compreender as
teorias da administração é essencial para desenvolver a capacidade de análise e intervenção nas organizações,
permitindo que os gestores identifiquem problemas, proponham soluções e implementem melhorias de forma fundamentada.

O autor também enfatiza a importância de uma visão crítica e reflexiva sobre as teorias administrativas. Em vez de
apresentá-las como verdades absolutas, o texto incentiva o leitor a analisar cada abordagem em seu contexto histórico
e a avaliar sua aplicabilidade nas diferentes situações organizacionais. Essa postura crítica é fundamental para o
desenvolvimento de um pensamento administrativo maduro e adaptável.

Por fim, o livro destaca que a administração moderna exige dos gestores não apenas conhecimentos técnicos, mas também
habilidades interpessoais, capacidade de liderança e visão estratégica. Ao integrar diferentes perspectivas teóricas,
o texto contribui para a formação de profissionais mais completos e preparados para os desafios do mercado de trabalho
contemporâneo.""",
    "link": "https://www.researchgate.net/publication/324025900_Teoria_Geral_da_Administracao"
}




def artigos_01_projeto_interdisciplinar01_detalhes():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_pisi['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_pisi['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_01_pisi['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_pisi['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_pisi['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break




def artigos_02_projeto_interdisciplinar01_detalhes():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_pisi['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_pisi['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_02_pisi['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_pisi['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_pisi['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_01_fundamentos_matematicos():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_fundamentos_matematicos['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_fundamentos_matematicos['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_01_fundamentos_matematicos['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_fundamentos_matematicos['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_fundamentos_matematicos['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_02_fundamentos_matematicos():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_fundamentos_matematicos['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_fundamentos_matematicos['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_02_fundamentos_matematicos['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_fundamentos_matematicos['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_fundamentos_matematicos['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_01_principios():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_principios_programacao['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_principios_programacao['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_01_principios_programacao['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_principios_programacao['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_principios_programacao['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_02_principios():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_principios_programacao['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_principios_programacao['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_02_principios_programacao['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_principios_programacao['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_principios_programacao['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_01_sustentabilidade():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_sustentabilidade['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_sustentabilidade['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_01_sustentabilidade['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_sustentabilidade['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_sustentabilidade['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_02_sustentabilidade():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_sustentabilidade['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_sustentabilidade['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_02_sustentabilidade['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_sustentabilidade['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_sustentabilidade['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_01_administracao():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_01_adm['introduction'], width=100)
        else:
            translated = translating_text(artigo_01_adm['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_01_adm['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_01_adm['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_01_adm['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break


def artigos_02_administracao():
    in_portuguese = False
    while True:
        if in_portuguese:
            introduction = textwrap.fill(artigo_02_adm['introduction'], width=100)
        else:
            translated = translating_text(artigo_02_adm['introduction'])
            introduction = textwrap.fill(translated, width=100)
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;36m|                           ARTIGO: {artigo_02_adm['title']}                        |\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        print(f"""\033[1;33mAutores:\033[0m {artigo_02_adm['authors']}
\033[1;33mIntrodução:\033[0m {introduction}
\033[1;33mLink:\033[0m {artigo_02_adm['link']}""")
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
            print("Voltando para o menu de cadeiras...🔄​")
            sleep(2)
            limpar_tela()
            break