"""
Dados dos artigos extraídos do projeto original (artigos_periodo1.py e artigos_periodo2.py).
Organizados como lista de dicionários para popular o banco via ArticleRepository.seed().
"""

ARTICLES = [
    # ======================== SEMESTRE 1 ========================
    {
        "semester": 1,
        "subject": "Projeto Interdisciplinar",
        "title": "Computação: O vetor de transformação da sociedade",
        "authors": "Avelino Francisco Zorzo, Andree Luis Alice Raabe, Christian Brackmann",
        "link": "https://arxiv.org/abs/2106.11419",
        "introduction": (
            "A introdução do artigo apresenta a computação como uma das forças mais importantes "
            "na transformação da sociedade contemporânea, destacando seu papel central em praticamente todas as áreas do "
            "conhecimento e da atividade humana. Os autores argumentam que, nas últimas décadas, o avanço tecnológico não "
            "apenas acelerou processos existentes, mas também criou novas formas de interação social, produção econômica "
            "e geração de conhecimento. A computação passou de uma área técnica restrita a especialistas para um elemento "
            "essencial do cotidiano, presente em dispositivos móveis, sistemas de informação, redes sociais e serviços digitais."
        ),
    },
    {
        "semester": 1,
        "subject": "Projeto Interdisciplinar",
        "title": "Computational Thinking",
        "authors": "Jeannette M. Wing",
        "link": "https://www.cs.cmu.edu/~15110-s13/Wing06-ct.pdf",
        "introduction": (
            "O artigo apresenta o conceito de pensamento computacional como uma habilidade essencial que deve ser incorporada "
            "ao conjunto de competências básicas de qualquer indivíduo, independentemente de sua área de atuação. "
            "A autora argumenta que, assim como leitura, escrita e aritmética, o pensamento computacional deve ser ensinado "
            "desde cedo, pois fornece uma maneira estruturada e eficiente de resolver problemas complexos."
        ),
    },
    {
        "semester": 1,
        "subject": "Fundamentos Matemáticos",
        "title": "The Simplex Geometry of Graphs",
        "authors": "Karel Devriendt, Piet Van Mieghem",
        "link": "https://arxiv.org/abs/1807.06475",
        "introduction": (
            "O artigo introduz uma nova abordagem geométrica para o estudo de grafos, propondo uma representação baseada "
            "na geometria dos símplices. Os autores demonstram que propriedades fundamentais dos grafos, como distância, "
            "conectividade e estrutura topológica, podem ser visualizadas e analisadas de maneira mais intuitiva e eficiente "
            "por meio dessa abordagem geométrica. A representação simplicial permite mapear grafos em espaços métricos de "
            "alta dimensão, possibilitando a aplicação de ferramentas da geometria diferencial e da álgebra linear."
        ),
    },
    {
        "semester": 1,
        "subject": "Fundamentos Matemáticos",
        "title": "Discrete Math with Programming: A Principled Approach",
        "authors": "Yanhong A. Liu, Matthew Castellana",
        "link": "https://arxiv.org/abs/2107.01248",
        "introduction": (
            "O artigo propõe uma abordagem integrada para o ensino de matemática discreta com programação, argumentando "
            "que a combinação dessas duas disciplinas não apenas facilita o aprendizado, mas também desenvolve habilidades "
            "mais profundas de resolução de problemas. Os autores defendem que conceitos matemáticos como lógica, conjuntos, "
            "relações e grafos se tornam mais concretos e compreensíveis quando implementados em linguagens de programação."
        ),
    },
    {
        "semester": 1,
        "subject": "Princípios de Programação",
        "title": "Learning and Teaching Programming",
        "authors": "Robins, Rountree",
        "link": "https://www.researchgate.net/publication/200085837_Learning_and_Teaching_Programming_A_Review_and_Discussion",
        "introduction": (
            "O artigo realiza uma revisão abrangente da literatura sobre aprendizado e ensino de programação, com o objetivo "
            "de identificar os principais desafios enfrentados por estudantes e professores nessa área. Os autores analisam "
            "pesquisas que investigam como os iniciantes constroem seu entendimento de conceitos fundamentais de programação, "
            "como variáveis, loops, condicionais e funções, além de explorar as dificuldades cognitivas envolvidas."
        ),
    },
    {
        "semester": 1,
        "subject": "Princípios de Programação",
        "title": "Computing at school in the UK",
        "authors": "Simon Peyton Jones",
        "link": "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/ComputingAtSchoolCACM.pdf",
        "introduction": (
            "O artigo discute a implementação do ensino de computação nas escolas do Reino Unido como disciplina obrigatória, "
            "descrevendo o processo de transformação curricular que levou à inclusão da ciência da computação na educação básica. "
            "O autor apresenta a motivação por trás dessa mudança, destacando a crescente demanda por profissionais com "
            "habilidades computacionais e a necessidade de preparar os cidadãos do futuro para uma sociedade cada vez mais digital."
        ),
    },
    {
        "semester": 1,
        "subject": "Sustentabilidade e Sistemas de Informação",
        "title": "Information Ethics: Its Nature and Scope",
        "authors": "Luciano Floridi",
        "link": "https://philarchive.org/archive/FLOIEI",
        "introduction": (
            "O artigo de Luciano Floridi apresenta uma análise aprofundada da ética da informação como um novo campo filosófico "
            "emergente, dedicado a examinar questões morais relacionadas à criação, gestão, uso e controle da informação. "
            "O autor argumenta que o crescimento exponencial da quantidade de informação disponível no mundo, impulsionado "
            "pelas tecnologias digitais, trouxe consigo uma série de dilemas éticos que as abordagens filosóficas tradicionais "
            "não conseguem responder de forma satisfatória."
        ),
    },
    {
        "semester": 1,
        "subject": "Sustentabilidade e Sistemas de Informação",
        "title": "An Introduction to Complex Systems Science",
        "authors": "Yaneer Bar-Yam",
        "link": "https://arxiv.org/pdf/1912.05088",
        "introduction": (
            "O texto de Yaneer Bar-Yam apresenta uma introdução abrangente à Ciência dos Sistemas Complexos, explorando "
            "como sistemas compostos por múltiplos componentes interativos exibem comportamentos emergentes que não podem "
            "ser previstos simplesmente pela análise de suas partes individuais. O autor explica que um sistema complexo "
            "é aquele em que as interações entre os componentes geram propriedades e padrões que surgem de forma espontânea "
            "e frequentemente imprevisível."
        ),
    },
    {
        "semester": 1,
        "subject": "Introdução a Sistemas de Administração",
        "title": "Introdução à Teoria Geral da Administração",
        "authors": "Idalberto Chiavenato",
        "link": "https://livrariapublica.com.br/livros/introducao-a-teoria-geral-da-administracao-idalberto-chiavenato/",
        "introduction": (
            "O livro de Idalberto Chiavenato apresenta uma visão abrangente e didática das principais teorias e abordagens "
            "que compõem o campo da Administração, desde seus primórdios até as tendências contemporâneas. O autor estrutura "
            "o conteúdo de forma cronológica e temática, permitindo ao leitor compreender a evolução do pensamento administrativo "
            "e como cada teoria surgiu como resposta às necessidades e desafios de sua época."
        ),
    },
    {
        "semester": 1,
        "subject": "Introdução a Sistemas de Administração",
        "title": "Teoria Geral da Administração",
        "authors": "Luís Moretto Neto",
        "link": "https://www.researchgate.net/publication/324025900_Teoria_Geral_da_Administracao",
        "introduction": (
            "A obra de Luís Moretto Neto oferece uma abordagem clara e estruturada da Teoria Geral da Administração (TGA), "
            "apresentando ao leitor os principais fundamentos teóricos que sustentam o campo da administração de organizações. "
            "O autor inicia o texto contextualizando a importância da administração como ciência e prática, destacando seu papel "
            "fundamental no desenvolvimento das organizações modernas e na sociedade como um todo."
        ),
    },

    # ======================== SEMESTRE 2 ========================
    {
        "semester": 2,
        "subject": "Comunicação e Expressão",
        "title": "The Craft of Scientific Writing",
        "authors": "Michael Alley",
        "link": "https://textbookheaven.org/pdf/The%20Craft%20of%20Scientific%20Writing.pdf",
        "introduction": (
            "O livro 'The Craft of Scientific Writing' de Michael Alley é uma obra de referência para pesquisadores, engenheiros "
            "e estudantes que desejam aprimorar suas habilidades de comunicação científica e técnica. O autor apresenta uma "
            "abordagem prática e detalhada sobre como escrever de forma clara, precisa e persuasiva em contextos científicos "
            "e de engenharia, com foco na produção de textos que sejam ao mesmo tempo informativos e acessíveis."
        ),
    },
    {
        "semester": 2,
        "subject": "Comunicação e Expressão",
        "title": "The Science of Scientific Writing",
        "authors": "George D. Gopen",
        "link": "https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing",
        "introduction": (
            "O artigo 'The Science of Scientific Writing' de George D. Gopen e Judith A. Swan propõe uma abordagem linguística "
            "para o problema da clareza na escrita científica. Os autores argumentam que muitos textos científicos são difíceis "
            "de ler não por causa da complexidade das ideias que transmitem, mas por causa da forma como essas ideias são apresentadas "
            "linguisticamente. A falta de clareza, segundo eles, raramente é culpa do leitor, mas sim do escritor."
        ),
    },
    {
        "semester": 2,
        "subject": "Álgebra Linear",
        "title": "Introduction to Linear Algebra",
        "authors": "Gilbert Strang",
        "link": "https://math.mit.edu/~gs/linearalgebra/ila6/Introduction%20to%20Linear%20Algebra%206th%20edition_02.pdf",
        "introduction": (
            "O livro 'Introduction to Linear Algebra' de Gilbert Strang é amplamente reconhecido como um dos textos mais "
            "didáticos e acessíveis sobre álgebra linear disponíveis atualmente. O autor apresenta os conceitos fundamentais "
            "da disciplina, como vetores, matrizes, sistemas lineares, espaços vetoriais, transformações lineares, autovalores "
            "e autovetores, com uma abordagem que combina rigor matemático com intuição geométrica e aplicações práticas."
        ),
    },
    {
        "semester": 2,
        "subject": "Álgebra Linear",
        "title": "Interactive Linear Algebra",
        "authors": "Dan Margalit",
        "link": "https://textbooks.math.gatech.edu/ila/",
        "introduction": (
            "O livro 'Interactive Linear Algebra' de Dan Margalit e Joseph Rabinoff é uma obra inovadora que busca tornar o "
            "aprendizado de álgebra linear mais intuitivo e acessível por meio de uma abordagem altamente visual e interativa. "
            "Os autores utilizam recursos de visualização gráfica para apresentar conceitos fundamentais como vetores, "
            "transformações lineares, bases, dimensão, autovalores e autovetores de uma forma que vai além das tradicionais "
            "manipulações algébricas."
        ),
    },
    {
        "semester": 2,
        "subject": "Algoritmos e Estruturas de Dados",
        "title": "Algorithms",
        "authors": "Jeff Erickson",
        "link": "https://jeffe.cs.illinois.edu/teaching/algorithms/",
        "introduction": (
            "O livro 'Algorithms' de Jeff Erickson é uma obra abrangente e rigorosa voltada para o estudo de algoritmos "
            "e estruturas de dados, amplamente utilizada em cursos avançados de ciência da computação. O autor apresenta "
            "os principais algoritmos e técnicas de projeto algorítmico, incluindo algoritmos de ordenação, busca, grafos, "
            "programação dinâmica, algoritmos gulosos e teoria de complexidade computacional."
        ),
    },
    {
        "semester": 2,
        "subject": "Algoritmos e Estruturas de Dados",
        "title": "CS50 Notes",
        "authors": "David J. Malan",
        "link": "https://cs50.harvard.edu/x/",
        "introduction": (
            "O material do CS50, desenvolvido por David J. Malan na Universidade de Harvard, é reconhecido mundialmente como "
            "um dos recursos mais acessíveis e completos para o aprendizado de ciência da computação e programação. "
            "O curso abrange desde conceitos fundamentais de computação, como representação binária de dados e operações "
            "lógicas, até tópicos avançados como algoritmos de busca e ordenação, estruturas de dados, programação web "
            "e segurança da informação."
        ),
    },
    {
        "semester": 2,
        "subject": "Elementos de Sistemas Computacionais",
        "title": "The Elements of Computing Systems",
        "authors": "Noam Nisan, Shimon Schocken",
        "link": "https://www.nand2tetris.org/",
        "introduction": (
            "O livro 'The Elements of Computing Systems', de Noam Nisan e Shimon Schocken, é uma obra didática e prática "
            "que propõe uma jornada do zero até a construção de um computador funcional, passando por todos os seus componentes "
            "fundamentais. Os autores partem dos princípios mais básicos da lógica booleana e constroem progressivamente, "
            "passo a passo, toda a estrutura de um sistema computacional moderno, incluindo portas lógicas, chips, memória, "
            "CPU, linguagem de máquina, assembler e sistema operacional."
        ),
    },
    {
        "semester": 2,
        "subject": "Elementos de Sistemas Computacionais",
        "title": "Computer Organization and Architecture",
        "authors": "OpenStax / Archive",
        "link": "https://archive.org/details/computer-organization-and-design-fifth-edition-the-hardware-software-interface-by-hennessy_202211",
        "introduction": (
            "O livro 'Computer Organization and Design' de David A. Patterson e John L. Hennessy é uma obra de referência "
            "fundamental no campo de organização e arquitetura de computadores, amplamente adotada em cursos universitários "
            "ao redor do mundo. Os autores abordam os princípios essenciais que regem o funcionamento interno dos computadores "
            "modernos, cobrindo desde a representação de dados e instruções até a implementação de processadores complexos."
        ),
    },
    {
        "semester": 2,
        "subject": "Fundamentos de Sistemas de Informação",
        "title": "Management Information Systems",
        "authors": "OpenStax",
        "link": "https://open.umn.edu/opentextbooks/textbooks/management-information-systems",
        "introduction": (
            "O livro 'Management Information Systems' da OpenStax apresenta uma introdução abrangente e acessível ao campo "
            "dos Sistemas de Informação Gerencial (SIG), explorando como as organizações utilizam a tecnologia da informação "
            "para tomar decisões estratégicas, melhorar a eficiência operacional e criar vantagens competitivas no mercado. "
            "Os autores abordam os fundamentos dos sistemas de informação, incluindo hardware, software, redes de comunicação "
            "e bancos de dados, contextualizando cada componente dentro do ambiente organizacional."
        ),
    },
    {
        "semester": 2,
        "subject": "Fundamentos de Sistemas de Informação",
        "title": "Principles of Information Systems",
        "authors": "Ralph Stair",
        "link": "https://archive.org/details/principlesofinfo0000stai_k3y9",
        "introduction": (
            "O livro 'Principles of Information Systems' de Ralph Stair e George Reynolds é uma obra introdutória e abrangente "
            "que apresenta os fundamentos dos sistemas de informação para estudantes de administração, computação e áreas correlatas. "
            "Os autores definem um sistema de informação como um conjunto de elementos interrelacionados que coletam, processam, "
            "armazenam e disseminam dados e informações para apoiar a tomada de decisão, o controle, a análise e a visualização "
            "em uma organização."
        ),
    },
]
