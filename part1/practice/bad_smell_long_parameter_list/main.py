class Unit:
    def __init__(self, field, x: int, y: int, direction, is_fly: bool, crawl: bool, speed: int = 1):
        self.field = field
        self.x = x
        self.y = y
        self.direction = direction
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.is_fly:
            return self.speed * 1.2
        elif self.is_fly:
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
