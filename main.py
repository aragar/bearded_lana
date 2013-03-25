class Runner:
    def __init__(self, env):
        self.env = env

    def parse(self, command):
        action, subject = command.split(' ')
        return getattr(
            self.env[subject],
            action,
            lambda: "You can't {} the {}".format(
                action, subject)
        )

    def main(self):
        print("Hello, you're in The Room")
        while True:
            command = input('> ')
            print(self.parse(command)())


class Door:
    color = 'black'
    material = 'wood'
    is_locked = False
    is_opened = False

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
            return "The Door is unlocked, now"
        else:
            return "The Door is already unlocked"

    def lock(self):
        if self.is_locked:
            return "The Door is already locked"
        else:
            self.is_locked = True
            return "The Door is locked, now"

if __name__ == '__main__':
    Runner({'door': Door()}).main()
