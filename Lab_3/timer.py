import time


class cm_timer():
    def init(self):
        self.start = 0.0
        self.end = 0.0

    def enter(self):
        self.start = time.time()
        return self

    def exit(self, exc_type, exc_value, exc_traceback):
        self.end = time.time()
        print('Время выполнения: {} секунд.'.format(self.end - self.start))


with cm_timer():
    time.sleep(5.5)