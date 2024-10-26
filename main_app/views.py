from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse


def index(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/index.html')


from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Проверка, что все поля заполнены
        if name and email and message:
            try:
                # Формируем HTML-шаблон для письма
                email_content = render_to_string('email_template.html', {
                    'name': name,
                    'email': email,
                    'message': message,
                })

                # Настройка письма
                email_message = EmailMessage(
                    subject=f'Сообщение от {name}',  # Тема письма
                    body=email_content,  # Тело письма (HTML)
                    from_email='basingerfelix17@gmail.com',  # От кого (должно совпадать с настройками SMTP)
                    to=['basingerfelix17@gmail.com'],  # Кому
                )

                # Указываем, что письмо в формате HTML
                email_message.content_subtype = 'html'

                # Отправляем письмо
                email_message.send(fail_silently=False)

                # Добавляем сообщение об успешной отправке
                messages.success(request, 'La mail è stata inviata con successo!')

                # Перенаправляем на главную страницу после успешной отправки
                return HttpResponseRedirect(reverse('index'))

            except Exception as e:
                messages.error(request, f"Errore nell'invio del messaggio: {e}")

    return render(request, 'main_app/index.html')


def chi_siamo(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/chi_siamo.html')


def impianto_oleodinamico(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/impianto_oleodinamico.html')


def impianto_elettrico(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/impianto_elettrico.html')


def impianti_speciali(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/impianti_speciali.html')


def piattaforme_elevatrici(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/piattaforme_elevatrici.html')


def scale_mobili(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/scale_mobili.html')


def tappeti_mobili(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/tappeti_mobili.html')


def marciapiedi_mobili(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/marciapiedi_mobili.html')


def gallery(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/gallery.html')


def contatti(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/contatti.html')


def ascensori_montacarichi_e_piattaforme(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/ascensori_montacarichi_e_piattaforme.html')


def scale_e_tappeti_mobili(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/scale_e_tappeti_mobili.html')


def cookie_policy(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/cookie_policy.html')


def privacy_policy(request):
    # Рендерим шаблон главной страницы
    return render(request, 'main_app/privacy_policy.html')
