class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacoes(self):
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}')

class LivroDigital(Livro):
    def __init__(self, titulo, autor, paginas, formato):
        super().__init__(titulo, autor, paginas)
        self.formato = formato

    def informacoes(self):
        super().informacoes()
        print(f'Formato: {self.formato}')

livro1 = LivroDigital('Frankenstein', 'Mary Shelley', 240, 'Digital')
livro1.informacoes()
