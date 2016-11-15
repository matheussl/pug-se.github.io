#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'PUG-SE'
AUTHOR = u'PUG-SE'
THEME = "themes/malt"
MALT_BASE_COLOR = "blue-grey"

# Referências à Github
GITHUB_REPO = "http://github.com/pug-se/pug-se.github.io"
GITHUB_BRANCH = "develop"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Static files
STATIC_PATHS = ['images', 'images/banners']

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python."
SITE_BACKGROUND_IMAGE = "images/banners/background.jpg"
FOOTER_ABOUT = "O PUG-SE é uma comunidade de usuários..."

# Tema do Syntax Hightlight
PYGMENTS_STYLE = "perldoc"

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        "title": "Home",
        "href": "",
    },
    {
        "title": "Chamada de Trabalhos",
        "href": "chamada-de-trabalhos",
    },
    {
        "title": "Sobre",
        "href": "sobre-o-pug-se",
    },
    {
        "title": "Blog",
        "href": "blog",
    }
]

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

LINKS = (('Lista de Discussão', 'https://groups.google.com/forum/#!forum/pug-se'),
         ('Telegram', 'https://telegram.me/pugse'),)

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "https://github.com/pug-se",
        "icon": "fa-github",
        "text": "PUG-SE",
    },
    {
        "href": "http://wiki.python.org.br/",
        "icon": "fa-globe",
        "text": "Python Brasil",
    },
    {
        "href": "https://python.org",
        "icon": "fa-globe",
        "text": "Python",
    },
)

# Membros do Grupy
MEMBROS = OrderedDict((
    ("Matheus Lima", {
        "twitter": "@matheeusLimaaaa",
        "github": "matheussl",
        "site": {
            "nome": "matheuslima.org",
            "href": "http://matheuslima.org",
            }
        }),
    ("Rodrigo Amaral", {
        "github": "rodrigoamaral",
        }
    ),
    ("Erick Mendonça", {
        "github": "erickmendonca",
        }
    ),
    ("Gabriel Araujo", {
        "github": "gabrielaraujof",
        }
    )
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "Nos comunicamos através de mailing " +\
                    "lists, grupo no telegram e no slack, mas frequentemente são " +\
                    "promovidos encontros diversos, como almoços, " +\
                    "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade PUG-SE, apesar de extensa possui alguns " +\
                        "colaboradores principais, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": " Atualmente possuimos poucos projetos em andamento:" +\
                        "Traduções do Django-docs e Python on Campus.",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
    {
        "color": "blue-grey lighten-4",
        "title": "Nossos Eventos",
        "items": [
            {
            "title": "PyBar",
            "icon": "fa-fighter-jet",
            "text": "PyBar é um evento de descontração e conhecimento. " +\
                    "Escolhemos um bar da cidade e pauta da \"reunião\".",
            "buttons": [
                    {
                        "text": "Conheça a agenda",
                        "href": "#",
                    },
                ]
            },
            {
            "title": "Python Day",
            "icon": "fa-gamepad",
            "text": "O Python Day é um evento anual com diversas palestas e treinamentos.",
            }
        ]
    },
    {
        "color": "blue-grey lighten-5",
        "title": "Entre em Contato",
        "items": [
            {
            "title": "",
            },
            {
            "icon": "fa-envelope",
            "buttons": [
                    {
                        "text": "Envie um e-mail!",
                        "href": "#",
                    },
                ]
            }
        ]
    }
    ]

from themes.malt.functions import *
