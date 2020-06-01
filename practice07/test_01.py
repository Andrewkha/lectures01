#  Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник.
#  Пианино необходимо доставить в институт, холодильник в общежитие. В каждое из этих мест ведет отдельная дорога,
#  начинающаяся от перекрестка, на котором Вы стоите, других дорог в мире нет. Известно, что по дороге в институт есть
#  мост, на котором действует ограничение максимальной допустимой массы автомобиля с грузом, а по дороге в общежитие
#  есть туннель с ограничением высоты. Требуется определить, возможно ли доставить грузы или нет (разумеется,
#  сгружать их, где попало, Вам запрещено).
# Формат входных данных
#
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке, в следующем порядке: вес
# грузовика без груза, высота платформы кузова (на которой стоят грузы), вес пианино, высота пианино, вес холодильника,
# высота холодильника, максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле
#
# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика, т.е. высоту кабины можно в расчет
# не принимать.
# Формат выходных данных
#
# Вывести YES если доставка возможна и NO в противном случае.

truck_weight = int(input())
platform_height = int(input())
piano_weight = int(input())
piano_height = int(input())
refr_weight = int(input())
refr_height = int(input())

max_bridge_weight = int(input())
max_tunnel_height = int(input())

dimensions = [truck_weight + piano_weight + refr_weight, platform_height + max(piano_height, refr_height)]


def try_deliver_piano(dims):
    if dims[0] > max_bridge_weight:
        return False
    return [dims[0] - piano_weight, platform_height + refr_height]


def try_deliver_refr(dims):
    if dims[1] > max_tunnel_height:
        return False
    return [dims[0] - refr_weight, platform_height + piano_height]


if try_deliver_piano(dimensions):
    dimensions = try_deliver_piano(dimensions)
    if try_deliver_refr(dimensions):
        print("YES")
    else:
        print('NO')

elif try_deliver_refr(dimensions):
    dimensions = try_deliver_refr(dimensions)
    if try_deliver_piano(dimensions):
        print("YES")
    else:
        print('NO')

else:
    print("NO")


