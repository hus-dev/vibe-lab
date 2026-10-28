import random


def generate_secret_number(low=1, high=100):
    """1부터 100 사이의 임의의 정수 생성"""
    return random.randint(low, high)


def get_user_guess():
    """사용자로부터 유효한 정수 입력 받기 (숫자가 아니면 재입력 요청)"""
    while True:
        user_input = input("1부터 100 사이의 숫자를 입력하세요: ")
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")


def play_game():
    """숫자 맞히기 게임 메인 로직"""
    secret_number = generate_secret_number(1, 100)
    attempts = 0

    print("=== 1부터 100 사이 숫자 맞히기 게임 ===")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("더 큰 수")
        elif guess > secret_number:
            print("더 작은 수")
        else:
            print(f"정답입니다! 시도 횟수: {attempts}회")
            break


def main():
    play_game()


if __name__ == "__main__":
    main()
