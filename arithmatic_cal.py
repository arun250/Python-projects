def arithmetic_arranger(problems):
    results = []
    for problem in problems:
        parts = problem.split()
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])


        str_num1 = str(num1)
        str_num2 = str(num2)
        width = max(len(str_num1), len(str_num2))+2
        

        top_line = f"{str_num1.rjust(width)}"
        bottom_line = f"{operator}{str_num2.rjust(width-2)}"
        operator_symbol = f"{operator.rjust(0)}"
        divider = "-" * (width)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2 
        else:
            raise ValueError("Unsupported error")
        
        result_line = f"{str(result).rjust(width)}"

        formatted_problems = f"{top_line}\n{bottom_line}\n{divider}\n{result_line}"
        results.append(formatted_problems)

    return "\n\n".join(results)



        

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')