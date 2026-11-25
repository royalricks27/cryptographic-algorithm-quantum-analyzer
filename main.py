import parse_algorithm

def main():
    # parsed_algorithm = parse_algorithm(input.txt) #parse_algorithm must return the parsed algorithm
    # vulnerability_analysis, time_complexity_analysis, space_complexity_analysis = analyze_algorithm(parsed_algorithm) #analyze_algorithm must return all three objects
    parse_algorithm.convert_pseudocode_to_algorithm()

if __name__ == "__main__":
    main()