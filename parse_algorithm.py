import numpy as np

def convert_pseudocode_to_algorithm():
    is_loop = False
    vars = dict()
    algorithm = list()
    conditions= dict()
    loop = list()
    with open("input.txt") as input:
        for line in input:
            condition = "" if not is_loop else condition
            tokens = line.strip().split(" ")
            #print(tokens), used for testing
            match tokens[0]:
                case "//":
                    is_loop = False
                    continue
                case "WHILE" | "FOR":
                    is_loop = True
                    for token in tokens[1:]:
                        condition += token
                    conditions[condition] = list()
                    #evaluate_loop_line(tokens[1:])
            if(is_loop):
                conditions[condition].append(line.strip())
            else:
                algorithm.append(line.strip())
    print(conditions)
    print(algorithm)

#def evaluate_non_loop_line(tokens: list):
    # match tokens[0]:
    #     case "//":
    #         if isWhile:
    #             break
    #         continue
    #     case "WHILE":
    #         if isWhile:
    #             break
    #         isWhile = True
    #         condition = ""
    #         for token in tokens[1:]:
    #             condition += token
    #         conditions[condition] = list()

#def evaluate_loop_line(tokens: list):
    #return

def convert_operation_to_list(input: tuple, operation, output) -> list:
    #NOTE: should output a list, since inputs, outputs, and operations (probably) aren't homogenous
    output = list()
    return

def convert_operations_to_oracle(*args: list) -> np.ndarray:
    oracle = np.empty(len(args), datatype=list)

def algorithm_to_dict() -> dict:
    return dict()