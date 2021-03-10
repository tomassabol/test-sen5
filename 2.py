def main():
    with open("cisla.txt", 'r') as file:
        numbers = file.read().split(" ")
        print(numbers)

    numbers_int = []
    for number in numbers:
        numbers_int.append(int(number))

    with open("riesenie.txt", 'w') as riesenie:
        for number in reversed(numbers_int):
            riesenie.write(str(number) + " ")

        riesenie.write("\n")

        numbers_int = sorted(numbers_int)

        for number in numbers_int:
            riesenie.write(str(number) + " ")

        riesenie.write("\n")

        median = numbers_int[len(numbers_int)//2]

        riesenie.write(str(median))


main()
