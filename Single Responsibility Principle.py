class ECommerceApp:
    def __init__(self):
        self.users = dict()
        self.catalog = dict()
        print("\n\nWelcome to EcommerceApp!\n\n")

    def add_user(self, id, user):
        self.users[id] = user

    def remove_user(self, id):
        if id in self.users:
            del self.users[id]

    def add_item_to_catalog(self, id, item):
        self.catalog[id] = item

    def remove_item_from_catalog(self, id):
        if id in self.catalog:
            del self.catalog[id]

    def send_notification(self, message):
        # Code for sending the notification to the user
        print(message,end="\n\n")

    def place_order(self, item):
        if item in self.catalog:
            # Code for placing an order
            self.send_notification(f"Your order has been placed for: {self.catalog[item]}")
        else:
            self.send_notification(f"Item with ID {item} not available.")
        
app = ECommerceApp()
app.add_item_to_catalog(1, "Book - Zero to One")
app.add_item_to_catalog(2, "Whey protein")
app.place_order(1)

class UserManager:
    def __init__(self):
        self.users = dict()
    
    def add_user(self,name,id):
        self.users[id] = name
    
    def remove_user(self, id):
        if id in self.users:
            del self.users[id]
            return True
        return False


class Catalog:
    def __init__(self):
        self.items = dict()

    def add_item(self, id, item):
        self.items[id] = item

    def remove_item(self, id):
        if id not in self.items:
            raise KeyError()
        del self.items[id]


class NotificationService:
    #Here we'll be sending various types of notifications(email, text, push) to users
    @staticmethod
    def send_notification(message):
        print(message)


class OrderProcessor:
    def __init__(self, catalog):
        self.catalog = catalog
        print("\n\nWelcome to OrderProcessor Service!\n\n")

    def place_order(self, item):
        if item in self.catalog.items:
            # Code for placing an order
            NotificationService.send_notification(f"Your order has been placed for: {self.catalog.items[item]}")
        else:
            NotificationService.send_notification("Item not available.")

catalog = Catalog()
catalog.add_item(1, "Book - Lean Startup")
catalog.add_item(2, "Red Bell Peppers")

order_processor = OrderProcessor(catalog)
order_processor.place_order(1)