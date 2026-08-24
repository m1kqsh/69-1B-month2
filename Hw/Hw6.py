class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return (
            f"{self.live()} "
            f"{self.superpower()} "
            f"{self.earn()}"
        )


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return (
            f"{self.live()} "
            f"{self.viral()} "
            f"{self.superpower()}"
        )


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return (
            f"{self.live()} "
            f"{self.earn()} "
            f"{self.viral()}"
        )


glow_streamer = GlowStreamer()
viral_cyborg = ViralCyborg()
donate_mage = DonateMage()


print("GlowStreamer MRO:")
print(GlowStreamer.mro())
print()

print("ViralCyborg MRO:")
print(ViralCyborg.mro())
print()

print("DonateMage MRO:")
print(DonateMage.mro())
print()


print("GlowStreamer live():")
print(glow_streamer.live())
print("Сработал метод Streamer, потому что Streamer стоит первым в MRO.")
print()

print("ViralCyborg live():")
print(viral_cyborg.live())
print("Сработал метод TikToker, потому что TikToker стоит первым в MRO.")
print()

print("DonateMage live():")
print(donate_mage.live())
print("Сработал метод Streamer, потому что Streamer стоит первым в MRO.")
print()


print("GlowStreamer ultimate_content():")
print(glow_streamer.ultimate_content())
print()

print("ViralCyborg ultimate_content():")
print(viral_cyborg.ultimate_content())
print()

print("DonateMage ultimate_content():")
print(donate_mage.ultimate_content())
