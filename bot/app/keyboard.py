"""
Модуль для создания различных клавиатур и кнопок с использованием aiogram.

Этот модуль содержит функции для генерации стандартных клавиатур (ReplyKeyboardMarkup)
и инлайн-клавиатур (InlineKeyboardMarkup), которые используются в чат-боте Telegram.
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



async def main():
    """
    Создаёт стандартную клавиатуру с кнопками "Меню" и "Корзина".

    Эта клавиатура отображается как обычные кнопки под полем ввода.

    Returns:
        ReplyKeyboardMarkup: Клавиатура с кнопками "Меню" и "Корзина".
    """
    # Создаём клавиатуру с двумя кнопками в одной строке
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Меню'), KeyboardButton(text='Корзина'), KeyboardButton(text='Поиск')]
    ], input_field_placeholder='Выберите:')  # Устанавливаем текст-заполнитель для поля ввода


async def options():
    """
    Создаёт инлайн-клавиатуру с основными разделами меню.

    Инлайн-кнопки отображаются прямо в сообщении и отправляют callback-запросы при нажатии.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с разделами меню.
    """
    # Создаём инлайн-кнопки для основных разделов
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Основное меню', callback_data='selected_Основное_меню')],
        [InlineKeyboardButton(text='Напитки и десерты', callback_data='selected_Напитки_и_десерты')],
        [InlineKeyboardButton(text='Комплексные обеды', callback_data='selected_Комплексные_обеды')],
    ])


async def added():
    """
    Создаёт инлайн-кнопки для перехода в корзину или возвращения к выбору разделов.

    Используется для взаимодействия с корзиной.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками "Перейти в корзину" и "Выбор раздела".
    """
    # Создаём кнопки для перехода в корзину или возврата к выбору разделов
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перейти в корзину', callback_data='selected_Перейти_в_корзину')],
        [InlineKeyboardButton(text='🔙Выбор раздела', callback_data='selected_🔙Выбор_раздела')],
    ])


async def to_new_order():
    """
    Создаёт инлайн-кнопку для создания нового заказа.

    Возвращает клавиатуру с одной кнопкой.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопкой "Сделать еще заказ".
    """
    # Кнопка для оформления нового заказа
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сделать еще заказ', callback_data='selected_Сделать_еще_заказ')],
    ])


async def create_buttons(option):
    """
    Создаёт инлайн-кнопки на основе переданного списка опций.

    Каждая строка клавиатуры содержит одну кнопку, соответствующую элементу из списка.

    Args:
        option (list): Список строк, каждая из которых станет текстом кнопки.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура, где каждая кнопка находится в отдельной строке.
    """
    buttons = []
    for text in option:
        # Преобразуем текст в callback_data, заменяя пробелы на подчёркивания
        callback_data = f'selected_{text}'.replace(' ', '_')
        # Создаём кнопку с текстом и соответствующим callback_data
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        # Добавляем кнопку в отдельной строке
        buttons.append([button])
    # Возвращаем готовую клавиатуру
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def cart_buttons():
    """
    Создаёт инлайн-кнопки для управления корзиной.

    Кнопки позволяют редактировать количество товаров, оплатить или очистить корзину.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками для управления корзиной.
    """
    # Кнопки для управления содержимым корзины
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Редактировать количество', callback_data='redact_quantity')],
        [InlineKeyboardButton(text='Оплатить', callback_data='pay_cart')],
        [InlineKeyboardButton(text='Очистить корзину', callback_data='clear_cart')],
    ])


async def quantity_buttons(product):
    """
    Создаёт инлайн-кнопки для изменения количества товара.

    Клавиатура содержит кнопки для увеличения, уменьшения количества и возврата в корзину.

    Args:
        product (str): Идентификатор товара.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками изменения количества и возврата.
    """
    # Кнопки для увеличения, уменьшения количества и возврата в корзину
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data=f'increase_{product}'),  # Увеличить количество
            InlineKeyboardButton(text='➖', callback_data=f'decrease_{product}')  # Уменьшить количество
        ],
        [InlineKeyboardButton(text='🔙В корзину', callback_data='back_to_cart')],  # Возврат в корзину
    ])


async def create_edit_quantity_buttons(cart):
    """
    Создаёт инлайн-кнопки для выбора товара из корзины для редактирования.

    Включает одну кнопку для каждого товара и кнопку возврата.

    Args:
        cart (list): Список товаров в корзине.

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками для каждого товара и кнопкой "Назад".
    """
    # Генерируем кнопки для каждого товара в корзине
    buttons = [
        [InlineKeyboardButton(text=str(product), callback_data=f'edit_{product.replace(' ', '_')}')]
        for product in cart
    ]
    # Добавляем кнопку "Назад" для возврата
    buttons.append([InlineKeyboardButton(text='Назад', callback_data='back_to_cart')])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def create_clear_cart_buttons():
    """
    Создаёт инлайн-кнопки для подтверждения очистки корзины.

    Клавиатура включает кнопки подтверждения ("Да") и отмены ("Нет").

    Returns:
        InlineKeyboardMarkup: Инлайн-клавиатура с кнопками "Да" и "Нет".
    """
    # Кнопки для подтверждения или отмены очистки корзины
    buttons = [
        [InlineKeyboardButton(text='Да', callback_data='confirm_clear_cart')],  # Подтвердить очистку
        [InlineKeyboardButton(text='Нет', callback_data='back_to_cart')],       # Отменить очистку
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

async def search_keyboard(product_name):
    InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить в корзину",
                    callback_data=f'selected_{product_name}'.replace(' ', '_')
                )
            ]
        ]
    )