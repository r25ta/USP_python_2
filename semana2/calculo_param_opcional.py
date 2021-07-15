def calculo_param_opcional(x, y=10, z=5):
    return x + y * z

def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s


def main():
    print(calculo_param_opcional(7,2))
    print(calculo_param_opcional(1,2,3))
    print(calculo_param_opcional(7))
    
    
    print(horario_em_segundos(1,2,3))

    print(horario_em_segundos(3,0,50))
main()