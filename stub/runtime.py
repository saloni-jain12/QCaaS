import random
import time


class Runtime:
    def __init__(self) -> None:
        pass

    def execute(self, job_value: str, job_mode: str, start_time: str) -> int:
        if job_mode.lower() == 'verbatim':
            print(f"{start_time}: Executing {job_value} in verbatim mode")
            time.sleep(10)
            return random.randrange(0,10)
        elif job_mode.lower() == 'simulation':
            print(f"{start_time}: Executing {job_value} in simulation mode")
            time.sleep(5)
            return random.randrange(0, 10)
        else:
            return random.randrange(1, 10)