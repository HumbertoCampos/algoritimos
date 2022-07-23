class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0
        self.maxValue = 0

    def insert(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.tail = newNode
            self.maxValue = value
        else:
            newNode.previous = self.tail
            self.tail = newNode
            if value > self.maxValue:
                self.maxValue = value

        self.size += 1

    def getLastValue(self):
        return self.tail.value

    def getConsDays(self):
        if self.maxValue == self.tail.value:
            return self.size
        node = self.tail
        actualValue = node.value
        consDays = 0
        
        for i in range(self.size):
            if node.value <= actualValue:
                consDays += 1
                node = node.previous
            else:
                return consDays
        return consDays


if __name__ == '__main__':
    number = int(input())
    lista = LinkedList()

    for i in range(number):
        command = str(input(""))
        command = command.split(" ")

        if command[0] == "ATUALIZA":
            lista.insert(int(command[1]))

        elif command[0] == "INFO":
            lastValue = lista.getLastValue()
            consecutiveDays = lista.getConsDays()

            print(f'O ULTIMO VALOR FOI {lastValue} E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS {consecutiveDays} DIAS')
