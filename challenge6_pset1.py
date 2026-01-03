def tower_of_hanoi(num,first,middle,last):
    assert num > 0
    if num == 1:
        print(f"Move disk {num} from {first} to {last}")
        return
    tower_of_hanoi(num-1,first,last,middle)
    print(f"Move disk {num} from {first} to {last}")
    tower_of_hanoi(num-1,middle,first,last)

tower_of_hanoi(3,'A','B','C')