from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class PersonalInfo(models.Model):
    """Личная информация"""
    first_name = models.CharField(
        max_length=50, 
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=50, 
        verbose_name="Отчество",
        blank=True
    )
    photo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на фото")
    email = models.EmailField(
        verbose_name="Электронная почта",
        validators=[EmailValidator()]
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="Телефон"
    )
    resume = models.TextField(
        verbose_name="Резюме/О себе",
        help_text="Краткая информация о себе, достижениях, интересах"
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активная запись"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Личная информация"
        verbose_name_plural = "Личная информация"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

class EducationalProgram(models.Model):
    """Описание образовательной программы"""
    name = models.CharField(
        max_length=200,
        verbose_name="Название программы"
    )
    university = models.CharField(
        max_length=200,
        verbose_name="Университет"
    )
    faculty = models.CharField(
        max_length=200,
        verbose_name="Факультет",
        blank=True
    )
    program_url = models.URLField(
        verbose_name="Ссылка на страницу программы",
        blank=True
    )
    what_i_study = models.TextField(
        verbose_name="Что я изучаю",
        help_text="Основные дисциплины и предметы"
    )
    what_i_learn = models.TextField(
        verbose_name="Чему научусь",
        help_text="Навыки и компетенции, которые получу"
    )
    advantages = models.TextField(
        verbose_name="Преимущества программы",
        help_text="Уникальные особенности и преимущества"
    )
    career_prospects = models.TextField(
        verbose_name="Перспективы после обучения",
        help_text="Карьерные возможности и перспективы"
    )
    duration = models.CharField(
        max_length=50,
        verbose_name="Длительность обучения",
        help_text="Например: 4 года, 2 года"
    )
    degree_level = models.CharField(
        max_length=50,
        verbose_name="Уровень образования",
        choices=[
            ('bachelor', 'Бакалавриат'),
            ('master', 'Магистратура'),
            ('specialist', 'Специалитет'),
            ('phd', 'Аспирантура'),
        ]
    )
    start_year = models.IntegerField(
        verbose_name="Год начала обучения"
    )
    end_year = models.IntegerField(
        verbose_name="Год окончания обучения"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активная запись"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.name} ({self.university})"

    @property
    def advantages_list(self):
        """Возвращает список преимуществ"""
        return [adv.strip() for adv in self.advantages.split('\n') if adv.strip()]

class Management(models.Model):
    """Менеджмент образовательной программы"""
    ROLE_CHOICES = [
        ('academic_director', 'Академический руководитель'),
        ('program_manager', 'Менеджер программы'),
        ('coordinator', 'Координатор'),
        ('dean', 'Декан'),
        ('vice_dean', 'Заместитель декана'),
    ]

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        blank=True
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        verbose_name="Должность"
    )
    photo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на фото")
    email = models.EmailField(
        verbose_name="Электронная почта",
        validators=[EmailValidator()]
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="Телефон",
        blank=True
    )
    department = models.CharField(
        max_length=200,
        verbose_name="Кафедра/Отдел",
        blank=True
    )
    academic_degree = models.CharField(
        max_length=100,
        verbose_name="Ученая степень",
        blank=True
    )
    bio = models.TextField(
        verbose_name="Биография",
        blank=True,
        help_text="Краткая информация о деятельности"
    )
    order = models.IntegerField(
        default=0,
        verbose_name="Порядок отображения"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активная запись"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Сотрудник менеджмента"
        verbose_name_plural = "Менеджмент программы"
        ordering = ['order', 'role', 'last_name']

    def __str__(self):
        return f"{self.full_name} - {self.get_role_display()}"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    @property
    def bio_paragraphs(self):
        """Возвращает список параграфов биографии"""
        return [p.strip() for p in self.bio.split('\n') if p.strip()]

class Classmate(models.Model):
    """Сокурсники"""
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия"
    )
    middle_name = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        blank=True
    )
    photo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на фото")
    email = models.EmailField(
        verbose_name="Электронная почта",
        validators=[EmailValidator()]
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр."
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="Телефон",
        blank=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        blank=True
    )
    group_number = models.CharField(
        max_length=20,
        verbose_name="Номер группы",
        blank=True
    )
    interests = models.TextField(
        verbose_name="Интересы",
        blank=True,
        help_text="Хобби, интересы, увлечения"
    )
    social_vk = models.URLField(
        verbose_name="ВКонтакте",
        blank=True
    )
    social_telegram = models.CharField(
        max_length=100,
        verbose_name="Telegram",
        blank=True,
        help_text="Например: @username"
    )
    social_instagram = models.CharField(
        max_length=100,
        verbose_name="Instagram",
        blank=True,
        help_text="Например: @username"
    )
    is_close_friend = models.BooleanField(
        default=False,
        verbose_name="Близкий друг",
        help_text="Отметить как близкого друга"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активная запись"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Сокурсник"
        verbose_name_plural = "Сокурсники"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    @property
    def interests_list(self):
        """Возвращает список интересов"""
        return [interest.strip() for interest in self.interests.split('\n') if interest.strip()]
