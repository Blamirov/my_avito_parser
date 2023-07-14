
class DataInfo:
    """Класс для сбора информации со страницы объявления """

    def __init__(self):
        self.num = None  # Порядковый номер
        self.position = None  # Позиция
        self.header = None  # Название объявления
        self.price = None  # Цена
        self.down_price = None  # Понижение цены
        self.views_total = None  # Всего просмотров
        self.views_today = None  # Просмотров за сегодня
        self.method_promotions = None  # Методы продвижения
        self.refresh_time = None  # Время последнего поднятия
        self.amount_photo = None  # Количество фотографий
        self.text = None  # Текст, описание товара
        self.amount_signs = None  # Количество знаков
        self.delivery = None  # Доставка
        self.sellers_name = None  # Имя продавца
        self.sellers_id = None   # id продавца
        self.announcements_id = None  # id объявления
        self.active_announcements = None  # Активные объявления
        self.address = None  # Адрес продавца
        self.web_link = None  # Ссылка
        self.photo = None  # Фото
        self.seller_web = None
