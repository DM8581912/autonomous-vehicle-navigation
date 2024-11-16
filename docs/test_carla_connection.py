import sys
sys.path.append("C:\\Users\\adamk\\OneDrive - University Of Houston\\COSC 4368\\CARLA_0.9.15\\WindowsNoEditor\\PythonAPI\\carla\\dist\\carla-0.9.15-py3.7-win-amd64.egg")
import carla

def test_carla():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        print("CARLA API successfully connected!")
    except Exception as e:
        print(f"CARLA connection failed: {e}")

if __name__ == "__main__":
    test_carla()
