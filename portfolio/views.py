from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import PersonalInfo, EducationalProgram, Management, Classmate


def home(request):
    """Главная страница - Я"""
    personal_info = PersonalInfo.objects.filter(is_active=True).first()

    # Статистика для главной страницы
    stats = {
        "classmates_count": Classmate.objects.filter(is_active=True).count(),
        "management_count": Management.objects.filter(is_active=True).count(),
        "programs_count": EducationalProgram.objects.filter(is_active=True).count(),
    }

    context = {
        "personal_info": personal_info,
        "stats": stats,
    }
    return render(request, "portfolio/home.html", context)


def about_me(request):
    """Страница 'Я' с подробной информацией"""
    personal_info = PersonalInfo.objects.filter(is_active=True).first()

    if not personal_info:
        # Если нет записи, создаем пустую для отображения формы в админке
        context = {"personal_info": None}
    else:
        context = {"personal_info": personal_info}

    return render(request, "portfolio/about_me.html", context)


def educational_program(request):
    """Страница описания образовательной программы"""
    programs = EducationalProgram.objects.filter(is_active=True)

    # Фильтрация
    search = request.GET.get("search", "")
    degree_level = request.GET.get("degree_level", "")

    if search:
        programs = programs.filter(
            Q(name__icontains=search)
            | Q(university__icontains=search)
            | Q(faculty__icontains=search)
        )

    if degree_level:
        programs = programs.filter(degree_level=degree_level)

    # Сортировка
    sort_by = request.GET.get("sort_by", "-start_year")
    if sort_by:
        programs = programs.order_by(sort_by)

    # Пагинация
    paginator = Paginator(programs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Варианты для фильтров
    degree_choices = EducationalProgram._meta.get_field("degree_level").choices

    context = {
        "page_obj": page_obj,
        "search": search,
        "degree_level": degree_level,
        "sort_by": sort_by,
        "degree_choices": degree_choices,
        "total_count": programs.count(),
    }
    return render(request, "portfolio/educational_program.html", context)


def program_detail(request, pk):
    """Детальная информация о программе"""
    program = get_object_or_404(EducationalProgram, pk=pk, is_active=True)

    context = {
        "program": program,
    }
    return render(request, "portfolio/program_detail.html", context)


def management(request):
    """Страница менеджмента программы"""
    management_list = Management.objects.filter(is_active=True)

    # Фильтрация
    search = request.GET.get("search", "")
    role = request.GET.get("role", "")
    department = request.GET.get("department", "")

    if search:
        management_list = management_list.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
            | Q(department__icontains=search)
        )

    if role:
        management_list = management_list.filter(role=role)

    if department:
        management_list = management_list.filter(department__icontains=department)

    # Сортировка
    sort_by = request.GET.get("sort_by", "order")
    if sort_by:
        management_list = management_list.order_by(sort_by)

    # Группировка по ролям для удобного отображения
    academic_directors = management_list.filter(role="academic_director")
    managers = management_list.filter(role="program_manager")
    coordinators = management_list.filter(role="coordinator")
    deans = management_list.filter(role__in=["dean", "vice_dean"])

    # Варианты для фильтров
    role_choices = Management._meta.get_field("role").choices
    departments = (
        Management.objects.filter(is_active=True)
        .values_list("department", flat=True)
        .distinct()
    )

    context = {
        "management_list": management_list,
        "academic_directors": academic_directors,
        "managers": managers,
        "coordinators": coordinators,
        "deans": deans,
        "search": search,
        "role": role,
        "department": department,
        "sort_by": sort_by,
        "role_choices": role_choices,
        "departments": [d for d in departments if d],
        "total_count": management_list.count(),
    }
    return render(request, "portfolio/management.html", context)


def classmates(request):
    """Страница сокурсников"""
    classmates_list = Classmate.objects.filter(is_active=True)

    # Фильтрация
    search = request.GET.get("search", "")
    city = request.GET.get("city", "")
    group_number = request.GET.get("group_number", "")

    if search:
        classmates_list = classmates_list.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
            | Q(interests__icontains=search)
        )

    if city:
        classmates_list = classmates_list.filter(city__icontains=city)

    if group_number:
        classmates_list = classmates_list.filter(group_number=group_number)

    # Сортировка
    sort_by = request.GET.get("sort_by", "last_name")
    if sort_by:
        classmates_list = classmates_list.order_by(sort_by)

    # Пагинация
    paginator = Paginator(classmates_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Варианты для фильтров
    cities = (
        Classmate.objects.filter(is_active=True)
        .values_list("city", flat=True)
        .distinct()
    )
    groups = (
        Classmate.objects.filter(is_active=True)
        .values_list("group_number", flat=True)
        .distinct()
    )

    context = {
        "page_obj": page_obj,
        "search": search,
        "city": city,
        "group_number": group_number,
        "sort_by": sort_by,
        "cities": [c for c in cities if c],
        "groups": [g for g in groups if g],
        "total_count": classmates_list.count(),
    }
    return render(request, "portfolio/classmates.html", context)


def classmate_detail(request, pk):
    """Детальная информация о сокурснике"""
    classmate = get_object_or_404(Classmate, pk=pk, is_active=True)

    context = {
        "classmate": classmate,
    }
    return render(request, "portfolio/classmate_detail.html", context)
