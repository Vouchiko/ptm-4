from datetime import datetime, timedelta

class Client:
    def __init__(self, first_name, last_name, check_in_date, check_out_date, room_class):
        self.first_name = first_name
        self.last_name = last_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_class = room_class

class Hotel:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, first_name, last_name):
        self.clients = [client for client in self.clients if client.first_name != first_name or client.last_name != last_name]

    def client_exists(self, first_name, last_name):
        return any(client.first_name == first_name and client.last_name == last_name for client in self.clients)

    def change_name(self, old_first_name, old_last_name, new_first_name, new_last_name):
        for client in self.clients:
            if client.first_name == old_first_name and client.last_name == old_last_name:
                client.first_name = new_first_name
                client.last_name = new_last_name

    def extend_stay(self, first_name, last_name, extra_days):
        for client in self.clients:
            if client.first_name == first_name and client.last_name == last_name:
                client.check_out_date += timedelta(days=extra_days)

    def change_room_class(self, first_name, last_name, new_room_class):
        for client in self.clients:
            if client.first_name == first_name and client.last_name == last_name:
                client.room_class = new_room_class


if __name__ == "__main__":
    try:
        
        hotel = Hotel()

        client1 = Client("Иван", "Иванов", datetime(2023, 12, 1), datetime(2023, 12, 10), "Стандарт")
        client2 = Client("Петр", "Петров", datetime(2023, 12, 5), datetime(2023, 12, 15), "Люкс")

        hotel.add_client(client1)
        hotel.add_client(client2)

        hotel.change_name("Иван", "Иванов", "Алексей", "Иванов")

        hotel.extend_stay("Алексей", "Иванов", 5)

        hotel.change_room_class("Петр", "Петров", "Президентский")

        print(hotel.client_exists("Алексей", "Иванов"))

        hotel.remove_client("Петр", "Петров")

    except Exception as e:
        print(f"Произошла ошибка: {e}")