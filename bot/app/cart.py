class Cart:
    def __init__(self):
        """Инициализация корзины пользователя."""
        self.user_carts = {}

    def _validate_user_id(self, user_id: int):
        """Валидация идентификатора пользователя."""
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("Идентификатор пользователя должен быть положительным целым числом.")

    def _validate_product(self, product_name: str, product_price: int = None):
        """Валидация названия и цены товара."""
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("Название товара должно быть непустой строкой.")
        if product_price is not None:
            if not isinstance(product_price, int) or product_price < 0:
                raise ValueError("Цена товара должна быть неотрицательным целым числом.")

    def add(self, user_id: int, product_name: str, product_price: int):
        """Добавление товара в корзину."""
        self._validate_user_id(user_id)
        self._validate_product(product_name, product_price)

        if user_id not in self.user_carts:
            self.user_carts[user_id] = {}
        if product_name in self.user_carts[user_id]:
            self.user_carts[user_id][product_name]['quantity'] += 1
        else:
            self.user_carts[user_id][product_name] = {'price': product_price, 'quantity': 1}

    def remove(self, user_id: int, product_name: str):
        """Удаление товара из корзины."""
        self._validate_user_id(user_id)
        self._validate_product(product_name)

        if user_id in self.user_carts and product_name in self.user_carts[user_id]:
            del self.user_carts[user_id][product_name]

    def edit_quantity(self, user_id: int, product_name: str, change: int):
        """Изменение количества товара."""
        self._validate_user_id(user_id)
        self._validate_product(product_name)

        if not isinstance(change, int):
            raise ValueError("Изменение количества должно быть целым числом.")

        if user_id in self.user_carts and product_name in self.user_carts[user_id]:
            self.user_carts[user_id][product_name]['quantity'] += change
            if self.user_carts[user_id][product_name]['quantity'] < 1:
                self.remove(user_id, product_name)

    def clear(self, user_id: int):
        """Очистка корзины."""
        self._validate_user_id(user_id)

        if user_id in self.user_carts:
            self.user_carts[user_id] = {}

    def show(self, user_id: int) -> str:
        """Отображение корзины."""
        self._validate_user_id(user_id)

        if user_id not in self.user_carts or not self.user_carts[user_id]:
            return 'Ваша корзина пуста.'

        cart_text = '🛒 Ваша корзина:\n'
        total_price = 0

        for product, info in self.user_carts[user_id].items():
            quantity = info['quantity']
            price = info['price']
            cart_text += f'• {product} - {quantity} шт. x {price} руб = {quantity * price} руб\n'
            total_price += quantity * price

        cart_text += f'\n💰 Общая сумма: {total_price} руб'
        return cart_text

    def get_total_price(self, user_id: int) -> int:
        """Возвращает общую стоимость корзины."""
        self._validate_user_id(user_id)

        return sum(
            item['quantity'] * item['price']
            for item in self.user_carts.get(user_id, {}).values()
        )

cart = Cart()
