# abs(): Retorna o valor absoluto de um número.
#   # Programa para calcular a distância entre dois pontos em uma linha numérica
#   def distance(x, y):
#       return abs(x - y)

#   point1 = -5
#   point2 = 10
#   print(f"A distância entre {point1} e {point2} é {distance(point1, point2)}")

# ==================================================================================
# all(): Retorna True se todos os elementos de um iterável são verdadeiros (ou se o iterável está vazio).
# # Programa para verificar se todos os números em uma lista são positivos
# def all_positive(numbers):
#     return all(num > 0 for num in numbers)

# numbers = [1, 2, 3, 4, 5]
# print(f"Todos os números são positivos: {all_positive(numbers)}")

# ==================================================================================S
# any(): Retorna True se algum elemento de um iterável é verdadeiro. Se o iterável está vazio, retorna False.
#   # Programa para verificar se há algum número par em uma lista
#   def any_even(numbers):
#       return any(num % 2 == 0 for num in numbers)

#   numbers = [1, 3, 5, 7, 2]
#   print(f"Há algum número par: {any_even(numbers)}")

# ==================================================================================
# ascii(): Retorna uma versão "readable" de um objeto, substituindo caracteres não-ASCII por escapes.
# # Programa para converter uma string com caracteres não-ASCII
# def to_ascii(text):
#     return ascii(text)

# text = "Olá, mundo!"
# print(f"Versão ASCII da string: {to_ascii(text)}")

# ==================================================================================
# bin(): Converte um número inteiro em uma string binária.
#   # Programa para converter uma lista de números decimais para binários
#   def convert_to_binary(numbers):
#       return [bin(num) for num in numbers]

#   numbers = [1, 2, 3, 4, 5]
#   print(f"Versão binária dos números: {convert_to_binary(numbers)}")

# ==================================================================================
# bool(): Converte um valor para um tipo booleano.
#   # Programa para converter vários valores para booleano
#   values = [0, 1, "", "Python", [], [1, 2, 3]]
#   bool_values = [bool(value) for value in values]
#   print(f"Valores booleanos: {bool_values}")

# ==================================================================================
# bytearray(): Retorna um novo array de bytes.
#   # Programa para criar uma sequência mutável de bytes a partir de uma string
#   def string_to_bytearray(text):
#       return bytearray(text, 'utf-8')

#   text = "Hello"
#   byte_arr = string_to_bytearray(text)
#   print(f"Bytearray: {byte_arr}")

# ==================================================================================
# bytes(): Retorna um novo objeto de bytes.
# # Programa para criar uma sequência imutável de bytes a partir de uma string
# def string_to_bytes(text):
#     return bytes(text, 'utf-8')

# text = "Hello"
# byte_seq = string_to_bytes(text)
# print(f"Bytes: {byte_seq}")

# ==================================================================================
# callable(): Retorna True se o objeto parece ser chamável (callable).
# # Programa para verificar se os objetos são chamáveis
# def example_function():
#     return "I am a function"

# example_lambda = lambda x: x * 2
# example_string = "I am not callable"

# print(f"example_function é chamável: {callable(example_function)}")
# print(f"example_lambda é chamável: {callable(example_lambda)}")
# print(f"example_string é chamável: {callable(example_string)}")

# ==================================================================================
# chr(): Retorna a string representando um caractere cujo código Unicode é o número inteiro passado.
#   # Programa para converter códigos Unicode para caracteres
#   def unicode_to_char(codes):
#       return [chr(code) for code in codes]

#   codes = [65, 66, 67, 97, 98, 99]
#   characters = unicode_to_char(codes)
#   print(f"Caracteres: {characters}")

# ==================================================================================
# classmethod(): Retorna um método de classe para a função passada.
#   # Programa para demonstrar o uso de métodos de classe
#   class MyClass:
#       count = 0

#       def __init__(self):
#           MyClass.count += 1

#       @classmethod
#       def get_instance_count(cls):
#           return cls.count

#   a = MyClass()
#   b = MyClass()
#   c = MyClass()
#   print(f"Instâncias criadas: {MyClass.get_instance_count()}")

# ==================================================================================
# compile(): Compila a fonte em código de objeto ou AST.
#   # Programa para compilar e executar código Python a partir de uma string
#   code = """
#   def greet(name):
#       return f'Hello, {name}'

#   print(greet('World'))
#   """

#   compiled_code = compile(code, '<string>', 'exec')
#   exec(compiled_code)

# ==================================================================================
# complex(): Cria um número complexo.
#   # Programa para realizar operações com números complexos
#   def add_complex_numbers(c1, c2):
#       return c1 + c2

#   c1 = complex(2, 3)
#   c2 = complex(1, 4)
#   result = add_complex_numbers(c1, c2)
#   print(f"Soma de {c1} e {c2} é {result}")

# ==================================================================================
# delattr(): Deleta um atributo de um objeto.
# # Programa para demonstrar a remoção de um atributo de um objeto
# class MyClass:
#     def __init__(self):
#         self.attribute = 'value'

# obj = MyClass()
# print(f"Atributo antes de deletar: {hasattr(obj, 'attribute')}")
# delattr(obj, 'attribute')
# print(f"Atributo após deletar: {hasattr(obj, 'attribute')}")

# ==================================================================================
# dict(): Cria um novo dicionário.
#   # Programa para criar um dicionário a partir de uma lista de tuplas
#   def list_to_dict(pairs):
#       return dict(pairs)

#   pairs = [('a', 1), ('b', 2), ('c', 3)]
#   dictionary = list_to_dict(pairs)
#   print(f"Dicionário: {dictionary}")
  
# ==================================================================================
# dir(): Tenta retornar uma lista de atributos válidos para o objeto.
# # Programa para listar os atributos de um objeto
# class MyClass:
#     def __init__(self):
#         self.attribute = 'value'

# obj = MyClass()
# print(f"Atributos de obj: {dir(obj)}")

# ==================================================================================
# divmod(): Toma dois números (a e b) e retorna uma tupla (a // b, a % b).
# # Programa para dividir dois números e obter o quociente e o resto
# def divide_and_remainder(a, b):
#     return divmod(a, b)

# a = 9
# b = 4
# quotient, remainder = divide_and_remainder(a, b)
# print(f"{a} dividido por {b} dá quociente {quotient} e resto {remainder}")

# ==================================================================================
# enumerate(): Retorna um objeto enumerado.
#   # Programa para enumerar os itens de uma lista
#   def enumerate_items(items):
#       return list(enumerate(items, start=1))

#   items = ['apple', 'banana', 'cherry']
#   enumerated_items = enumerate_items(items)
#   print(f"Itens enumerados: {enumerated_items}")

# ==================================================================================
# eval(): Avalia uma expressão de string.
# # Programa para avaliar expressões matemáticas a partir de strings
# def evaluate_expression(expression):
#     return eval(expression)

# expression = "2 + 3 * 5"
# result = evaluate_expression(expression)
# print(f"Resultado da expressão '{expression}': {result}")

# ==================================================================================
# exec(): Executa o código de um objeto de código (ou string) Python.
#   # Programa para executar código Python a partir de uma string
#   code = """
#   for i in range(5):
#       print(f'Número: {i}')
#   """

#   exec(code)

# ==================================================================================
# filter(): Constrói um iterador a partir de elementos de um iterável para os quais uma função retorna verdadeiro.
#   # Programa para filtrar números pares de uma lista
#   def filter_even(numbers):
#       return list(filter(lambda x: x % 2 == 0, numbers))

#   numbers = [1, 2, 3, 4, 5, 6]
#   even_numbers = filter_even(numbers)
#   print(f"Números pares: {even_numbers}")

# ==================================================================================
# float(): Converte um número ou string para um número de ponto flutuante.
# # Programa para converter uma lista de strings para números de ponto flutuante
# def convert_to_float(strings):
#     return [float(s) for s in strings]

# strings = ["1.1", "2.2", "3.3"]
# float_numbers = convert_to_float(strings)
# print(f"Números de ponto flutuante: {float_numbers}")

# ==================================================================================
# format(): Formata um valor de acordo com o formato especificado.
#   # Programa para formatar uma string com múltiplos valores
#   def format_string(name, age):
#       return "Name: {name}, Age: {age}".format(name=name, age=age)

#   name = "Alice"
#   age = 30
#   formatted_string = format_string(name, age)
#   print(formatted_string)

# ==================================================================================
# frozenset(): Retorna um objeto conjunto imutável.
# # Programa para criar um conjunto imutável
# def create_frozenset(elements):
#     return frozenset(elements)

# elements = [1, 2, 3, 2, 1]
# immutable_set = create_frozenset(elements)
# print(f"Conjunto imutável: {immutable_set}")

# ==================================================================================
# getattr(): Retorna o valor do atributo nomeado do objeto.
#   # Programa para obter o valor de um atributo de um objeto
#   class MyClass:
#       def __init__(self, value):
#           self.attribute = value

#   obj = MyClass("some value")
#   attribute_value = getattr(obj, 'attribute', 'default value')
#   print(f"Valor do atributo: {attribute_value}")

# ==================================================================================
# globals(): Retorna um dicionário representando a tabela de símbolos globais atuais.
# # Programa para listar todas as variáveis globais
# def list_globals():
#     return globals()

# print(f"Variáveis globais: {list_globals()}")

# ==================================================================================
# hasattr(): Retorna True se o objeto tiver um atributo com o nome fornecido.
#   # Programa para verificar se um objeto tem um atributo específico
#   class MyClass:
#       def __init__(self):
#           self.attribute = 'value'

#   obj = MyClass()
#   print(f"Objeto tem 'attribute': {hasattr(obj, 'attribute')}")
#   print(f"Objeto tem 'nonexistent': {hasattr(obj, 'nonexistent')}")

# ==================================================================================
# hash(): Retorna o valor hash de um objeto.
#   # Programa para obter o valor hash de vários tipos de dados
#   def hash_values(values):
#       return [hash(value) for value in values]

#   values = [1, "hello", (1, 2, 3)]
#   hashes = hash_values(values)
#   print(f"Hashes: {hashes}")

# ==================================================================================
# help(): Invoca o sistema de ajuda integrado.
# # Programa para exibir ajuda sobre a função len
# help(len)

# ==================================================================================
# hex(): Converte um número inteiro em uma string hexadecimal.
#   # Programa para converter uma lista de números decimais para hexadecimais
#   def convert_to_hex(numbers):
#       return [hex(num) for num in numbers]

#   numbers = [10, 255, 1024]
#   hex_numbers = convert_to_hex(numbers)
#   print(f"Números hexadecimais: {hex_numbers}")

# ==================================================================================
# id(): Retorna o "identity" de um objeto.
#   # Programa para obter o identificador único de objetos
#   a = "hello"
#   b = [1, 2, 3]
#   print(f"ID de a: {id(a)}")
#   print(f"ID de b: {id(b)}")

# ==================================================================================
# input(): Lê uma linha da entrada, converte-a em uma string (retirando o caractere de nova linha final).
# # Programa para obter a entrada do usuário e imprimi-la
# user_input = input("Digite algo: ")
# print(f"Você digitou: {user_input}")

# ==================================================================================
# int(): Converte um número ou string para um inteiro.
#   # Programa para converter uma lista de strings para inteiros
#   def convert_to_int(strings):
#       return [int(s) for s in strings]

#   strings = ["1", "2", "3"]
#   int_numbers = convert_to_int(strings)
#   print(f"Números inteiros: {int_numbers}")

# ==================================================================================
# isinstance(): Retorna True se o objeto argumentado é uma instância da classe argumentada ou uma instância de uma subclasse.

# ===# Programa para verificar o tipo de vários objetos
# def check_instance(objects, cls):
#     return [isinstance(obj, cls) for obj in objects]

# objects = [1, "hello", 3.5, (1, 2)]
# results = check_instance(objects, str)
# print(f"São instâncias de str: {results}")
# ===============================================================================
# issubclass(): Retorna True se a classe argumentada é uma subclasse da classe argumentada.
#   # Programa para verificar a relação de subclasses
#   class Animal:
#       pass

#   class Dog(Animal):
#       pass

#   print(f"Dog é subclasse de Animal: {issubclass(Dog, Animal)}")
#   print(f"Animal é subclasse de Dog: {issubclass(Animal, Dog)}")

# ==================================================================================
# iter(): Retorna um iterador de um objeto.
# # Programa para criar um iterador e percorrê-lo
# def iterate_items(items):
#     iterator = iter(items)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break

# items = [1, 2, 3]
# iterate_items(items)

# ==================================================================================
# len(): Retorna o número de itens de um objeto.
#   # Programa para obter o comprimento de várias coleções
#   def get_lengths(collections):
#       return [len(collection) for collection in collections]

#   collections = ["hello", [1, 2, 3], (4, 5, 6)]
#   lengths = get_lengths(collections)
#   print(f"Comprimentos: {lengths}")

# ==================================================================================
# list(): Cria uma lista.
#   # Programa para criar uma lista a partir de uma string
#   def string_to_list(s):
#       return list(s)

#   s = "hello"
#   list_s = string_to_list(s)
#   print(f"Lista: {list_s}")

# ==================================================================================
# locals(): Atualiza e retorna um dicionário representando a tabela de símbolos locais atuais.
#   # Programa para listar variáveis locais dentro de uma função
#   def list_locals():
#       a = 1
#       b = "hello"
#       return locals()

#   print(f"Variáveis locais: {list_locals()}")

# ==================================================================================
# map(): Aplica uma função a todos os itens de um iterável.
# # Programa para aplicar uma função a todos os itens de uma lista
# def square(numbers):
#     return list(map(lambda x: x**2, numbers))

# numbers = [1, 2, 3, 4]
# squared_numbers = square(numbers)
# print(f"Números ao quadrado: {squared_numbers}")

# ==================================================================================
# max(): Retorna o maior item em um iterável ou o maior de dois ou mais argumentos.
#   # Programa para encontrar o maior número em uma lista
#   def find_max(numbers):
#       return max(numbers)

#   numbers = [1, 2, 3, 4, 5]
#   max_number = find_max(numbers)
#   print(f"Maior número: {max_number}")

# ==================================================================================
# memoryview(): Retorna um "view object" da memória de um objeto.
# # Programa para criar uma visão de memória de um objeto de bytes
# def create_memoryview(data):
#     return memoryview(data)

# data = b"hello"
# mem_view = create_memoryview(data)
# print(f"Memory view: {mem_view}")
# print(f"Primeiro byte: {mem_view[0]}")

# ==================================================================================
# min(): Retorna o menor item em um iterável ou o menor de dois ou mais argumentos.
# # Programa para encontrar o menor número em uma lista
# def find_min(numbers):
#     return min(numbers)

# numbers = [1, 2, 3, 4, 5]
# min_number = find_min(numbers)
# print(f"Menor número: {min_number}")

# ==================================================================================
# next(): Recupera o próximo item de um iterador.
#   # Programa para obter o próximo item de um iterador
#   def get_next(iterator):
#       try:
#           return next(iterator)
#       except StopIteration:
#           return "Fim do iterador"

#   iterator = iter([1, 2, 3])
#   print(get_next(iterator))  # Saída: 1
#   print(get_next(iterator))  # Saída: 2
#   print(get_next(iterator))  # Saída: 3
#   print(get_next(iterator))  # Saída: Fim do iterador

# ==================================================================================
# object(): Retorna um novo objeto vazio.
# # Programa para criar um novo objeto vazio
# obj = object()
# print(f"Novo objeto: {obj}")

# ==================================================================================
# oct(): Converte um número inteiro em uma string octal.
#   # Programa para converter uma lista de números decimais para octais
#   def convert_to_oct(numbers):
#       return [oct(num) for num in numbers]

#   numbers = [8, 16, 64]
#   oct_numbers = convert_to_oct(numbers)
#   print(f"Números octais: {oct_numbers}")

# ==================================================================================
# open(): Abre um arquivo e retorna um objeto de arquivo.
#   # Programa para ler o conteúdo de um arquivo
#   def read_file(filename):
#       with open(filename, 'r') as file:
#           return file.read()

#   filename = 'example.txt'
#   print(f"Conteúdo do arquivo: {read_file(filename)}")

# ==================================================================================
# ord(): Retorna o inteiro representando o ponto de código Unicode para um caractere dado.
#   # Programa para converter caracteres em seus valores Unicode
#   def char_to_unicode(chars):
#       return [ord(char) for char in chars]

#   chars = ['A', 'B', 'C']
#   unicode_values = char_to_unicode(chars)
#   print(f"Valores Unicode: {unicode_values}")

# ==================================================================================
# pow(): Retorna o valor de x**y (x elevado a y).
# # Programa para calcular a potência de números
# def calculate_power(base, exp):
#     return pow(base, exp)

# base = 2
# exp = 3
# result = calculate_power(base, exp)
# print(f"{base} elevado a {exp} é {result}")

# ==================================================================================
# print(): Imprime objetos na saída de texto.
# # Programa para imprimir várias mensagens
# def print_messages(messages):
#     for message in messages:
#         print(message)

# messages = ["Hello", "World", "Python"]
# print_messages(messages)

# ==================================================================================
# property(): Retorna um objeto de propriedade.
# # Programa para demonstrar o uso de propriedades
# class MyClass:
#     def __init__(self, value):
#         self._attribute = value

#     @property
#     def attribute(self):
#         return self._attribute

#     @attribute.setter
#     def attribute(self, value):
#         self._attribute = value

# obj = MyClass("initial value")
# print(f"Valor inicial: {obj.attribute}")
# obj.attribute = "new value"
# print(f"Novo valor: {obj.attribute}")

# ==================================================================================
# range(): Retorna uma sequência de números.
# # Programa para gerar uma lista de números usando range
# def generate_numbers(start, end, step):
#     return list(range(start, end, step))

# numbers = generate_numbers(0, 10, 2)
# print(f"Números gerados: {numbers}")

# ==================================================================================
# repr(): Retorna uma representação de string de um objeto.
#   # Programa para obter a representação string de um objeto
#   class MyClass:
#       def __init__(self, value):
#           self.value = value

#       def __repr__(self):
#           return f"MyClass(value={self.value})"

#   obj = MyClass(10)
#   print(f"Representação: {repr(obj)}")

# ==================================================================================
# reversed(): Retorna um iterador invertido.
#   # Programa para reverter uma lista
#   def reverse_list(items):
#       return list(reversed(items))

#   items = [1, 2, 3, 4]
#   reversed_items = reverse_list(items)
#   print(f"Lista invertida: {reversed_items}")

# ==================================================================================
# round(): Retorna o número arredondado para o dígito mais próximo.
# # Programa para arredondar números de ponto flutuante
# def round_numbers(numbers):
#     return [round(num) for num in numbers]

# numbers = [1.2, 2.5, 3.8]
# rounded_numbers = round_numbers(numbers)
# print(f"Números arredondados: {rounded_numbers}")

# ==================================================================================
# set(): Cria um novo conjunto.
#   # Programa para criar um conjunto a partir de uma lista
#   def create_set(items):
#       return set(items)

#   items = [1, 2, 2, 3, 3, 3]
#   unique_items = create_set(items)
#   print(f"Conjunto: {unique_items}")

# ==================================================================================
# setattr(): Define um atributo em um objeto.
# # Programa para definir um atributo de um objeto
# class MyClass:
#     pass

# obj = MyClass()
# setattr(obj, 'attribute', 'value')
# print(f"Valor do atributo: {obj.attribute}")

# ==================================================================================
# slice(): Retorna um objeto de slice.
# # Programa para fatiar uma lista usando um objeto slice
# def slice_list(items, start, end):
#     return items[slice(start, end)]

# items = [1, 2, 3, 4, 5]
# sliced_items = slice_list(items, 1, 4)
# print(f"Lista fatiada: {sliced_items}")

# ==================================================================================
# sorted(): Retorna uma lista ordenada a partir dos itens de qualquer iterável.
# # Programa para ordenar uma lista de números
# def sort_numbers(numbers):
#     return sorted(numbers)

# numbers = [5, 2, 9, 1, 5, 6]
# sorted_numbers = sort_numbers(numbers)
# print(f"Números ordenados: {sorted_numbers}")

# ==================================================================================
# staticmethod(): Transforma um método em um método estático.
#   # Programa para demonstrar o uso de métodos estáticos
#   class MyClass:
#       @staticmethod
#       def static_method():
#           return "I am a static method"

#   print(MyClass.static_method())

# ==================================================================================
# str(): Retorna uma representação de string de um objeto.
#   # Programa para converter vários tipos de dados para string
#   def convert_to_string(values):
#       return [str(value) for value in values]

#   values = [1, 2.5, True, None]
#   strings = convert_to_string(values)
#   print(f"Strings: {strings}")

# ==================================================================================
# sum(): Soma os itens de um iterável.
# # Programa para somar os números em uma lista
# def sum_numbers(numbers):
#     return sum(numbers)

# numbers = [1, 2, 3, 4, 5]
# total = sum_numbers(numbers)
# print(f"Soma total: {total}")

# ==================================================================================
# super(): Retorna um objeto proxy que delega chamadas de método para uma classe pai ou irmão.
# # Programa para demonstrar o uso de super() em herança
# class Parent:
#     def __init__(self):
#         self.value = "Parent"

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.value = "Child"

# child = Child()
# print(f"Valor: {child.value}")

# ==================================================================================
# tuple(): Cria uma tupla.
#   # Programa para criar uma tupla a partir de uma lista
#   def create_tuple(items):
#       return tuple(items)

#   items = [1, 2, 3]
#   tuple_items = create_tuple(items)
#   print(f"Tupla: {tuple_items}")

# ==================================================================================
# type(): Retorna o tipo de um objeto ou cria um novo tipo.
# # Programa para verificar o tipo de vários objetos
# def check_types(objects):
#     return [type(obj) for obj in objects]

# objects = [1, "hello", 3.5, (1, 2)]
# types = check_types(objects)
# print(f"Tipos: {types}")

# ==================================================================================
# vars(): Retorna o __dict__ (atributos) de um objeto.
#   # Programa para listar os atributos de um objeto
#   class MyClass:
#       def __init__(self, value):
#           self.attribute = value

#   obj = MyClass("some value")
#   print(f"Atributos de obj: {vars(obj)}")

# ==================================================================================
# zip(): Cria um iterador que agrega elementos de iteráveis fornecidos.
#   # Programa para combinar duas listas em uma lista de tuplas
#   def zip_lists(list1, list2):
#       return list(zip(list1, list2))

#   list1 = [1, 2, 3]
#   list2 = ['a', 'b', 'c']
#   zipped = zip_lists(list1, list2)
#   print(f"Listas combinadas: {zipped}")

# ==================================================================================
# __import__(): Função chamada pelo comando import.
# # Programa para importar dinamicamente um módulo usando __import__()
# def dynamic_import(module_name):
#     module = __import__(module_name)
#     return module

# # Importando o módulo math dinamicamente
# math_module = dynamic_import('math')
# print(f"Resultado de math.sqrt(16): {math_module.sqrt(16)}")

# # Importando o módulo datetime dinamicamente
# datetime_module = dynamic_import('datetime')
# print(f"Data e hora atuais: {datetime_module.datetime.now()}")

# ==================================================================================

# nha = input('fale seu nha ')
# print('me mama? {}',type(nha))
# print('no mames? {}', nha.isspace())
# print('mames? {}', nha.isnumeric())
# print('ma? {}', nha.isalpha())
# print('mes? {}', nha.isupper())
# print('me? {}', nha.islower())
# print('mama? {}', nha.istitle())

# nha = int(input('fale seu nha '))
# for i in range(1, 11):
# print('{} x {} = {}'.format(nha, i, nha*i))

# p = int(input('fale seu nha '))
# r = int(input('fale seu nha '))
# d = p +(10 - 1)*r
# for c in range(p,d,r):
#   print('{} '.format(c), end='-> ')
# print("cabou")

# mai = 0 
# men = 0
# for c in range(1, 6): 
#   nha = float(input('fale seu nha '))
#   if nha == 1:
#     mai = c
#     men = c
#   else:
#       if nha > mai:
#         mai = nha
#       if nha < men:
#         men = nha
# print('o maior nha é {} '.format(mai))
# print('o menor nha é {} '.format(men))
# sidade = 0
# mai= 0 
# cont =  0 
# for c in range(1, 4): 
#   print('------{}PESSOA------'.format(c))
#   idade = int(input('fale sua idade '))
#   nome = str(input('fale seu nome ')).strip()
#   gereno = str(input('fale seu genero M/F/NA ')).strip()
#   sidade =+ idade
#   if idade > mai and gereno in 'Mm'  :
#     mai = idade
#   if idade < 20 and gereno in 'Ff':
#     cont += 1
#   elif gereno in 'NAna':
#     print('{} {}'.format(nome,idade))
# sidade /= 4
# print("a media é {}".format(sidade)) 
# print("o homi mas velho é {}".format(mai))
# print("a quantidade de mulheres menores de 20 é {}".format(cont))

# v = []
# cont = 0 
# while True:
#   no = v.append(int(input('fale sua nha ')))
#   r = str(input('quer continuar S/N '))
#   if r in 'Nn':
#     break
# print('-=-'*21)
# print(f'vc falou {len(v)} valores')
# v.sort(reverse=True)
# print(f'seu numero são {v}' )
# if 5 in v:
#   cont += 1
#   print(f'vc tem {cont} numero 5 nos valores')
# else: 
#   print("vc n tem nem um 5 nos valores")
  
# num = list()
# par = list()
# impar = list() 
# while True:
#   num.append(int(input('fale sua nha ')))  
#   r = str(input('quer continuar S/N '))
#   if r in 'Nn':
#     break
# for i,v in enumerate(num): 
#   if v % 2 == 0:
#     par.append(v)
#   elif v % 2 == 1:
#       impar.append(v)
# print(f'os numeros pares são {par}')
# print(f'os numeros impares são {impar}')
# print(f'os numeros são {num}')

# m = [[0,0,0] , [0,0,0] , [0,0,0]]
# spar = mai = scol = 0
# for i in range(0,3): 
#   for j in range(0,3):
#     m[i][j] = int(input(f'mete bala {i}, {j}   '))
# for i in range(0,3):
#   for j in range(0,3):
#     print(f'[{m[i][j]}]', end='')
#     if m[i][j] % 2 == 0:
#       spar += m[i][j]
#   print()
# for i in range(0 ,3):
#   scol += m[i][2]
# print(f'a soma é {spar}')
# for j in range(0 ,3):
#   if j == 0:
#     mai = m[1][j]
#   elif m[1][j] > mai:
#     mai = m[1][j]
# print(f'o maior {mai} ')    