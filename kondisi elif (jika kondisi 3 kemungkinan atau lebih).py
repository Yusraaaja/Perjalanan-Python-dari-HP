nama = input('Siapa namamu? : ')
umur = int(input('Berapa umurmu? : '))
if umur < 20 :
    print(f'karna umurmu {umur}, maka kamu masuk tim magang.')
elif umur < 40 :
    print(f'karna umurmu {umur}, maka kamu masuk tim lapangan.')
else :
    print(f'karna umurmu {umur}, maka kamu masuk tim administrasi.')