def rase_to_power(base_num,power_num ):
    result =1
    for inder in range(power_num):
        result = result * base_num
        result = result * base_num
        return result

    print(rase_to_power(3,4))