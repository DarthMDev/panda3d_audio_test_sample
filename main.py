import threading
from direct.showbase.ShowBase import ShowBase
from panda3d.core import AudioSound

class AudioTestApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load a mono sound effect
        self.sound = self.loader.loadSfx("sfx/whistle.mp3")
        self.sound.setVolume(1.0)
        self.sound.setLoop(False)
        # Print which audio driver is in use
        print("Audio Driver:", base.sfxManagerList[0].getType().getName())

        # Start a separate thread to wait for user input
        input_thread = threading.Thread(target=self.wait_for_input, daemon=True)
        input_thread.start()

    def wait_for_input(self):
        input("Press ENTER to play the sound...\n")
        self.play_sound()

    def play_sound(self):
        print("Playing mono sound...")
        self.sound.play()

app = AudioTestApp()
app.run()

