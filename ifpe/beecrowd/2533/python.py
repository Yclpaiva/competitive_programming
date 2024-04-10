while True:
    
    try:
        subjects_amount = 0
        subjects_amount = int(input())
        array = []
        i = 0
        valor_n = 0
        valor_total = 0

        while i < subjects_amount:

            inputvalor = input()
            inputvalor = inputvalor.split(" ")
            valor_n += float(inputvalor[0]) * float(inputvalor[1])
            valor_total += float(inputvalor[1])
            i += 1
        
        valorgeral = (((valor_n)/(valor_total*100)))
        print(f"{valorgeral:.4f}")

    except EOFError:
        break
