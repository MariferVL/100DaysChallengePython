stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lista_palabras = ['sobre', 'entre', 'cuando', 'tambien', 'habia', 'hasta', 'desde', 'porque', 'puede', 'todos', 'parte',
                  'tiene', 'donde', 'tiempo', 'mismo', 'ahora', 'despues', 'otros', 'aunque', 'gobierno', 'durante',
                  'siempre', 'tanto', 'segun', 'menos', 'mundo', 'antes', 'estado', 'contra', 'forma', 'hacer',
                  'general', 'estaba', 'estos', 'presidente', 'mayor', 'hacia', 'ellos', 'hecho', 'primera', 'mucho',
                  'mientras', 'ademas', 'quien', 'momento', 'millones', 'españa', 'hombre', 'estan', 'lugar', 'madrid',
                  'nacional', 'trabajo', 'otras', 'mejor', 'nuevo', 'decir', 'algunos', 'entonces', 'todas', 'politica',
                  'viviana', 'luego', 'pasado', 'primer', 'medio', 'estas', 'tenia', 'nunca', 'poder', 'veces',
                  'embargo', 'partido', 'personas', 'grupo', 'cuenta', 'pueden', 'tienen', 'misma', 'nueva', 'fueron',
                  'mujer', 'frente', 'cosas', 'ciudad', 'fernando', 'social', 'manera', 'tener', 'sistema', 'historia',
                  'muchos', 'cuatro', 'dentro', 'nuestro', 'punto', 'cualquier', 'noche', 'parece', 'haber',
                  'situacion', 'fuera', 'grandes', 'nuestra', 'ejemplo', 'acuerdo', 'habian', 'usted', 'estados',
                  'jacinta', 'nadie', 'almendra', 'paises', 'horas', 'posible', 'tarde', 'importante', 'guerra',
                  'desarrollo', 'proceso', 'realidad', 'sentido', 'cambio', 'estar', 'numero', 'sociedad', 'centro',
                  'padre', 'gente', 'final', 'relacion', 'cuerpo', 'incluso', 'traves', 'ultimo', 'madre', 'problemas',
                  'cinco', 'carlos', 'hombres', 'informacion', 'muerte', 'nombre', 'algunas', 'publico', 'mujeres',
                  'siglo', 'todavia', 'meses', 'mañana', 'nosotros', 'muchas', 'pueblo', 'alguna', 'problema',
                  'derecho', 'verdad', 'maria', 'unidos', 'podria', 'seria', 'junto', 'cabeza', 'aquel', 'cuanto',
                  'tierra', 'equipo', 'segundo', 'director', 'dicho', 'cierto', 'casos', 'manos', 'nivel', 'podia',
                  'familia', 'largo', 'partir', 'falta', 'llegar', 'propio', 'ministro', 'primero', 'seguridad',
                  'hemos', 'trata', 'algun', 'respecto', 'semana', 'varios', 'señor', 'quienes', 'proyecto', 'mercado',
                  'mayoria', 'claro', 'pesetas', 'orden', 'español', 'buena', 'quiere', 'aquella', 'programa',
                  'palabras', 'internacional', 'segunda', 'empresa', 'puesto', 'propia', 'libro', 'igual', 'politico',
                  'persona', 'ultimos', 'ellas', 'total', 'tengo', 'española', 'condiciones', 'mexico', 'fuerza',
                  'unico', 'accion', 'policia', 'puerta', 'pesar', 'calle', 'interior', 'tampoco', 'musica', 'ningun',
                  'vista', 'campo', 'hubiera', 'saber', 'obras', 'razon', 'niños', 'presencia', 'dinero', 'comision',
                  'antonio', 'servicio', 'ultima', 'ciento', 'estoy', 'hablar', 'minutos', 'produccion', 'fortuna',
                  'multimillonario', 'unicornio', 'camino', 'quien', 'fondo', 'direccion', 'papel', 'demas',
                  'barcelona', 'especial', 'diferentes', 'capital', 'ambos', 'europa', 'libertad', 'relaciones',
                  'espacio', 'medios', 'actual', 'poblacion', 'empresas', 'estudio', 'salud', 'servicios', 'principio',
                  'siendo', 'cultura', 'anterior', 'media', 'mediante', 'primeros', 'sector', 'imagen', 'medida',
                  'deben', 'datos', 'consejo', 'personal', 'interes', 'julio', 'grupos', 'miembros', 'ninguna',
                  'existe', 'movimiento', 'visto', 'llego', 'puntos', 'actividad', 'bueno', 'dificil', 'joven',
                  'futuro', 'aquellos', 'pronto', 'hacia', 'nuevos', 'nuestros', 'estaban', 'posibilidad', 'sigue',
                  'cerca', 'resultados', 'educacion', 'atencion', 'gonzalez', 'capacidad', 'efecto', 'necesario',
                  'valor', 'investigacion', 'siguiente', 'figura', 'central', 'comunidad', 'necesidad', 'serie',
                  'organizacion', 'nuevas', 'calidad']

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]
