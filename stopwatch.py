import datetime
import keyboard


def chronometer_format(seconds):
    hours, remainder = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def chronometer():
    start_chronometer = datetime.datetime.now()

    while True:

        current_chronometer = datetime.datetime.now()
        elapsed_time = int((current_chronometer - start_chronometer).total_seconds())
        print(f"Pass Time: {chronometer_format(elapsed_time)}", end='\r')

        if keyboard.is_pressed("s"):
            break

    print("\nStopwatch is stopped.")
    print("r: Reset, c: Continue, q: Quit")

    while True:

        user_choice = input("Enter your choice (r/c/q): ").lower()

        if user_choice == "r":
            start_chronometer = datetime.datetime.now()  

            while True:

                current_chronometer = datetime.datetime.now()
                elapsed_time = int((current_chronometer - start_chronometer).total_seconds())
                print(f"Pass Time: {chronometer_format(elapsed_time)}", end='\r')

                if keyboard.is_pressed("s"):
                    break

            print("\nStopwatch is stopped.")
            print("r: Reset, c: Continue, q: Quit")

        elif user_choice == "c":

            start_chronometer = datetime.datetime.now() - datetime.timedelta(seconds=elapsed_time)
            while True:

                current_chronometer = datetime.datetime.now()
                elapsed_time = int((current_chronometer - start_chronometer).total_seconds())
                print(f"Pass Time: {chronometer_format(elapsed_time)}", end='\r')

                if keyboard.is_pressed("s"):
                    break

            print("\nStopwatch is stopped.")
            print("r: Reset, c: Continue, q: Quit")

        elif user_choice == "q":
            break


chronometer()
