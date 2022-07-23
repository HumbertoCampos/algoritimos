class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, element):
        #insere um element na fila
        node = Node(element)
        if self.last is None:
            self.last = node

        else:
            self.last.next = node
            self.last.previous = self.last.next
            self.last = node

        if self.first is None:
            self.first = node

        self.size = self.size + 1

    def pop(self):
        #remove o element do começo
        if self.size > 0:
            element = self.first.data
            self.first = self.first.next
            self.size = self.size - 1
            return element

    def pop_l(self):
        #remove o element do final
        if self.size > 0:
            element = self.last.data
            self.last = self.last.previous
            self.last = self.first.next
            self.size = self.size - 1
            return element


if __name__ == '__main__':
    fila_one = Queue()
    fila_two = Queue()
    box1 = box2 = real_size = 0
    transfer = None

    comando = input()

    while comando != 'FIM':

        comando = comando.split(' ')

        if comando[0] == 'ENTROU:':
            if comando[2] == '1':
                fila_one.push(comando)
                print(f'{comando[1]} entrou na fila 1')

            elif comando[2] == '2':
                fila_two.push(comando)
                print(f'{comando[1]} entrou na fila 2')

        elif comando[0] == 'PROXIMO:':
            if comando[1] == '1':
                if fila_one.size == 0:
                    real_size = fila_two.size

                    while fila_two.size != (real_size // 2):
                        transfer = fila_two.pop_l()
                        fila_one.push(transfer)

                    aux = fila_one.pop()

                    print(f'{aux[1]} foi chamado para o caixa 1')
                    box1 += float(aux[3])

                elif fila_one.size > 0:
                    aux = fila_one.pop()

                    print(f'{aux[1]} foi chamado para o caixa 1')
                    box1 += float(aux[3])

            elif comando[1] == '2':
                if fila_two.size == 0:
                    real_size = fila_one.size

                    while fila_one.size != (real_size // 2):
                        transfer = fila_one.pop_l()
                        fila_two.push(transfer)


                    aux = fila_two.pop()

                    print(f'{aux[1]} foi chamado para o caixa 2')
                    box2 += float(aux[3])

                elif fila_two.size > 0:
                    aux = fila_two.pop()

                    print(f'{aux[1]} foi chamado para o caixa 2')
                    box2 += float(aux[3])


        comando = input()

    print(f'Caixa 1: R$ {box1:.2f}, Caixa 2: R$ {box2:.2f}')
