import random

class PrivacyMixer:
    def mix(self, inputs):
        random.shuffle(inputs)
        return inputs

if __name__ == "__main__":
    mixer = PrivacyMixer()
    print(mixer.mix([10,20,30]))
