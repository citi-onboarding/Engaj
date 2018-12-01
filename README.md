# Site - ENGAJ
A ENGAJ é a empresa Júnior do curso de Engenharia Ambiental da USP São Carlos. Essa one-page foi costruída durante o PSC 2018.2. Preview: http://engaj-staging.herokuapp.com/

## Primeiros passos
Siga estes passos, caso queira ter uma cópia do projeto configurada e executando no seu host local, para propósitos de desenvolvimento e testes. Veja a seção `Realizando Deploy` para entender como fazer a instalação em um ambiente de produção.

### Requisitos
Nesse tutorial, está coberto apenas o procedimento para configuração em um ambiente Linux. Assim, é necessário possuir `python3` e `virtualenv` instalandos. Caso não os possua, é possível obtê-los no Ubuntu pelo comando:

```
sudo apt install python3 virtualenv -y
```

### Ambiente para desenvolvimento
Inicialmente, obtenha o código da aplicação. Utilizando o git, você teria algo assim:

```
git clone https://github.com/citi-onboarding/Engaj.git
```

entre no diretório `Engaj/`:

```
cd Engaj/
```

Crie uma pasta para o ambiente virtual:

```
mkdir env/
```

Crie o ambiente virtual. Nesse caso, usando o `virtualenv` no Linux, basta executar:

```
virtualenv env/ -p python3
```
Ative-o:

```
source env/bin/activate
```

Instale todas as dependências contidas no `requirements.txt`

```
pip install -r requirements.txt
```
Para testar se tudo foi corretamente instalado, basta executar:

```
python manage.py runserver
```
E acessar o endereço https://locahost:8000 em um navegador como Chrome, Firefox ou Safari.

## Realizando Deploy
Veja [Deploy com Heroku](https://devcenter.heroku.com/articles/github-integration#enabling-github-integration) para mais informações

## Ferramentas

* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Ferramenta de criação dos ambientes virtuais em python
* [Slick](http://kenwheeler.github.io/slick/) - Framework para criação dos carrosseis
* [Parallax.js](http://pixelcog.github.io/parallax.js/) - Script para fazer o efeito de parallax
* [Django Storage](https://django-storages.readthedocs.io/en/latest/) - Biblioteca para mudar onde os arquivos de mídia são armazenados
* [Heroku](https://dashboard.heroku.com/) - Plataforma usada para deploy

## Autores

* **Júnior Mendes** - [jrmmendes](https://github.com/jrmmendes)
* **Ana Beatriz** - [abcr98](https://github.com/abcr98)
* **Lucas Zacarias** - [lucaszsd](https://github.com/lucaszsd)
