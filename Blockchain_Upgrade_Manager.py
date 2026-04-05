class UpgradeManager:
    def __init__(self):
        self.current_version = "v1.0.0"

    def upgrade(self, new_version):
        if new_version > self.current_version:
            self.current_version = new_version
            return True
        return False

if __name__ == "__main__":
    um = UpgradeManager()
    print("升级结果:", um.upgrade("v1.1.0"))
