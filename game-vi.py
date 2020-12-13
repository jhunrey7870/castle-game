import random
exitChoice = "jhunrey is gay lmao"
while exitChoice != " ":
print("Bạm bị kẹt trong 1 tòa lâu đài tối thui mà chính bạn cũng ko biết tại sao bạn lại ở đó :v")
print("Ở đó có 4 cánh cửa mà bạn có thể đi qua")
playerChoice = input("Chọn 1,2,3 hoặc 4:")
if playerChoice == "1":
    print("nah bạn đã chết bởi vì ko có lý do =))")
    print("Bạn đã thua cuộc!")
elif playerChoice == "2": 
    print("Cánh cửa từ từ mở ra, một con chó yêu tinh nhảy ra và đập bạn =)")
    print("Bạn đã thua cuộc!")
elif playerChoice == "3":
    print("Bạn tiến vào căn phòng và thấy một con rồng nằm ngủ")
    print("Bạn có thể chọn:")
    print("1. lấy cái s20 ultra của nó xD")
    print("2. cẩn thận pay qua người nó")
    dragonChoice = input("Lựa chọn sống của bạn:")
    if dragonChoice == "1":
        print("Nah con rồng đã thấy buds plus của nó bị ngắt kết nối và ăn bạn")
        print("Bạn đã thua cuộc!")
    elif dragonChoice == "2":
        print("Bạn đã pay qua ass con rồng thành công!")
        print("Bạn đã thắng, xin chúc mừng OwO")
    else:
        print("bruh chọn 1 trong 2 đi")
elif playerChoice == "4":
    print("Bạn vào và có 1 con phù thủy pay tứ lung tung, nó đang chơi lotto, bạn hãy đoán 1 số từ 1 đến 5 và xem có đúng ko")
    number = int(input("Choose your number:"))
    if number == random.randint(1,5):
        print("Con phù thủy thấy nhụk nhã nên đã uống H2SO4 và chết !")
        print("Bạn đã thắng, xin chúc mừng OwO")
    else:
        print("Bạn đã đoán sai và phải làm đầy tớ cho nó đến cuối đời =))!")
        print("Bạn đã thua cuộc!")
else:
    print("bạn đã k chọn 1 hay 2 hay 3 hay 4 =/")
exitChoice = input("Chạy lại game để khám phá lại!")
