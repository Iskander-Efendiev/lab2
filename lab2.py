def int_fract(dec_num, base):
    int_part = ''
    fract_part = ''
    flag = False
    for i in dec_num:
        if i == ",":
            flag = True
        if flag == False and i != ",":
            int_part += i
        elif flag and i != ',':
            fract_part += i
    if flag:
        return f"{int_conv(int_part, base) + fract_conv(fract_part)}"
    else:
        return f"{int_conv(int_part, base)}"
    
def is_sixty_num(num, base):
    if base != 10:
        if num == 10:
            return "A"
        elif num == 11:
            return "B"
        elif num == 12:
            return "C"
        elif num == 13:
            return "D"
        elif num == 14:
            return "E"
        elif num == 15:
            return "F"
        else:
            return str(num)
    else:
        if num == "A":
            return 10
        if num == "B":
            return 11
        if num == "C":
            return 12
        if num == "D":
            return 13
        if num == "E":
            return 14
        if num == "F":
            return 15
        else:
            return int(num)
        
        
def int_conv(int_part, base):
    try:
        if int(int_part) == 0:
            return "0"
    except:
        pass

    # if base2 == 2:
    #     result_arr = [int_part[i:i + 4] for i in range[0, len(int_part), 4]]

    #     dict_16ss = {
    #         "0000" : "0",
    #         "0001" : "1",
    #         "0010" : "2",
    #         "0011" : "3",
    #         "0100" : "4",
    #         "0101" : "5",
    #         "0110" : "6",
    #         "0111" : "7",
    #         "1000" : "8",
    #         "1001" : "9",
    #         "1010" : "A",
    #         "1011" : "B",
    #         "1100" : "C",
    #         "1101" : "D",
    #         "1110" : "E",
    #         "1111" : "F",
    #     }

    #     temp_result = ""
    #     result = ""
    #     for i in result_arr:
    #         temp_result += dict_16ss[i]

    #     for i in range(len(temp_result)):
    #         if temp_result[i] != "0":
    #             result = temp_result[i:]
    #             break
        
    if base != 10:
        try:
            quotient = int(int_part)
        except ValueError:
            quotient = is_sixty_num(int_part, 10)
        remains = ""

        while quotient > (base - 1):
            remains += is_sixty_num(quotient % base, base)
            print(quotient, base, remains, quotient, sep='/')
            print(f"{quotient} % {base} = {quotient % base} / {remains}")
            remains //= base
        else:
            remains += is_sixty_num(int(quotient), base)
        result = "".join(reversed(remains))

        if base == 2:
            if int_part[0] != ".":
                return result.zfill(16)
            else:
                wrap_dict_2ss = {
                    "0" : "1",
                    "1" : "0"
                }
                temp_result = result.zfill(17)[:-1]
                result = ""
                for i in temp_result:
                    result += wrap_dict_2ss[i]
                return result
        elif base == 16:
            return result
    else:
        index = len(int_part) - 1
        result = 0
        for i in int_part:
            i = is_sixty_num(i, base)
            result += i * (base ** index)
            index -= 1
        return result
    

if __name__ == "__main__":
    dec_num = str(input("Введите число: "))
    base2 = int(input("Введите основание, в которой находится число: "))
    base = int(input("Введите в какую основанию нужно привести число: "))
    print(int_fract(dec_num, base))

# def is_sixty_num(num):
#     if num == 10:
#         return "A"
#     elif num == 11:
#         return "B"
#     elif num == 12:
#         return "C"
#     elif num == 13:
#         return "D"
#     elif num == 14:
#         return "E"
#     elif num == 15:
#         return "F"
#     else:
#         return str(num)
    
# def is_sixty_num_two(num):
#     if num == 10:
#         return "A"
#     elif num == 11:
#         return "B"
#     elif num == 12:
#         return "C"
#     elif num == 13:
#         return "D"
#     elif num == 14:
#         return "E"
#     elif num == 15:
#         return "F"
#     else:
#         return str(num)
    
# def int_conv_twoss(int_part):
#     if int(int_part) == 0:
#         return "0"
#     quotient = int(int_part)
#     remains = ""

#     while quotient > (2 - 1):
#         remains += str(quotient % 2)
#         quotient //= 2
#     else:
#         remains += str(quotient)
#     result = "".join(reversed(remains))
#     if int_part[0] != ".":
#         return result.zfill(16)
#     else:
#         wrap_dict_2ss = {
#             "0" : "1",
#             "1" : "0"
#         }
#         temp_result = result.zfill(17)[:-1]
#         result = ""
#         for i in temp_result:
#             result += wrap_dict_2ss[i]
#         return result

# def int_conv_tens(int_part):
#     if int_part == 0:
#         return "0"
#     index = len(int_part) - 1
#     result = 0
#     for i in int_part:
#         result += int(i) * (1 ** index)
#         index -= 1
#         return str(result)
    
# def int_conv_sixtenss(int_part):
#     result_arr = [int_part[i:i + 4] for i in range(0, len(int_part), 4)]
#     dict_16ss = {
#         "0000" : "0",
#         "0001" : "1",
#         "0010" : "2",
#         "0011" : "3",
#         "0100" : "4",
#         "0101" : "5",
#         "0110" : "6",
#         "0111" : "7",
#         "1000" : "8",
#         "0001" : "1",
#         "0010" : "2",
#         "0011" : "3",
#         "0100" : "4",
#         "0101" : "5",
#         "0110" : "6",
#         "0111" : "7",
#     }
#     temp_result = ''
#     result = ''
#     for i in result_arr:
#         temp_result += dict_16ss[i]

#     for i in  range(len(temp_result)):
#         if temp_result[i] != "0" :
#             result = temp_result[i:]
#             break

#     return result