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
        if(self.size == 0):
            self.tail = newNode
            self.maxValue = value
        else:
            newNode.previous = self.tail
            self.tail = newNode
            if (value > self.maxValue):
                self.maxValue = value

        self.size += 1

    def getLastValue(self):
        return self.tail.value

    def getConsDays(self):
        if (self.maxValue == self.tail.value):
            return self.size
        node = self.tail
        actualValue = node.value
        consDays = 0
        count = 0
        while (count < self.size):
            if(node.value <= actualValue):
                consDays += 1
                node = node.previous
                count += 1
            else:
                return consDays
        return consDays


if __name__ == '__main__':
    number = int(input())
    count = 0
    lista = LinkedList()

    while(count < number):
        command = str(input(""))
        command = command.split(" ")

        if(command[0] == "ATUALIZA"):
            lista.insert(int(command[1]))

        elif(command[0] == "INFO"):
            lastValue = lista.getLastValue()
            consecutiveDays = lista.getConsDays()

            print("O ULTIMO VALOR FOI {value} E HOJE E UM BOM DIA PARA VENDER ACOES DOS ULTIMOS {day} DIAS".format(
                value=lastValue, day=consecutiveDays))

        count += 1
