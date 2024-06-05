def main():
    try:
        qntRepeticoes = int(input())
    except ValueError as err:
        print(err)
        return

    for _ in range(qntRepeticoes):
        input_str = input()
        list_of_strings = input_str.split()

        palavra1, palavra2 = list_of_strings[0], list_of_strings[1]
        try:
            num = int(palavra1)
        except ValueError as err:
            print(err)
            continue

        result, acrescimo = 0, 0

        if num > 45:
            if num > 45 and palavra2 == "2T":
                result = ((num // 45)*45) + 45
                acrescimo = (num + 45) - 90
            else:
                result = 45
                acrescimo = num - 45
        else:
            if palavra2 == "2T":
                result = num + 45
            else:
                result = num

        if acrescimo > 0:
            print(f"{result}+{acrescimo}")
        else:
            print(result)

if __name__ == "__main__":
    main()

