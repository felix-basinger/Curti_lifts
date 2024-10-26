from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('chi_siamo/', views.chi_siamo, name='chi_siamo'),
    path('impianto_oleodinamico/', views.impianto_oleodinamico, name='impianto_oleodinamico'),
    path('impianto_elettrico/', views.impianto_elettrico, name='impianto_elettrico'),
    path('impianti_speciali/', views.impianti_speciali, name='impianti_speciali'),
    path('piattaforme_elevatrici/', views.piattaforme_elevatrici, name='piattaforme_elevatrici'),
    path('scale_mobili/', views.scale_mobili, name='scale_mobili'),
    path('tappeti_mobili/', views.tappeti_mobili, name='tappeti_mobili'),
    path('marciapiedi_mobili/', views.marciapiedi_mobili, name='marciapiedi_mobili'),
    path('gallery/', views.gallery, name='gallery'),
    path('contatti/', views.contatti, name='contatti'),
    path('ascensori_montacarichi_e_piattaforme/', views.ascensori_montacarichi_e_piattaforme,
         name='ascensori_montacarichi_e_piattaform'),
    path('scale_e_tappeti_mobili/', views.scale_e_tappeti_mobili, name='scale_e_tappeti_mobili'),
    path('cookie_policy/', views.cookie_policy, name='cookie_policy'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
