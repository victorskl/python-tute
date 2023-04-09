from structure.di_registry_subscriber import hello_world

def write_to_log():
    print("Waking up!")


if __name__ == '__main__':
    hello_world.subscribers.append(write_to_log)
    hello_world.hello_world()
