import unicodedata


# =========================================================
# BLACK CLOVER - personagens com estado e esquadrão
# =========================================================
# estado: "vivo", "morto" ou "desconhecido"
# esquadrao: touros_negros, aguia_prateada, leoes_carmesim,
#            rosa_azul, manto_verde, veado_aqua, pavão_coral,
#            orcas_roxas, corujas_oliva, touro_dourado,
#            nenhum, demonio, elfo, outro
# =========================================================

PERSONAGENS = [
    # ---------- TOUROS NEGROS ----------
    {"nome": "Asta", "cabelo": "cinza", "olhos": "verdes", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "antimagia", "arma": "espada", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Yami Sukehiro", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "hino", "poder": "escuridao", "arma": "katana", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Noelle Silva", "cabelo": "prateado", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "agua", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Finral Roulacase", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "espacial", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Magna Swing", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "fogo", "arma": "bat", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Luck Voltia", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "raio", "arma": "punhos", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Gauche Adlai", "cabelo": "loiro", "olhos": "roxos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "espelho", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Vanessa Enoteca", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "destino", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Charmy Pappitson", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "alimentacao", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Gordon Agrippa", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "maldicao", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Grey", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "transformacao", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Henry Legolant", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "absorcao", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Zora Ideale", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "armadilha", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Nacht Faust", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "sombras", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Nero", "cabelo": "preto", "olhos": "negros", "altura": "baixo", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "selo", "arma": "grimorio", "estado": "vivo", "esquadrao": "touros_negros"},
    {"nome": "Liebe", "cabelo": "preto", "olhos": "vermelhos", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "demonio", "poder": "antimagia", "arma": "espada", "estado": "vivo", "esquadrao": "touros_negros"},

    # ---------- TOURO DOURADO ----------
    {"nome": "Yuno", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "William Vangeance", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "arvore", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Langris Vaude", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "espacial", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Klaus Lunettes", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "aco", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Mimosa Vermillion", "cabelo": "loiro", "olhos": "verdes", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "plantas", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Alecdora Sandler", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "areia", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Hamon Caseus", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "vidro", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Shiren Tium", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "rocha", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},
    {"nome": "Letoile Becquerel", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "bussola", "arma": "grimorio", "estado": "vivo", "esquadrao": "touro_dourado"},

    # ---------- ÁGUIA PRATEADA ----------
    {"nome": "Nozel Silva", "cabelo": "prateado", "olhos": "roxos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "mercurio", "arma": "grimorio", "estado": "vivo", "esquadrao": "aguia_prateada"},
    {"nome": "Nebra Silva", "cabelo": "prateado", "olhos": "roxos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "nevoa", "arma": "grimorio", "estado": "vivo", "esquadrao": "aguia_prateada"},
    {"nome": "Solid Silva", "cabelo": "prateado", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "agua", "arma": "grimorio", "estado": "vivo", "esquadrao": "aguia_prateada"},

    # ---------- LEÕES CARMESIM ----------
    {"nome": "Fuegoleon Vermillion", "cabelo": "vermelho", "olhos": "vermelhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "fogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "leoes_carmesim"},
    {"nome": "Mereoleona Vermillion", "cabelo": "vermelho", "olhos": "vermelhos", "altura": "alto", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "fogo", "arma": "punhos", "estado": "vivo", "esquadrao": "leoes_carmesim"},
    {"nome": "Leopold Vermillion", "cabelo": "vermelho", "olhos": "vermelhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "fogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "leoes_carmesim"},
    {"nome": "Kirsch Vermillion", "cabelo": "vermelho", "olhos": "vermelhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "cerejeira", "arma": "grimorio", "estado": "vivo", "esquadrao": "leoes_carmesim"},
    {"nome": "Randall Luftair", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "leoes_carmesim"},

    # ---------- ROSA AZUL ----------
    {"nome": "Charlotte Roselei", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "espinhos", "arma": "grimorio", "estado": "vivo", "esquadrao": "rosa_azul"},
    {"nome": "Sol Marron", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "terra", "arma": "grimorio", "estado": "vivo", "esquadrao": "rosa_azul"},
    {"nome": "Paulie Angel", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "cristal", "arma": "grimorio", "estado": "vivo", "esquadrao": "rosa_azul"},

    # ---------- MANTO VERDE ----------
    {"nome": "Jack The Ripper", "cabelo": "preto", "olhos": "verdes", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "corte", "arma": "grimorio", "estado": "vivo", "esquadrao": "manto_verde"},
    {"nome": "Sekke Bronzazza", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "bronze", "arma": "grimorio", "estado": "vivo", "esquadrao": "manto_verde"},
    {"nome": "En Ringard", "cabelo": "verde", "olhos": "verdes", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "fungo", "arma": "grimorio", "estado": "vivo", "esquadrao": "manto_verde"},

    # ---------- VEADO AQUA ----------
    {"nome": "Rill Boismortier", "cabelo": "loiro", "olhos": "azuis", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "pintura", "arma": "grimorio", "estado": "vivo", "esquadrao": "veado_aqua"},
    {"nome": "Fragil Tormenta", "cabelo": "loiro", "olhos": "azuis", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "neve", "arma": "grimorio", "estado": "vivo", "esquadrao": "veado_aqua"},
    {"nome": "Walter", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "gelo", "arma": "grimorio", "estado": "vivo", "esquadrao": "veado_aqua"},

    # ---------- PAVÃO CORAL ----------
    {"nome": "Dorothy Unsworth", "cabelo": "loiro", "olhos": "azuis", "altura": "baixo", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "sonho", "arma": "grimorio", "estado": "vivo", "esquadrao": "pavao_coral"},
    {"nome": "Rick Cornell", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "calor", "arma": "grimorio", "estado": "vivo", "esquadrao": "pavao_coral"},
    {"nome": "Demitri Brint", "cabelo": "preto", "olhos": "negros", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "sangue", "arma": "grimorio", "estado": "vivo", "esquadrao": "pavao_coral"},

    # ---------- ORCAS ROXAS ----------
    {"nome": "Kaiser Granvorka", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "orcas_roxas"},
    {"nome": "Gueldre Poizot", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "veneno", "arma": "grimorio", "estado": "morto", "esquadrao": "orcas_roxas"},
    {"nome": "Xerx Lügner", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "orcas_roxas"},
    {"nome": "Digit Taliss", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "gelo", "arma": "grimorio", "estado": "morto", "esquadrao": "orcas_roxas"},

    # ---------- CORUJAS OLIVA ----------
    {"nome": "Gadjah", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "heart", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "corujas_oliva"},
    {"nome": "Lovilia", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "perfume", "arma": "grimorio", "estado": "vivo", "esquadrao": "corujas_oliva"},

    # ---------- REALEZA / WIZARD KING ----------
    {"nome": "Julius Novachrono", "cabelo": "loiro", "olhos": "verdes", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "tempo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Lumiel Silvamillion Clover", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "clover", "poder": "luz", "arma": "espada", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Marx Francois", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "memoria", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Owen", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "cura", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Augustus Kira Clover XIII", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "clover", "poder": "luz", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Damnatio Kira", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "escala", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Cob Portaport", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "espacial", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},

    # ---------- ELFOS ----------
    {"nome": "Patry", "cabelo": "loiro", "olhos": "verdes", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "luz", "arma": "espada", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Licht", "cabelo": "branco", "olhos": "azuis", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "espada", "arma": "espada", "estado": "morto", "esquadrao": "elfo"},
    {"nome": "Rhya", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "copiar", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Fana", "cabelo": "loiro", "olhos": "verdes", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "elfo", "poder": "fogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Vetto", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "besta", "arma": "punhos", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Ronne", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "cura", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Drowa", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "espelho", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Eclat", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "elfo", "poder": "luz", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},
    {"nome": "Latry", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "adulto", "genero": "masculino", "origem": "elfo", "poder": "ilusao", "arma": "grimorio", "estado": "vivo", "esquadrao": "elfo"},

    # ---------- DEMÓNIOS / ZOGRATIS ----------
    {"nome": "Dante Zogratis", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "spade", "poder": "gravidade", "arma": "grimorio", "estado": "morto", "esquadrao": "demonio"},
    {"nome": "Zenon Zogratis", "cabelo": "prateado", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "spade", "poder": "espacial", "arma": "grimorio", "estado": "morto", "esquadrao": "demonio"},
    {"nome": "Vanica Zogratis", "cabelo": "loiro", "olhos": "verdes", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "spade", "poder": "sangue", "arma": "grimorio", "estado": "vivo", "esquadrao": "demonio"},
    {"nome": "Lucius Zogratis", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "spade", "poder": "alma", "arma": "grimorio", "estado": "vivo", "esquadrao": "demonio"},
    {"nome": "Megicula", "cabelo": "loiro", "olhos": "verdes", "altura": "medio", "idade": "idoso", "genero": "feminino", "origem": "demonio", "poder": "maldicao", "arma": "grimorio", "estado": "vivo", "esquadrao": "demonio"},
    {"nome": "Lucifero", "cabelo": "preto", "olhos": "vermelhos", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "demonio", "poder": "gravidade", "arma": "grimorio", "estado": "vivo", "esquadrao": "demonio"},

    # ---------- REINO DO CORAÇÃO ----------
    {"nome": "Lolopechika", "cabelo": "rosa", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "heart", "poder": "agua", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Gifso", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "adulto", "genero": "masculino", "origem": "heart", "poder": "jogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Gio", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "heart", "poder": "vento", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Kahono", "cabelo": "azul", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "heart", "poder": "som", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Kiato", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "heart", "poder": "espada", "arma": "espada", "estado": "vivo", "esquadrao": "nenhum"},

    # ---------- REINO DE SPADE / DIAMANTE ----------
    {"nome": "Ladros", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "spade", "poder": "magma", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Mars", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "diamond", "poder": "cristal", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Fana (humana)", "cabelo": "loiro", "olhos": "verdes", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "diamond", "poder": "fogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Lotus Whomalt", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "diamond", "poder": "cinzas", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Morris Libardirt", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "diamond", "poder": "modificacao", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},

    # ---------- OLHO DO SOL DA MEIA-NOITE ----------
    {"nome": "Rades Spirito", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "necromancia", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Valtos", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "espacial", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Heath Grice", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "gelo", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Catherine", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "maldicao", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},

    # ---------- FLORESTA DAS BRUXAS ----------
    {"nome": "Rainha das Bruxas", "cabelo": "preto", "olhos": "negros", "altura": "alto", "idade": "idoso", "genero": "feminino", "origem": "floresta", "poder": "sangue", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Samantha Kravitz", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "floresta", "poder": "cura", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Elvira Aguirre", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "floresta", "poder": "veneno", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},

    # ---------- ALDEIA DE HAGE ----------
    {"nome": "Orsi Orfai", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Lily Aquaria", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "agua", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Nash", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Recca", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Aruru", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Hollo", "cabelo": "castanho", "olhos": "castanhos", "altura": "baixo", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},

    # ---------- OUTROS ----------
    {"nome": "Secre Swallowtail", "cabelo": "preto", "olhos": "negros", "altura": "baixo", "idade": "idoso", "genero": "feminino", "origem": "clover", "poder": "selo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Fanzell Kruger", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "diamond", "poder": "vento", "arma": "espada", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Dominante Code", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "diamond", "poder": "gelo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Mariella", "cabelo": "loiro", "olhos": "azuis", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "fogo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Theresa Rapual", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "idoso", "genero": "feminino", "origem": "clover", "poder": "cura", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Rebecca Scarlet", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "nenhum", "arma": "nenhuma", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Marie Adlai", "cabelo": "loiro", "olhos": "roxos", "altura": "baixo", "idade": "jovem", "genero": "feminino", "origem": "clover", "poder": "maldicao", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Revchi Salik", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "corrente", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Salim Hapshass", "cabelo": "castanho", "olhos": "castanhos", "altura": "medio", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "raio", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Zara Ideale", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "armadilha", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Morgen Faust", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "jovem", "genero": "masculino", "origem": "clover", "poder": "sombra", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Acier Silva", "cabelo": "prateado", "olhos": "roxos", "altura": "alto", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "aco", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Licita", "cabelo": "preto", "olhos": "negros", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "absorcao", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
    {"nome": "Ichika Yami", "cabelo": "preto", "olhos": "negros", "altura": "medio", "idade": "jovem", "genero": "feminino", "origem": "hino", "poder": "escuridao", "arma": "katana", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Jester Garandros", "cabelo": "loiro", "olhos": "azuis", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "clover", "poder": "ilusao", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Princia Funnybunny", "cabelo": "rosa", "olhos": "azuis", "altura": "medio", "idade": "adulto", "genero": "feminino", "origem": "clover", "poder": "tempo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Edward Avalaché", "cabelo": "branco", "olhos": "azuis", "altura": "alto", "idade": "idoso", "genero": "masculino", "origem": "clover", "poder": "gelo", "arma": "grimorio", "estado": "vivo", "esquadrao": "nenhum"},
    {"nome": "Conrad Leto", "cabelo": "castanho", "olhos": "castanhos", "altura": "alto", "idade": "adulto", "genero": "masculino", "origem": "clover", "poder": "barreira", "arma": "grimorio", "estado": "morto", "esquadrao": "nenhum"},
]


# =========================================================
# GRUPOS (para decidir quando é "amarelo")
# =========================================================

GRUPOS = {
    "cabelo": {
        "escuro": ["preto", "castanho", "cinza"],
        "claro": ["loiro", "branco", "prateado"],
        "colorido": ["rosa", "azul", "vermelho", "verde"],
    },
    "olhos": {
        "escuros": ["negros", "castanhos"],
        "claros": ["azuis", "verdes", "cinza"],
        "especiais": ["brancos", "vermelhos", "roxos"],
    },
    "altura": {
        "pequeno": ["baixo"],
        "medio": ["medio"],
        "grande": ["alto"],
    },
    "idade": {
        "jovem": ["jovem"],
        "adulto": ["adulto"],
        "idoso": ["idoso"],
    },
    "genero": {
        "m": ["masculino"],
        "f": ["feminino"],
        "outro": ["outro"],
    },
    "origem": {
        "reino": ["clover", "spade", "heart", "diamond"],
        "nao_humano": ["elfo", "demonio"],
        "outro": ["hino", "floresta"],
    },
    "poder": {
        "elemental": ["fogo", "agua", "vento", "terra", "gelo", "raio"],
        "fisico": ["antimagia", "corte", "punhos", "besta", "espada"],
    },
    "arma": {
        "corte": ["katana", "espada"],
        "impacto": ["punhos", "bat"],
        "magica": ["grimorio"],
        "outro": ["nenhuma"],
    },
    "estado": {
        "vida": ["vivo"],
        "morte": ["morto"],
        "incerto": ["desconhecido"],
    },
    "esquadrao": {
        "touros": ["touros_negros"],
        "aguia": ["aguia_prateada"],
        "leoes": ["leoes_carmesim"],
        "rosa": ["rosa_azul"],
        "manto": ["manto_verde"],
        "veado": ["veado_aqua"],
        "pavao": ["pavao_coral"],
        "orcas": ["orcas_roxas"],
        "corujas": ["corujas_oliva"],
        "touro_dourado": ["touro_dourado"],
        "sem_esquadrao": ["nenhum"],
        "nao_humano": ["demonio", "elfo"],
    },
}


# =========================================================
# CONFIGURAÇÃO DE EXIBIÇÃO
# =========================================================

# Agora também mostramos estado e esquadrão na tabela
CARACTERISTICAS = [
    "cabelo", "olhos", "altura", "idade",
    "genero", "origem", "poder", "arma",
    "estado", "esquadrao",
]

NOMES_EXIBIDOS = {
    "cabelo": "Cabelo",
    "olhos": "Olhos",
    "altura": "Altura",
    "idade": "Idade",
    "genero": "Género",
    "origem": "Origem",
    "poder": "Poder",
    "arma": "Arma",
    "estado": "Estado",
    "esquadrao": "Esquadrão",
}

# Nomes bonitos para os valores de "esquadrao" e "estado"
VALORES_BONITOS = {
    "touros_negros": "Touros Negros",
    "aguia_prateada": "Águia Prateada",
    "leoes_carmesim": "Leões Carmesim",
    "rosa_azul": "Rosa Azul",
    "manto_verde": "Manto Verde",
    "veado_aqua": "Veado Aqua",
    "pavao_coral": "Pavão Coral",
    "orcas_roxas": "Orcas Roxas",
    "corujas_oliva": "Corujas Oliva",
    "touro_dourado": "Touro Dourado",
    "nenhum": "Sem esquadrão",
    "demonio": "Demónio",
    "elfo": "Elfo",
    "vivo": "Vivo",
    "morto": "Morto",
    "desconhecido": "Desconhecido",
}


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def valor_bonito(valor):
    """Converte 'touros_negros' em 'Touros Negros'."""
    return VALORES_BONITOS.get(valor, valor.replace("_", " ").title())


def valor_para_grupo(caracteristica, valor):
    grupos = GRUPOS.get(caracteristica, {})
    for nome_grupo, valores in grupos.items():
        if valor in valores:
            return nome_grupo
    return None


def comparar(palpite, secreto):
    resultado = []
    for campo in CARACTERISTICAS:
        v_palpite = palpite[campo]
        v_secreto = secreto[campo]

        if v_palpite == v_secreto:
            cor = "verde"
        else:
            g1 = valor_para_grupo(campo, v_palpite)
            g2 = valor_para_grupo(campo, v_secreto)
            cor = "amarelo" if (g1 is not None and g1 == g2) else "vermelho"

        resultado.append({
            "campo": campo,
            "nome": NOMES_EXIBIDOS[campo],
            "valor": valor_bonito(v_palpite),
            "cor": cor,
        })
    return resultado


def procurar(termo):
    termo_norm = normalizar(termo.strip())
    if not termo_norm:
        return [p["nome"] for p in PERSONAGENS]
    return [
        p["nome"] for p in PERSONAGENS
        if normalizar(p["nome"]).startswith(termo_norm)
    ]


def obter_personagem(nome):
    for p in PERSONAGENS:
        if p["nome"] == nome:
            return p
    return None