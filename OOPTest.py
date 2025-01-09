class Engine:
    def start_Engine(self):
        print("Engine Stated")

    @staticmethod
    def stop_Engine():
        print("Engine Stopped")

# Create an object
obj = Engine()
obj.start_Engine()
obj.stop_Engine()
print("***********")
obj.start_Engine()
obj.stop_Engine()