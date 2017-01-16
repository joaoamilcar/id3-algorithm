import math
from src.node import Node


class ID3:
    dataset = []
    newdataset = []
    attributes = []
    # boolean type class (eg. 0s e 1s)
    class1Occurrence = 0
    class2Occurrence = 0
    totalOccurrence = 0

    def __init__(self, dataset, attributes):
        self.dataset = dataset
        self.attributes = attributes
        self.newdataset = dataset[:]

    def run(self, node):
        column = self.attributes.index(node.attribute)
        cases = set()

        for register in self.dataset:
            cases.add(register[column])

        totalEntropy = self.get_total_entropy(node.subdataset)
        self.reset_class_occurencies()
        entropy = totalEntropy

        for c in cases:
            partialEntropy = self.get_partial_entropy(node.subdataset, c)
            entropy = entropy - ((self.totalOccurrence / len(node.subdataset)) * partialEntropy)
            self.reset_class_occurencies()

        return entropy

    def get_root(self):
        biggerIg = 0
        root = None  # bigger IG

        for position in range(1, len(self.attributes) - 1):
            ig = 0

            ig = self.get_ig(self.dataset, self.attributes[position])
            print(self.attributes[position], ig)

            if ig > biggerIg:
                biggerIg = ig
                root = self.attributes[position]
        print("")

        return root

    def get_ig(self, newdataset, attribute):
        column = self.attributes.index(attribute)
        cases = set()

        for register in newdataset:
            cases.add(register[column])

        totalEntropy = self.get_total_entropy(newdataset)
        self.reset_class_occurencies()
        entropy = totalEntropy

        for c in cases:
            partialEntropy = self.get_partial_entropy(newdataset, c)
            entropy = entropy - ((self.totalOccurrence / len(newdataset)) * partialEntropy)
            self.reset_class_occurencies()



        return entropy

    def get_total_entropy(self, newdataset): # uma medida para o nivel de incerteza sobre um evento
        firstRegisterOccurence = None

        for register in newdataset:
            if firstRegisterOccurence == None:
                firstRegisterOccurence = register

            if register[len(register) - 1] == firstRegisterOccurence[len(firstRegisterOccurence) - 1]:
                self.class1Occurrence += 1
            else:
                self.class2Occurrence += 1

        self.totalOccurrence = self.class1Occurrence + self.class2Occurrence
        portion1 = 0
        portion2 = 0

        # log(x) is defined only for x > 0
        if self.class1Occurrence > 0:
            portion1 = - (self.class1Occurrence / self.totalOccurrence) * math.log((self.class1Occurrence / self.totalOccurrence), 2)

        if self.class2Occurrence > 0:
            portion2 = - (self.class2Occurrence / self.totalOccurrence) * math.log((self.class2Occurrence / self.totalOccurrence), 2)

        entropy = portion1 + portion2

        return entropy

    def get_partial_entropy(self, newdataset, case):
        firstRegisterOccurence = None

        column = self.find_attribute_column_by_case(case)

        for register in newdataset:
            if register[column] == case:
                if firstRegisterOccurence == None:
                    firstRegisterOccurence = register

                if register[len(register) - 1] == firstRegisterOccurence[len(firstRegisterOccurence) - 1]:
                    self.class1Occurrence += 1
                else:
                    self.class2Occurrence += 1

        self.totalOccurrence = self.class1Occurrence + self.class2Occurrence
        portion1 = 0
        portion2 = 0

        # log(x) is defined only for x > 0
        if self.class1Occurrence > 0:
            portion1 = - (self.class1Occurrence / self.totalOccurrence) * math.log(
                (self.class1Occurrence / self.totalOccurrence), 2)

        if self.class2Occurrence > 0:
            portion2 = - (self.class2Occurrence / self.totalOccurrence) * math.log(
                (self.class2Occurrence / self.totalOccurrence), 2)

        entropy = portion1 + portion2

        return entropy

    def find_attribute_column_by_case(self, case):
        for register in self.dataset:
            for position in range (1, len(register) - 1):
                if register[position] == case:
                    return position

    def reset_class_occurencies(self):
        self.class1Occurrence = 0
        self.class2Occurrence = 0
        self.totalOccurrence = 0

    def isCaseInAttribute(self, case, attribute):
        pass